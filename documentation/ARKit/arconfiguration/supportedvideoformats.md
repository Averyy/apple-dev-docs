# supportedVideoFormats

**Framework**: ARKit  
**Kind**: property

The set of video capture formats available on the current device.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class var supportedVideoFormats: [ARConfiguration.VideoFormat] { get }
```

#### Discussion

By default, the [`videoFormat`](arconfiguration/videoformat-swift.property.md) property for a new session configuration matches the first video capture format in this array. To change the video format for a session, change that property’s value to one of the other [`ARConfiguration.VideoFormat`](arconfiguration/videoformat-swift.class.md) objects in this array.

> ❗ **Important**:  [`ARConfiguration`](arconfiguration.md) is an abstract base class, so its implementation of this property always returns an empty array. Read this property from the configuration subclass you plan to use for your AR session, such as [`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md) or [`ARFaceTrackingConfiguration`](arfacetrackingconfiguration.md).

Different devices and iOS versions offer different sets of supported video formats, but the order of this array always puts higher-quality formats before lower-quality formats. For best results across all devices and versions, choose formats based on their order in the array rather than on hard-coded minimum resolution or frame rate values.

## See Also

- [var videoFormat: ARConfiguration.VideoFormat](arconfiguration/videoformat-swift.property.md)
  Video format of the session output.
- [ARConfiguration.VideoFormat](arconfiguration/videoformat-swift.class.md)
  A video size and frame rate specification for use with an AR session.
- [var videoHDRAllowed: Bool](arconfiguration/videohdrallowed.md)
  Enables high dynamic range (HDR) for the session’s camera feed.
- [class var configurableCaptureDeviceForPrimaryCamera: AVCaptureDevice?](arconfiguration/configurablecapturedeviceforprimarycamera.md)
  An object that enables you to alter the appearance of a frame’s captured image.
- [class var recommendedVideoFormatFor4KResolution: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatfor4kresolution.md)
  Provides a 4K video format if the device and configuration support it.
- [class var recommendedVideoFormatForHighResolutionFrameCapturing: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatforhighresolutionframecapturing.md)
  Returns a video format that the framework recommends for high-resolution-still-image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/supportedvideoformats)*