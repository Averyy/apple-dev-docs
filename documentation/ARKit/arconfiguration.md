# ARConfiguration

**Framework**: ARKit  
**Kind**: class

The base object that contains information about how to configure an augmented reality session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARConfiguration
```

## Mentions

- [Verifying Device Support and User Permission](verifying-device-support-and-user-permission.md)

#### Overview

[`ARConfiguration`](arconfiguration.md) defines a base class for the different options you can configure in your AR experience.

All AR configurations establish a correspondence between the real world that the device inhabits and the virtual 3D-coordinate space, where you model content. When your app mixes virtual content with a live-camera image, the user experiences the illusion that your virtual content is part of the real world.

To acquire the live-camera imagery, ARKit manages a camera-capture pipeline for you. Depending on the configuration you choose, it determines the cameras that capture imagery, and which camera feed the app displays.

AR apps recognize real-world regions of interest. At runtime, ARKit generates an [`ARAnchor`](aranchor.md) for a real-world object it recognizes, which allows an app to refer to its details, such as size and physical location. The configuration you choose determines the kinds of real-world objects ARKit recognizes and makes available to your app.

Don’t allocate [`ARConfiguration`](arconfiguration.md) yourself; instead, instantiate one of its subclasses.

For more information about the camera-capture pipeline, see [`Choosing Which Camera Feed to Augment`](choosing-which-camera-feed-to-augment.md).

## Topics

### Verifying device support
- [class var isSupported: Bool](arconfiguration/issupported.md)
  A Boolean value indicating whether the current device supports this session configuration class.
### Enabling frame features
- [var frameSemantics: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.property.md)
  The set of active semantics on the frame.
- [ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct.md)
  Types of optional frame features you can enable in your app.
- [class func supportsFrameSemantics(ARConfiguration.FrameSemantics) -> Bool](arconfiguration/supportsframesemantics(_:).md)
  Checks whether a particular feature is supported.
### Configuring the AR session
- [var isLightEstimationEnabled: Bool](arconfiguration/islightestimationenabled.md)
  A Boolean value specifying whether ARKit analyzes scene lighting in captured camera images.
- [var worldAlignment: ARConfiguration.WorldAlignment](arconfiguration/worldalignment-swift.property.md)
  A value specifying how the session maps real-world device motion into a 3D scene coordinate system.
- [ARConfiguration.WorldAlignment](arconfiguration/worldalignment-swift.enum.md)
  Options for how ARKit constructs a scene coordinate system based on real-world device motion.
### Managing video capture options
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
- [class var recommendedVideoFormatFor4KResolution: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatfor4kresolution.md)
  Provides a 4K video format if the device and configuration support it.
- [class var recommendedVideoFormatForHighResolutionFrameCapturing: ARConfiguration.VideoFormat?](arconfiguration/recommendedvideoformatforhighresolutionframecapturing.md)
  Returns a video format that the framework recommends for high-resolution-still-image capture.
### Recording Audio
- [var providesAudioData: Bool](arconfiguration/providesaudiodata.md)
  A Boolean value that specifies whether to capture audio during the AR session.
### Reconstructing the Scene
- [ARConfiguration.SceneReconstruction](arconfiguration/scenereconstruction.md)
  Options that enable ARKit to detect the shape of the physical environment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ARBodyTrackingConfiguration](arbodytrackingconfiguration.md)
- [ARFaceTrackingConfiguration](arfacetrackingconfiguration.md)
- [ARGeoTrackingConfiguration](argeotrackingconfiguration.md)
- [ARImageTrackingConfiguration](arimagetrackingconfiguration.md)
- [ARObjectScanningConfiguration](arobjectscanningconfiguration.md)
- [AROrientationTrackingConfiguration](arorientationtrackingconfiguration.md)
- [ARPositionalTrackingConfiguration](arpositionaltrackingconfiguration.md)
- [ARWorldTrackingConfiguration](arworldtrackingconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration)*