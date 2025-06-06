# Classifying Sounds in an Audio Stream

**Framework**: Sound Analysis

Identify individual sounds in an audio data stream, such as from a microphone, with an audio stream analyzer.

#### Overview

Use an [`SNAudioStreamAnalyzer`](snaudiostreamanalyzer.md) to recognize sounds, such as human speech, music, and singing, by processing an audio stream, such as from a microphone. For example, a sound recording app can use an audio stream analyzer to show a visual label for sounds the app identifies in real time.

This article builds on the [`Classifying Sounds in an Audio File`](classifying-sounds-in-an-audio-file.md) article, including:

- Creating an [`SNClassifySoundRequest`](snclassifysoundrequest.md)
- Implementing a type that conforms to [`SNResultsObserving`](snresultsobserving.md)

##### Start an Audio Engine

The [`Audio Engine`](https://developer.apple.com/documentation/AVFAudio/audio-engine) API simplifies audio-related tasks, including capturing audio data with a microphone.

Capture audio data from the device’s default microphone:

1. Create an [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine) instance.
2. Save a reference to the microphone’s [`AVAudioFormat`](https://developer.apple.com/documentation/AVFAudio/AVAudioFormat) instance.
3. Begin the audio pipeline’s data flow by calling the engine’s [`start()`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine/start()) method.

```swift
func startAudioEngine() {
    // Create a new audio engine.
    audioEngine = AVAudioEngine()

    // Get the native audio format of the engine's input bus.
    inputBus = AVAudioNodeBus(0)
    inputFormat = audioEngine.inputNode.inputFormat(forBus: inputBus)
    
    do {
        // Start the stream of audio data.
        try audioEngine.start()
    } catch {
        print("Unable to start AVAudioEngine: \(error.localizedDescription)")
    }
}
```

When you create an audio engine instance, its default [`inputNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine/inputNode) accesses audio data from the device’s default microphone.

> ❗ **Important**:  To access the device’s microphone in iOS or watchOS, add a description for the [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) key in your project’s `Info.plist` file.

 To access the device’s microphone in iOS or watchOS, add a description for the [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) key in your project’s `Info.plist` file.

##### Create a Stream Analyzer

Analyze the microphone audio by configuring an [`SNAudioStreamAnalyzer`](snaudiostreamanalyzer.md) to the input device’s native PCM (pulse code modulation) audio format.

```swift
// Create a new stream analyzer.
streamAnalyzer = SNAudioStreamAnalyzer(format: inputFormat)
```

Audio stream analyzers only work with audio data in the PCM format, unlike [`SNAudioFileAnalyzer`](snaudiofileanalyzer.md) instances.

> ❗ **Important**:  If the input device’s audio format changes, you must discard the current `SNAudioStreamAnalyzer` and create a new one that matches the input’s updated audio format.

 If the input device’s audio format changes, you must discard the current `SNAudioStreamAnalyzer` and create a new one that matches the input’s updated audio format.

Create a sound classification request and a results observer (see [`Classifying Sounds in an Audio File`](classifying-sounds-in-an-audio-file.md)) and add them to the stream analyzer by calling [`add(_:withObserver:)`](snaudiostreamanalyzer/add(_:withobserver:).md).

```swift
// Add a sound classification request that reports to an observer.
try streamAnalyzer.add(classifySoundRequest,
                       withObserver: resultsObserver)
```

##### Analyze the Sound Data with an Audio Tap

Access the microphone’s audio data by creating a tap to the audio engine’s input node.

```swift
func installAudioTap() {
    audioEngine.inputNode.installTap(onBus: inputBus,
                                     bufferSize: 8192,
                                     format: inputFormat,
                                     block: analyzeAudio(buffer:at:))
}
```

Keep your app responsive and the audio engine operating efficiently by running the stream analyzer on a dedicated dispatch queue. Separating the work frees the audio engine to process incoming audio data while the request analyzes the previous audio buffers.

```swift
let analysisQueue = DispatchQueue(label: "com.example.AnalysisQueue")

...

func analyzeAudio(buffer: AVAudioBuffer, at time: AVAudioTime) {
    analysisQueue.async {
        self.streamAnalyzer.analyze(buffer,
                                    atAudioFramePosition: time.sampleTime)
    }
}
```

The stream analyzer sends the results to your [`SNResultsObserving`](snresultsobserving.md) instance.

## See Also

- [Classifying Sounds in an Audio File](classifying-sounds-in-an-audio-file.md)
  Identify individual sounds in a file, such as a recording, with an audio file analyzer.
- [class SNAudioFileAnalyzer](snaudiofileanalyzer.md)
  An analyzer that runs sound classification requests on an audio file.
- [class SNAudioStreamAnalyzer](snaudiostreamanalyzer.md)
  An object you create to analyze a stream of audio data and provide the results to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/classifying-sounds-in-an-audio-stream)*