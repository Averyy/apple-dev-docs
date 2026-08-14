# Building an audio sequencer to arrange and play clips

**Framework**: AVFAudio

Synchronize audio loops with a main tempo by creating a real-time clip launcher.

**Availability**:
- macOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Synchronizing multiple audio loops with different tempos requires precise timing control — small errors in playback rate or scheduling compound over time and pull clips out of sync.

This sample builds a grid-based clip launcher that synchronizes multiple audio loops in real time, adjusting their playback rates to match a main tempo while maintaining sample-accurate timing. The sample uses Swift concurrency features for thread-safe buffer sharing and concurrent audio metering. The app uses an actor to handle file input and audio analysis on background threads, while the main actor manages audio engine operations. The sample demonstrates:

- Automatic BPM detection using the [`Music Understanding`](https://developer.apple.com/documentation/musicunderstanding) framework.
- Per-track rate adjustment to synchronize loops with different BPMs
- Quantized clip launching aligned to bar boundaries
- Drift-free looping through manual buffer rescheduling
- Real-time volume unit (VU) metering with smooth decay

#### Load Clips and Detect Tempo

The `ClipLoader` actor performs file operations on background threads while analyzing audio files to detect tempo information. It uses [`AVReadOnlyAudioPCMBuffer`](avreadonlyaudiopcmbuffer.md) for thread-safe buffer sharing across actor boundaries:

```swift
actor ClipLoader {
    func load(from url: URL) async throws -> (clip: AudioClip, statusMessage: String) {
        let file = try AVAudioFile(forReading: url)

        let frames = AVAudioFrameCount(file.length)

        // Single read into a read-only buffer for analysis, playback, and waveform extraction.
        let buffer = try file.read(frameCount: frames)

        let duration = Double(buffer.frameLength) / buffer.format.sampleRate

        // Analyze the rhythm with the Music Understanding framework.
        guard let rhythm = await analyzeRhythm(from: buffer, duration: duration) else {
            throw LoadError.bpmDetectionFailed(url.lastPathComponent)
        }
        guard let detectedBPM = rhythm.beatsPerMinute else {
            throw LoadError.bpmDetectionFailed(url.lastPathComponent)
        }
        let bpmValue = Double(round(detectedBPM))

        // Use the beat times that the Music Understanding framework detects.
        let beatTimes: [Double]
        if !rhythm.beats.isEmpty {
            beatTimes = rhythm.beats.map { CMTimeGetSeconds($0) }
            print("MusicUnderstanding: \(beatTimes.count) beats detected")
        } else {
            beatTimes = []
            print("MusicUnderstanding: No beat grid detected")
        }

        let amplitudes = WaveformExtractor.makeRMSBarsExact(from: buffer, targetPoints: Constants.Waveform.targetPoints)
        let name = url.deletingPathExtension().lastPathComponent

        let clip = AudioClip(
            id: UUID(),
            buffer: buffer,
            bpm: bpmValue,
            duration: duration,
            amplitudes: amplitudes,
            beatTimes: beatTimes
        )

        let status = "Loaded \(name) @ \(Int(round(clip.bpm))) BPM"
        return (clip, status)
    }
}
```

The clip loader analyzes audio content to detect BPM using the [`Music Understanding`](https://developer.apple.com/documentation/musicunderstanding) framework. For clips shorter than 15 seconds, the `analyzeRhythm` helper repeats the audio to provide enough data for accurate tempo detection.

#### Configure the Audio Engine

The audio engine uses a per-track signal path architecture that enables independent processing and metering for each track. When you load a clip, the engine creates a dedicated chain of audio nodes and connects them to the mixer hierarchy:

```swift
func loadClip(_ clip: AudioClip, into track: TrackID) {
    ensureTrack(track)
    // Remove the existing clip with the same ID, if present.
    if let existing = clips[track]?[clip.id] {
        existing.node.stop()
        engine.disconnectNodeOutput(existing.node)
        engine.disconnectNodeOutput(existing.varispeed)
        engine.detach(existing.node)
        engine.detach(existing.varispeed)
    }

    let node = AVAudioPlayerNode()
    let varispeed = AVAudioUnitVarispeed()
    varispeed.rate = playbackRate(for: clip)
    engine.attach(node)
    engine.attach(varispeed)
    do {
        try engine.connectNode(node, to: varispeed, format: clip.buffer.format)
    } catch {
        print("ClipEngine: Failed to connect player node to varispeed: \(error)")
    }

    // Connect to track mixer, which feeds into `MainMixer`.
    // Audio graph: PlayerNode > Varispeed > TrackMixer > MainMixer.
    if let trackMixer = trackMixers[track] {
        do {
            try engine.connectNode(varispeed, to: trackMixer, format: clip.buffer.format)
        } catch {
            print("ClipEngine: Failed to connect varispeed to track mixer: \(error)")
        }
    } else {
        // Fallback (shouldn't happen if calling `ensureTrack`).
        do {
            try engine.connectNode(varispeed, to: mixer, format: clip.buffer.format)
        } catch {
            print("ClipEngine: Failed to connect varispeed to main mixer: \(error)")
        }
    }
    clips[track, default: [:]][clip.id] = LoadedClip(
        clip: clip,
        node: node,
        varispeed: varispeed
    )
}
```

Each track has its own [`AVAudioMixerNode`](avaudiomixernode.md) that connects to the main mixer, allowing the sample to load new clips without disconnecting currently playing clips. The [`AVAudioUnitVarispeed`](avaudiounitvarispeed.md) node adjusts the playback rate based on the clip’s BPM and the main tempo, so that all loops play in sync.

#### Quantize Clip Launches

When a person launches a clip, the engine defers playback to the next bar boundary so that all clips stay in musical sync. The `TransportTiming` structure calculates the next quantized start time based on the transport grid:

```swift
func quantizedStart(
    nowSeconds: Double,
    transportStartSeconds: Double?,
    tempo: Double
) -> QuantizedStart {
    let secPerBar = secondsPerBar(tempo: tempo)

    guard let startSeconds = transportStartSeconds else {
        // For the first clip, start one quantization period in the future.
        let offset = secPerBar * quantizationBars
        return QuantizedStart(
            offsetSeconds: offset,
            newTransportStart: nowSeconds + offset
        )
    }

    let elapsed = nowSeconds - startSeconds
    let barsElapsed = elapsed / secPerBar
    let quantizedBars = barsElapsed / quantizationBars

    // Check if the time is within the tolerance of a bar boundary.
    let fractionalPart = quantizedBars - floor(quantizedBars)

    let nextBar: Double
    if fractionalPart < Self.barSnapTolerance {
        // If the time is just past a boundary, snap to the current bar then start immediately.
        nextBar = floor(quantizedBars) * quantizationBars
    } else if fractionalPart > (1.0 - Self.barSnapTolerance) {
        // If the time is just before the next boundary, snap to the next bar.
        nextBar = ceil(quantizedBars) * quantizationBars
    } else {
        // Wait for the next bar.
        nextBar = ceil(quantizedBars) * quantizationBars
    }

    let targetSeconds = startSeconds + nextBar * secPerBar
    let offset = max(0, targetSeconds - nowSeconds)

    return QuantizedStart(
        offsetSeconds: offset,
        newTransportStart: startSeconds // Unchanged.
    )
}
```

For the first clip, the method establishes the transport grid and schedules playback one bar in the future. For subsequent clips, it snaps to the nearest bar boundary using a 2 percent tolerance window to account for minor timing variations. This ensures that clips launched at slightly different moments still start on the beat.

#### Create Drift Free Looping

Instead of using the built-in looping option on [`AVAudioPlayerNode`](avaudioplayernode.md), the sample manually reschedules clips at each loop boundary. This avoids the timing drift that accumulates from floating-point errors over many iterations. A timer monitors loop end times and schedules the next iteration precisely when necessary.

```swift
func scheduleClip(_ loaded: LoadedClip, track: TrackID, startHostTime: UInt64) {
    loaded.varispeed.rate = playbackRate(for: loaded.clip)
    loaded.node.stop()

    // Start at zero volume, then ramp up to avoid clicks from non-zero-crossing starts.
    // The audio engine smooths volume changes over its render buffer (~5 ms).
    loaded.node.volume = 0

    // Schedule the buffer for a single iteration without using the `.loops` option.
    // Manually reschedule at each loop boundary to maintain sync with the transport grid.
    //
    // This approach prevents long-term drift that occurs when the internal looping of
    // `AVAudioPlayerNode` accumulates floating-point errors over many iterations.
    loaded.node.scheduleBuffer(
        loaded.clip.buffer,
        atTime: AVAudioTime(hostTime: startHostTime),
        options: [],
        completionHandler: nil
    )

    do {
        try loaded.node.playAudio(at: AVAudioTime(hostTime: startHostTime))
    } catch {
        print("ClipEngine: Failed to start playback: \(error)")
    }
    loaded.node.volume = 1
    notifyLaunch(track: track, clipID: loaded.clip.id, at: startHostTime)
    activeClipID[track] = loaded.clip.id
    startTimes[track] = startHostTime

    // Calculate when this loop iteration ends and store it for resync.
    let loopDurationSeconds = clipDuration(loaded)
    let endHostTime = startHostTime &+ AVAudioTime.hostTime(forSeconds: loopDurationSeconds)
    loopEndHostTimes[track] = endHostTime

    // Start the resync timer if not already running.
    startResyncTimerIfNeeded()
}
```

The resync timer checks every 50 ms whether any playing clips are approaching their loop boundaries. When a clip is within 100 ms of the loop boundary, the engine reschedules the next iteration to start exactly when the current one ends:

```swift
func rescheduleLoop(track: TrackID, loaded: LoadedClip, currentLoopEndHostTime: UInt64) {
    // Start the next loop when the current one ends to maintain accurate timing without drift.
    let nextStartHostTime = currentLoopEndHostTime

    // Schedule the next buffer iteration.
    loaded.node.scheduleBuffer(
        loaded.clip.buffer,
        atTime: AVAudioTime(hostTime: nextStartHostTime),
        options: [],
        completionHandler: nil
    )

    // Update the loop end time for the next iteration.
    let loopDurationSeconds = clipDuration(loaded)
    let nextEndHostTime = nextStartHostTime &+ AVAudioTime.hostTime(forSeconds: loopDurationSeconds)
    loopEndHostTimes[track] = nextEndHostTime
}
```

This approach maintains sample-accurate synchronization across all tracks and prevents the gradual timing drift that occurs with the built-in looping option.

#### Adapt to Tempo Changes

When the tempo changes, the engine clamps the value to the valid range and updates all [`AVAudioUnitVarispeed`](avaudiounitvarispeed.md) nodes so that every clip immediately plays at the correct rate for the new tempo:

```swift
func setTempo(_ bpm: Double) {
    tempo = max(Constants.BPM.minTempo, min(bpm, Constants.BPM.maxTempo))
    updateAllRates()
}
```

The `updateAllRates` method iterates over every loaded clip and sets its varispeed rate to the ratio of the main tempo to the clip’s original BPM. This keeps all loops synchronized regardless of their native tempos.

```swift
func updateAllRates() {
    for trackClips in clips.values {
        for loaded in trackClips.values {
            loaded.varispeed.rate = playbackRate(for: loaded.clip)
        }
    }
}
```

The [`AVAudioUnitVarispeed`](avaudiounitvarispeed.md) node applies the rate change in real time, so clips adjust their playback speed instantly without interrupting playback.

#### Perform Audio Metering

The `AudioLevelTap` class monitors audio levels using [`installAudioTap(onBus:bufferSize:format:tapProvider:)`](avaudionode/installaudiotap(onbus:buffersize:format:tapprovider:).md), which receives [`AVReadOnlyAudioPCMBuffer`](avreadonlyaudiopcmbuffer.md) for thread-safe concurrent processing. The tap block runs on the audio thread and uses the [`Accelerate`](https://developer.apple.com/documentation/accelerate) framework for efficient peak detection:

```swift
@Observable
@MainActor
public final class AudioLevelTap {
    public private(set) var level: Float = 0
    private let state = LevelState()
    private var refreshTask: Task<Void, Never>?

    public func attach(to node: AVAudioNode) {
        let format = node.outputFormat(forBus: Self.bus)
        let sampleRate = Float(format.sampleRate)

        // Install a sendable tap block to receive `AVReadOnlyAudioPCMBuffer`.
        do {
            try node.installAudioTap(
                onBus: Self.bus, bufferSize: Constants.Metering.tapBufferSize, format: format
            ) { [state] buffer, _ in
                // The buffer is an `AVReadOnlyAudioPCMBuffer` that conforms to `Sendable`.
                let channelData = buffer.channelData(0)
                guard case .float(let samples) = channelData else { return }

                // Get the peak magnitude from the buffer using the Accelerate framework.
                var peak: Float = 0
                samples.withUnsafeBufferPointer { ptr in
                    guard let baseAddress = ptr.baseAddress else { return }
                    // Use the span's own count, which may be shorter than `frameLength`.
                    vDSP_maxmgv(baseAddress, 1, &peak, vDSP_Length(ptr.count))
                }

                // Calculate the decay factor based on the sample rate and buffer size.
                let numFrames = Float(buffer.frameLength)
                let decay = powf(1.0 - Constants.Metering.decayRateMultiplier / sampleRate, numFrames)

                // Update the peak state from the audio render thread, which is the single writer.
                state.updatePeak(peak, decay: decay)
            }
        } catch {
            print("AudioLevelTap: Failed to install tap on bus \(Self.bus): \(error)")
            return
        }

        // Start the UI refresh task using structured concurrency.
        refreshTask = Task { [weak self, state] in
            while !Task.isCancelled {
                try? await Task.sleep(for: .seconds(Constants.Metering.uiRefreshInterval))
                guard let self else { break }

                let currentPeak = state.currentPeak
                // Apply a -140 dB threshold.
                self.level = currentPeak < Self.minus140dB ? 0 : currentPeak
            }
        }
    }
}
```

The level state uses lock-free atomic operations to communicate between the audio render thread and the main actor. The class stores peak values as `ManagedAtomic<UInt32>` with bit-pattern conversion, keeping the audio callback free of blocking synchronization.

```swift
private final class LevelState: Sendable {
    private let _peak = ManagedAtomic<UInt32>(0)

    var currentPeak: Float {
        Float(bitPattern: _peak.load(ordering: .relaxed))
    }

    func updatePeak(_ newPeak: Float, decay: Float) {
        let decayed = Float(bitPattern: _peak.load(ordering: .relaxed)) * decay + Float.leastNonzeroMagnitude
        _peak.store(max(decayed, newPeak).bitPattern, ordering: .relaxed)
    }
}
```

This architecture keeps audio metering responsive and accurate without adding `Task` overhead or executor hops, both of which can disrupt timing-critical audio callbacks. The smooth decay produces natural VU meter movement that tracks the audio’s perceived loudness.

## See Also

- [Playing custom audio with your own player](playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [Using voice processing](using-voice-processing.md)
  Add voice-processing capabilities to your app by using audio engine.
- [class AVAudioPlayerNode](avaudioplayernode.md)
  An object for scheduling the playback of buffers or segments of audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/building-an-audio-sequencer-to-arrange-and-play-clips)*