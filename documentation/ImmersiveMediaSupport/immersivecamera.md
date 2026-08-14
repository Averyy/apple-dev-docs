# ImmersiveCamera

**Framework**: Immersive Media Support  
**Kind**: struct

A structure that holds the required information for an immersive media camera to process and render video frames.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ImmersiveCamera
```

#### Overview

This type holds information including the camera identifier, type, default presentation rate, pose, and calibration data. Immersive media content can be captured with more than one camera calibrated lens, which means it’s necessary to use different geometry for each to render the corresponding video clips. AIV content creators should be able to add or remove any camera at any point during the creation and iteration process.

## Topics

### Initializers
- [init(id: String, calibration: ImmersiveCameraCalibration, type: ImmersiveCamera.CameraType, presentationFrameRate: Int, pose: Pose3DFloat)](immersivecamera/init(id:calibration:type:presentationframerate:pose:).md)
### Instance Properties
- [var calibration: ImmersiveCameraCalibration](immersivecamera/calibration.md)
  Calibration details for this camera.
- [var id: String](immersivecamera/id.md)
  A unique and non empty identifier string for this immersive camera.
- [var pose: Pose3DFloat](immersivecamera/pose.md)
  The pose of this immersive camera.
- [var presentationFrameRate: Int](immersivecamera/presentationframerate.md)
  Presentation frame rate suited for this immersive camera.
- [var type: ImmersiveCamera.CameraType](immersivecamera/type.md)
  Represents the type of the camera.
### Type Properties
- [static let defaultPresentationFrameRate: Int](immersivecamera/defaultpresentationframerate.md)
  Default presentation frame rate for any immersive camera.
### Enumerations
- [ImmersiveCamera.CameraType](immersivecamera/cameratype.md)
  A value that represents the type of immersive camera.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [actor VenueDescriptor](venuedescriptor.md)
  The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.
- [struct ImmersiveCameraLensDefinition](immersivecameralensdefinition.md)
  This type holds the ILPD lens configuration parameters to generate a camera calibration type instance.
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [enum ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.
- [class ImmersiveImageMask](immersiveimagemask.md)
  An object that holds all the information needed to load immersive media masks from image data or from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecamera)*