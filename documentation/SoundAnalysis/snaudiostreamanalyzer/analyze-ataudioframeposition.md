# analyze(_:atAudioFramePosition:)

**Framework**: Sound Analysis  
**Kind**: method

Adds a new audio buffer to the analyzer’s larger stream buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func analyze(_ audioBuffer: AVAudioBuffer, atAudioFramePosition audioFramePosition: AVAudioFramePosition)
```

#### Discussion

Serialize all calls to this method on a dedicated dispatch queue to prevent blocking the calling thread. The audio stream analyzer sends errors to each request’s results observer.

> ❗ **Important**:  Don’t call this method from a real-time audio context. However, you may call it from a lower priority thread, such as an [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine) tap or an [`AudioQueueRef`](https://developer.apple.com/documentation/AudioToolbox/AudioQueueRef) callback.

The method handles audio buffers that vary in size. If necessary, the analyzer regroups the data to a block size the underlying Core ML model expects. The analyzer uses a fixed-size audio block from some audio analysis types and may call a request’s results observer one time or many times. The factors that affect the number of calls are:

- The input buffer size
- The underlying model’s native analysis block size
- The analyzer’s current state

By default, the analyzer processes data on the first audio channel in the audio stream. The analyzer converts the sample rate of the data if it doesn’t match the underlying model’s requirements.

## Parameters

- `audioBuffer`: The audio data buffer.
- `audioFramePosition`: The frame position of the data in the buffer. The analyzer expects this parameter to monotonically increase with each call. Otherwise, the analyzer may reset its internal state to account for the jump in time.

## See Also

- [func completeAnalysis()](snaudiostreamanalyzer/completeanalysis.md)
  Notifies the analyzer when it receives the final audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiostreamanalyzer/analyze(_:ataudioframeposition:))*