# capturesAudio

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to capture audio.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 13.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var capturesAudio: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL capturesAudio;
```

#### Discussion

A stream doesn’t capture audio by default. Set this value to [`true`](../../Swift/true.md) if you require audio capture.

## See Also

### Configuring audio
- [var sampleRate: Int](./samplerate.md)
  The sample rate for audio capture.
- [var channelCount: Int](./channelcount.md)
  The number of audio channels to capture.
- [var excludesCurrentProcessAudio: Bool](./excludescurrentprocessaudio.md)
  A Boolean value that indicates whether to exclude audio from your app during capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/capturesaudio)*