# SCStreamOutputType.audio

**Framework**: ScreenCaptureKit  
**Kind**: case

An output type that represents an audio capture sample buffer.

**Availability**:
- Mac Catalyst 18.2+
- macOS 13.0+

## Declaration

```swift
case audio
```

#### Discussion

A captured sample buffer wraps an [`AudioBufferList`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBufferList) structure that contains the audio samples. The stream configuration’s [`sampleRate`](scstreamconfiguration/samplerate.md) and [`channelCount`](scstreamconfiguration/channelcount.md) property values determine of the format of the audio.

## See Also

- [SCStreamOutputType.screen](scstreamoutputtype/screen.md)
  An output type that represents a screen capture sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutputtype/audio)*