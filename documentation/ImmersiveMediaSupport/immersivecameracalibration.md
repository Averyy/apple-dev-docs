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
  Position information that represents the origin from which to render the calibration in 3D space relative to the user’s eye
- [ImmersiveCameraCalibration.CameraTextureMapping](immersivecameracalibration/cameratexturemapping.md)
  Represents the matrices used for video frame texture mapping on the camera lens geometry.
### Initializers
- [init(from: any Decoder) throws](immersivecameracalibration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(lensParameters: ImmersiveLensDefinition, mask: ImmersiveCameraMask, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(lensparameters:mask:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a parametric calibration from meiRives data and a image-based mask.
- [init(lensParameters: ImmersiveLensDefinition, maskDefinition: ImmersiveDynamicMask?, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(lensparameters:maskdefinition:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a parametric calibration from meiRives data and a dynamic mask.
- [init(usdzData: Data, mask: ImmersiveCameraMask, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(usdzdata:mask:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a mesh based calibration from USDZ data and a image-based mask.
- [init(usdzData: Data, maskDefinition: ImmersiveDynamicMask, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(usdzdata:maskdefinition:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a mesh based calibration from USDZ data and a dynamic mask.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecameracalibration/encode(to:).md)
  Encodes this value into the given encoder.
### Enumerations
- [ImmersiveCameraCalibration.CalibrationType](immersivecameracalibration/calibrationtype.md)
  An enum representing the calibration type used to generate camera calibration geometry.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [actor VenueDescriptor](venuedescriptor.md)
  The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary with every Apple Immersive Video.
- [struct ImmersiveCamera](immersivecamera.md)
  A structure that holds the required information for an immersive media camera to process and render video frames.
- [struct ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.
- [struct ImmersiveLensDefinition](immersivelensdefinition.md)
  This type holds the ILPD Meirives lens configuration parameters using which a camera calibration type instance can be generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration)*