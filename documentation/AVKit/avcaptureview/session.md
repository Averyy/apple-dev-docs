# session

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The view’s associated capture session.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var session: AVCaptureSession? { get }
```

```objc
@property (readonly, nullable) AVCaptureSession * session;
```

#### Discussion

This property’s default value is a capture session configured for movie file recordings of audio and video data. Use the [`setSession(_:showVideoPreview:showAudioPreview:)`](./setsession%28_,showvideopreview,showaudiopreview%29.md) method to provide a custom capture session. Modifying the capture session changes its visual representation in the view.

## See Also

### Configuring the capture session
- [func setSession(AVCaptureSession?, showVideoPreview: Bool, showAudioPreview: Bool)](./setsession%28_,showvideopreview,showaudiopreview%29.md)
  Sets the view’s capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview/session)*