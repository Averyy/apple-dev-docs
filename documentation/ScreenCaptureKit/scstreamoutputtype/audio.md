# SCStreamOutputType.audio

**Framework**: ScreenCaptureKit  
**Kind**: case  
**Role**: Case

An output type that represents an audio capture sample buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 13.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case audio
```

```c
SCStreamOutputTypeAudio
```

#### Discussion

A captured sample buffer wraps an [`AudioBufferList`](../../CoreAudioTypes/audiobufferlist.md) structure that contains the audio samples. The stream configuration’s [`sampleRate`](../scstreamconfiguration/samplerate.md) and [`channelCount`](../scstreamconfiguration/channelcount.md) property values determine of the format of the audio.

## See Also

### Output types
- [SCStreamOutputType.screen](./screen.md)
  An output type that represents a screen capture sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutputtype/audio)*