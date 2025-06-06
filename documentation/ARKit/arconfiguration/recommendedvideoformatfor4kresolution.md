# recommendedVideoFormatFor4KResolution

**Framework**: ARKit  
**Kind**: property

Provides a 4K video format if the device and configuration support it.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class var recommendedVideoFormatFor4KResolution: ARConfiguration.VideoFormat? { get }
```

#### Discussion

If the device and configuration support 4K, the returned video format is also present in the configuration’s [`supportedVideoFormats`](arconfiguration/supportedvideoformats.md) array.

This function returns `nil` if the device or configuration doesn’t support 4K, so you can call this function to determine whether to enable 4K for your session.

## See Also

- [var videoFormat: ARConfiguration.VideoFormat](arconfiguration/videoformat-swift.property.md)
  Video format of the session output.
- [class var supportedVideoFormats: [ARConfiguration.VideoFormat]](arconfiguration/supportedvideoformats.md)
  The set of video capture formats available on the current device.
- [ARConfiguration.VideoFormat](arconfiguration/videoformat-swift.class.md)
  A video size and frame rate specification for use with an AR session.
- [var videoHDRAllowed: Bool](arconfiguration/videohdrallowed.md)
  Enables high dynamic range (HDR) for the session’s camera feed.
- [class var configurableCaptureDeviceForPrimaryCamera: AVCaptureDevice?](arconfiguration/configurablecapturedeviceforprimarycamera.md)
  An object that enables you to alter the appearance of a frame’s captured image.
- [class var recommendedVideoFormatForHighResolutionFrameCapturing: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatforhighresolutionframecapturing.md)
  Returns a video format that the framework recommends for high-resolution-still-image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/recommendedvideoformatfor4kresolution)*