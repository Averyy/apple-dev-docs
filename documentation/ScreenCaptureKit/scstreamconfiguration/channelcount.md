# channelCount

**Framework**: ScreenCaptureKit  
**Kind**: property

The number of audio channels to capture.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 13.0+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var channelCount: Int { get set }
```

#### Discussion

The framework supports channel counts of `1` (mono) or `2` (stereo). If you don’t specify a channel count, or specify an unsupported value, the system defaults to stereo audio capture.

## See Also

- [var capturesAudio: Bool](scstreamconfiguration/capturesaudio.md)
  A Boolean value that indicates whether to capture audio.
- [var sampleRate: Int](scstreamconfiguration/samplerate.md)
  The sample rate for audio capture.
- [var excludesCurrentProcessAudio: Bool](scstreamconfiguration/excludescurrentprocessaudio.md)
  A Boolean value that indicates whether to exclude audio from your app during capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/channelcount)*