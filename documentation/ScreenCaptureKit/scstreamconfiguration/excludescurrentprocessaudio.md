# excludesCurrentProcessAudio

**Framework**: ScreenCaptureKit  
**Kind**: property

A Boolean value that indicates whether to exclude audio from your app during capture.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
var excludesCurrentProcessAudio: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). If you include your app process in the stream output, you can set this value to [`true`](https://developer.apple.com/documentation/swift/true) to exclude its audio.

## See Also

- [var capturesAudio: Bool](scstreamconfiguration/capturesaudio.md)
  A Boolean value that indicates whether to capture audio.
- [var sampleRate: Int](scstreamconfiguration/samplerate.md)
  The sample rate for audio capture.
- [var channelCount: Int](scstreamconfiguration/channelcount.md)
  The number of audio channels to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/excludescurrentprocessaudio)*