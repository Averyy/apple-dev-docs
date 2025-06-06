# sampleRate

**Framework**: ScreenCaptureKit  
**Kind**: property

The sample rate for audio capture.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
var sampleRate: Int { get set }
```

#### Discussion

The framework supports sample rates of `8000`, `16000`, `24000`, and `48000`. If you don’t specify a sample rate, or specify an unsupported value, the system uses a default sample rate of 48 kHz.

## See Also

- [var capturesAudio: Bool](scstreamconfiguration/capturesaudio.md)
  A Boolean value that indicates whether to capture audio.
- [var channelCount: Int](scstreamconfiguration/channelcount.md)
  The number of audio channels to capture.
- [var excludesCurrentProcessAudio: Bool](scstreamconfiguration/excludescurrentprocessaudio.md)
  A Boolean value that indicates whether to exclude audio from your app during capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/samplerate)*