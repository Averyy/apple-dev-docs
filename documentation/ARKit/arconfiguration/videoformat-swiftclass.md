# ARConfiguration.VideoFormat

**Framework**: ARKit  
**Kind**: class

A video size and frame rate specification for use with an AR session.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class VideoFormat
```

#### Overview

This class is immutable; to set the frame rate and video resolution for an AR session, set your configuration’s [`videoFormat`](arconfiguration/videoformat-swift.property.md) property to one of the formats in the [`supportedVideoFormats`](arconfiguration/supportedvideoformats.md) array.

## Topics

### Accessing format information
- [var framesPerSecond: Int](arconfiguration/videoformat-swift.class/framespersecond.md)
  The rate at which the session captures video and provides AR frame information.
- [var imageResolution: CGSize](arconfiguration/videoformat-swift.class/imageresolution.md)
  The size, in pixels, of video images captured in the session.
- [var isRecommendedForHighResolutionFrameCapturing: Bool](arconfiguration/videoformat-swift.class/isrecommendedforhighresolutionframecapturing.md)
  Determines whether the framework considers a format suitable for high-resolution frame capture.
- [var isVideoHDRSupported: Bool](arconfiguration/videoformat-swift.class/isvideohdrsupported.md)
  Determines whether the format supports high dynamic range (HDR).
### Inspecting the video source
- [var captureDevicePosition: AVCaptureDevice.Position](arconfiguration/videoformat-swift.class/capturedeviceposition.md)
  The position of the capture device.
- [enum AVCaptureDevice.Position](../avfoundation/avcapturedevice/position.md)
  Constants that indicate the physical position of a capture device.
- [var captureDeviceType: AVCaptureDevice.DeviceType](arconfiguration/videoformat-swift.class/capturedevicetype.md)
  The camera that supplies the video format.
### Instance Properties
- [var defaultColorSpace: AVCaptureColorSpace](arconfiguration/videoformat-swift.class/defaultcolorspace.md)
  The color space ARKit uses to configure the capture session when this video format is selected.
- [var defaultPhotoSettings: AVCapturePhotoSettings](arconfiguration/videoformat-swift.class/defaultphotosettings.md)
  The default AVCapturePhotoSettings object that ARKit uses when capturing a high resolution frame using this video format.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var videoFormat: ARConfiguration.VideoFormat](arconfiguration/videoformat-swift.property.md)
  Video format of the session output.
- [class var supportedVideoFormats: [ARConfiguration.VideoFormat]](arconfiguration/supportedvideoformats.md)
  The set of video capture formats available on the current device.
- [var videoHDRAllowed: Bool](arconfiguration/videohdrallowed.md)
  Enables high dynamic range (HDR) for the session’s camera feed.
- [class var configurableCaptureDeviceForPrimaryCamera: AVCaptureDevice?](arconfiguration/configurablecapturedeviceforprimarycamera.md)
  An object that enables you to alter the appearance of a frame’s captured image.
- [class var recommendedVideoFormatFor4KResolution: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatfor4kresolution.md)
  Provides a 4K video format if the device and configuration support it.
- [class var recommendedVideoFormatForHighResolutionFrameCapturing: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatforhighresolutionframecapturing.md)
  Returns a video format that the framework recommends for high-resolution-still-image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class)*