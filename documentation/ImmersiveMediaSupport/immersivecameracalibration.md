# ImmersiveCameraCalibration

**Framework**: Immersive Media Support  
**Kind**: struct

A structure that represents immersive media camera calibration data.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImmersiveCameraCalibration
```

#### Overview

This data includes calibration type, calibration name, calibration file name, lens definition, mask data, camera origin, and other relevant data.

## Topics

### Structures
- [ImmersiveCameraCalibration.CameraOrigin](immersivecameracalibration/cameraorigin.md)
  A type that holds the position information representing the origin from which to render the calibration in 3D space relative to the user’s eye
- [ImmersiveCameraCalibration.CameraTextureMapping](immersivecameracalibration/cameratexturemapping.md)
  A type that holds the matrices used for video frame texture mapping on the camera lens geometry.
### Initializers
- [init(from: any Decoder) throws](immersivecameracalibration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(name: String, type: ImmersiveCameraCalibration.CalibrationType, mask: ImmersiveCameraMask?, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(name:type:mask:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a mesh based calibration from USDZ data and a image-based mask.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecameracalibration/encode(to:).md)
  Encodes this value into the given encoder.
### Enumerations
- [ImmersiveCameraCalibration.CalibrationType](immersivecameracalibration/calibrationtype.md)
  A value representing the calibration type used to generate camera calibration geometry.
### Instance Properties
- [var environmentFilename: String?](immersivecameracalibration/environmentfilename.md)
  The usdz file name of a backdrop that needs to be used for this calibration.
- [var mask: ImmersiveCameraMask?](immersivecameracalibration/mask.md)
  Immersive camera mask that needs to be used for this calibration.
- [var name: String](immersivecameracalibration/name.md)
  A string identifying this calibration.
- [var origin: ImmersiveCameraCalibration.CameraOrigin](immersivecameracalibration/origin.md)
  Position information that represents the origin from which to render the calibration in 3D space relative to the user’s eye.
- [var positionable: Bool](immersivecameracalibration/positionable.md)
  A Boolean value that indicates whether this calibration can be anchored in mixed reality 3D space rather than being centered on the user’s eye position or not.
- [var textureMapping: ImmersiveCameraCalibration.CameraTextureMapping](immersivecameracalibration/texturemapping.md)
  Texture mapping describing how each section of the video frame should be mapped into the calibration.
- [var type: ImmersiveCameraCalibration.CalibrationType](immersivecameracalibration/type.md)
  The type of this calibration.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [actor VenueDescriptor](venuedescriptor.md)
  The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.
- [struct ImmersiveCamera](immersivecamera.md)
  A structure that holds the required information for an immersive media camera to process and render video frames.
- [enum ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration)*