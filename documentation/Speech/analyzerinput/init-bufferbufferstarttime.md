# init(buffer:bufferStartTime:)

**Framework**: Speech  
**Kind**: init

Creates an audio input object for audio that may be discontiguous with previous input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(buffer: AVAudioPCMBuffer, bufferStartTime: CMTime?)
```

#### Discussion

The audio buffer must not overlap or precede other audio input, as determined by the `bufferStartTime` value.

> ❗ **Important**: If the buffer is converted from other differently-formatted audio, ensure that the buffer’s start time is accurate. Some conversion algorithms can use a “priming” method that may shift some audio to a later converted buffer. This shift will misalign the original and converted audio buffers; the original buffer’s start time would not be usable as the `bufferStartTime` value for the converted buffer.

> 💡 **Tip**: Convert an `AVAudioTime` instance to a `CMTime` instance with this code. ```swift
CMTime(value: avAudioTime.sampleTime, timescale: CMTimeScale(avAudioTime.sampleRate))
```

## Parameters

- `buffer`: An audio buffer.
- `bufferStartTime`: The time-code of the start of the audio buffer. If  , this audio buffer is assumed to start immediately after the previous buffer (or at time-code zero if there is no previous buffer). The   can have a different timescale than the sample rate of the audio data.

## See Also

- [init(buffer: AVAudioPCMBuffer)](analyzerinput/init(buffer:).md)
  Creates an audio input object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinput/init(buffer:bufferstarttime:))*