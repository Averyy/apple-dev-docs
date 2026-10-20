# recommendedVideoFormatFor4KResolution

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

Provides a 4K video format if the device and configuration support it.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
class var recommendedVideoFormatFor4KResolution: ARConfiguration.VideoFormat? { get }
```

```objc
@property (class, nonatomic, readonly, nullable) ARVideoFormat * recommendedVideoFormatFor4KResolution;
```

#### Discussion

If the device and configuration support 4K, the returned video format is also present in the configuration’s [`supportedVideoFormats`](./supportedvideoformats.md) array.

This function returns `nil` if the device or configuration doesn’t support 4K, so you can call this function to determine whether to enable 4K for your session.

## See Also

### Managing video capture options
- [var videoFormat: ARConfiguration.VideoFormat](./videoformat-swift.property.md)
  Video format of the session output.
- [class var supportedVideoFormats: [ARConfiguration.VideoFormat]](./supportedvideoformats.md)
  The set of video capture formats available on the current device.
- [ARConfiguration.VideoFormat](./videoformat-swift.class.md)
  A video size and frame rate specification for use with an AR session.
- [var videoHDRAllowed: Bool](./videohdrallowed.md)
  Enables high dynamic range (HDR) for the session’s camera feed.
- [class var configurableCaptureDeviceForPrimaryCamera: AVCaptureDevice?](./configurablecapturedeviceforprimarycamera.md)
  An object that enables you to alter the appearance of a frame’s captured image.
- [class var recommendedVideoFormatForHighResolutionFrameCapturing: ARConfiguration.VideoFormat?](./recommendedvideoformatforhighresolutionframecapturing.md)
  Returns a video format that the framework recommends for high-resolution-still-image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/recommendedvideoformatfor4kresolution)*