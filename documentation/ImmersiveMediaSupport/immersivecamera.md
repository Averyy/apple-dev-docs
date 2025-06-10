# ImmersiveCamera

**Framework**: Immersive Media Support  
**Kind**: struct

A structure that holds the required information for an immersive media camera to process and render video frames.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImmersiveCamera
```

#### Overview

This type holds information including the camera identifier, type, default presentation rate, pose, and calibration data. Immersive media content can be captured with more than one camera calibrated lens, which means it’s necessary to use different geometry for each to render the corresponding video clips. AIV content creators should be able to add or remove any camera at any point during the creation and iteration process.

## Topics

### Structures
- [ImmersiveCamera.CameraPose](immersivecamera/camerapose.md)
  A struct representing the pose (position and orientation) of the immersive camera.
### Initializers
- [init(from: any Decoder) throws](immersivecamera/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(id: String, calibration: ImmersiveCameraCalibration, type: ImmersiveCamera.CameraType, presentationFrameRate: Float, pose: ImmersiveCamera.CameraPose)](immersivecamera/init(id:calibration:type:presentationframerate:pose:).md)
### Instance Properties
- [var calibration: ImmersiveCameraCalibration](immersivecamera/calibration.md)
  Calibration details for this camera.
- [var id: String](immersivecamera/id-swift.property.md)
  An identifier string for this immersive camera. Must be unique for each immersive camera and cannot be blank.
- [var pose: ImmersiveCamera.CameraPose](immersivecamera/pose.md)
  The pose of this immersive camera..
- [var presentationFrameRate: Float](immersivecamera/presentationframerate.md)
  Presentation frame rate suited for this immersive camera.
- [var type: ImmersiveCamera.CameraType](immersivecamera/type.md)
  Type of camera. Currently only the “stereoCamera” type is supported.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecamera/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [ImmersiveCamera.ID](immersivecamera/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Type Properties
- [static let defaultPresentationFrameRate: Float](immersivecamera/defaultpresentationframerate.md)
  Default presentation frame rate for any immersive camera.
### Enumerations
- [ImmersiveCamera.CameraType](immersivecamera/cameratype.md)
  Represents the type of immersive camera.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [actor VenueDescriptor](venuedescriptor.md)
  The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary with every Apple Immersive Video.
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [struct ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.
- [struct ImmersiveLensDefinition](immersivelensdefinition.md)
  This type holds the ILPD Meirives lens configuration parameters using which a camera calibration type instance can be generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecamera)*