# configurableCaptureDeviceForPrimaryCamera

**Framework**: ARKit  
**Kind**: property

An object that enables you to alter the appearance of a frame’s captured image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class var configurableCaptureDeviceForPrimaryCamera: AVCaptureDevice? { get }
```

#### Discussion

This property provides the underlying capture device for the framework’s camera feed. By altering the device’s configuration, your app indirectly adjusts the visual properties of the each AR frame’s [`capturedImage`](arframe/capturedimage.md).

Alter the device’s settings with caution, as extreme changes can affect ARKit’s features that rely on the [`capturedImage`](arframe/capturedimage.md) and depend on its integrity, such as people occlusion that uses [`personSegmentation`](arconfiguration/framesemantics-swift.struct/personsegmentation.md).

> ❗ **Important**:  This property is `nil` on devices that aren’t equiped with an ultra-wide camera.

 This property is `nil` on devices that aren’t equiped with an ultra-wide camera.

## See Also

- [var videoFormat: ARConfiguration.VideoFormat](arconfiguration/videoformat-swift.property.md)
  Video format of the session output.
- [class var supportedVideoFormats: [ARConfiguration.VideoFormat]](arconfiguration/supportedvideoformats.md)
  The set of video capture formats available on the current device.
- [ARConfiguration.VideoFormat](arconfiguration/videoformat-swift.class.md)
  A video size and frame rate specification for use with an AR session.
- [var videoHDRAllowed: Bool](arconfiguration/videohdrallowed.md)
  Enables high dynamic range (HDR) for the session’s camera feed.
- [class var recommendedVideoFormatFor4KResolution: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatfor4kresolution.md)
  Provides a 4K video format if the device and configuration support it.
- [class var recommendedVideoFormatForHighResolutionFrameCapturing: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatforhighresolutionframecapturing.md)
  Returns a video format that the framework recommends for high-resolution-still-image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/configurablecapturedeviceforprimarycamera)*