# videoFormat

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Video format of the session output.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
var videoFormat: ARConfiguration.VideoFormat { get set }
```

```objc
@property (nonatomic, strong) ARVideoFormat * videoFormat;
```

## See Also

### Managing video capture options
- [class var supportedVideoFormats: [ARConfiguration.VideoFormat]](./supportedvideoformats.md)
  The set of video capture formats available on the current device.
- [ARConfiguration.VideoFormat](./videoformat-swift.class.md)
  A video size and frame rate specification for use with an AR session.
- [var videoHDRAllowed: Bool](./videohdrallowed.md)
  Enables high dynamic range (HDR) for the session’s camera feed.
- [class var configurableCaptureDeviceForPrimaryCamera: AVCaptureDevice?](./configurablecapturedeviceforprimarycamera.md)
  An object that enables you to alter the appearance of a frame’s captured image.
- [class var recommendedVideoFormatFor4KResolution: ARConfiguration.VideoFormat?](./recommendedvideoformatfor4kresolution.md)
  Provides a 4K video format if the device and configuration support it.
- [class var recommendedVideoFormatForHighResolutionFrameCapturing: ARConfiguration.VideoFormat?](./recommendedvideoformatforhighresolutionframecapturing.md)
  Returns a video format that the framework recommends for high-resolution-still-image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.property)*