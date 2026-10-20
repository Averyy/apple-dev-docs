# excludesCurrentProcessAudio

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to exclude audio from your app during capture.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 13.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var excludesCurrentProcessAudio: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL excludesCurrentProcessAudio;
```

#### Discussion

The default value is [`false`](../../Swift/false.md). If you include your app process in the stream output, you can set this value to [`true`](../../Swift/true.md) to exclude its audio.

## See Also

### Configuring audio
- [var capturesAudio: Bool](./capturesaudio.md)
  A Boolean value that indicates whether to capture audio.
- [var sampleRate: Int](./samplerate.md)
  The sample rate for audio capture.
- [var channelCount: Int](./channelcount.md)
  The number of audio channels to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/excludescurrentprocessaudio)*