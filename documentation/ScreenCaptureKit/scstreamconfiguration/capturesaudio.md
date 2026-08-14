# capturesAudio

**Framework**: ScreenCaptureKit  
**Kind**: property

A Boolean value that indicates whether to capture audio.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 13.0+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var capturesAudio: Bool { get set }
```

#### Discussion

A stream doesn’t capture audio by default. Set this value to [`true`](https://developer.apple.com/documentation/swift/true) if you require audio capture.

## See Also

- [var sampleRate: Int](scstreamconfiguration/samplerate.md)
  The sample rate for audio capture.
- [var channelCount: Int](scstreamconfiguration/channelcount.md)
  The number of audio channels to capture.
- [var excludesCurrentProcessAudio: Bool](scstreamconfiguration/excludescurrentprocessaudio.md)
  A Boolean value that indicates whether to exclude audio from your app during capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/capturesaudio)*