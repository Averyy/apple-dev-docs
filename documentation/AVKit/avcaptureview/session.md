# session

**Framework**: AVKit  
**Kind**: property

The view’s associated capture session.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var session: AVCaptureSession? { get }
```

#### Discussion

This property’s default value is a capture session configured for movie file recordings of audio and video data. Use the [`setSession(_:showVideoPreview:showAudioPreview:)`](avcaptureview/setsession(_:showvideopreview:showaudiopreview:).md) method to provide a custom capture session. Modifying the capture session changes its visual representation in the view.

## See Also

- [func setSession(AVCaptureSession?, showVideoPreview: Bool, showAudioPreview: Bool)](avcaptureview/setsession(_:showvideopreview:showaudiopreview:).md)
  Sets the view’s capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview/session)*