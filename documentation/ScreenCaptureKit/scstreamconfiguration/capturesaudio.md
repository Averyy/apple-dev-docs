# capturesAudio

**Framework**: ScreenCaptureKit  
**Kind**: property

A Boolean value that indicates whether to capture audio.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
var capturesAudio: Bool { get set }
```

#### Discussion

A stream doesn’t capture audio by default. Set this value to [`true`](https://developer.apple.com/documentation/Swift/true) if you require audio capture.

## See Also

- [var sampleRate: Int](scstreamconfiguration/samplerate.md)
  The sample rate for audio capture.
- [var channelCount: Int](scstreamconfiguration/channelcount.md)
  The number of audio channels to capture.
- [var excludesCurrentProcessAudio: Bool](scstreamconfiguration/excludescurrentprocessaudio.md)
  A Boolean value that indicates whether to exclude audio from your app during capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/capturesaudio)*