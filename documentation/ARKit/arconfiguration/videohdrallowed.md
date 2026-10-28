# videoHDRAllowed

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Enables high dynamic range (HDR) for the session’s camera feed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
var videoHDRAllowed: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL videoHDRAllowed;
```

## Discussion

Before calling this function, check whether the session configuration’s video format supports HDR first by calling [`isVideoHDRSupported`](./videoformat-swift.class/isvideohdrsupported.md).

## See Also

### Managing video capture options
- [var videoFormat: ARConfiguration.VideoFormat](./videoformat-swift.property.md)
  Video format of the session output.
- [class var supportedVideoFormats: [ARConfiguration.VideoFormat]](./supportedvideoformats.md)
  The set of video capture formats available on the current device.
- [ARConfiguration.VideoFormat](./videoformat-swift.class.md)
  A video size and frame rate specification for use with an AR session.
- [class var configurableCaptureDeviceForPrimaryCamera: AVCaptureDevice?](./configurablecapturedeviceforprimarycamera.md)
  An object that enables you to alter the appearance of a frame’s captured image.
- [class var recommendedVideoFormatFor4KResolution: ARConfiguration.VideoFormat?](./recommendedvideoformatfor4kresolution.md)
  Provides a 4K video format if the device and configuration support it.
- [class var recommendedVideoFormatForHighResolutionFrameCapturing: ARConfiguration.VideoFormat?](./recommendedvideoformatforhighresolutionframecapturing.md)
  Returns a video format that the framework recommends for high-resolution-still-image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videohdrallowed)*