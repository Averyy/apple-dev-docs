# ImmersiveLensDefinition

**Framework**: Immersive Media Support  
**Kind**: struct

This type holds the ILPD Meirives lens configuration parameters using which a camera calibration type instance can be generated.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImmersiveLensDefinition
```

#### Overview

Initializer method creates these types from ILPD data blobs(JSON contents) read from ILPD files. These lens definition metadata types are also used for STMap generation to transform AIV video frames of one lens projection type to another during content previews.

## Topics

### Initializers
- [init(from: any Decoder) throws](immersivelensdefinition/init(from:)-825gt.md)
  Creates a new instance by decoding from the given decoder.
- [init(from: Data) throws](immersivelensdefinition/init(from:)-9kmmo.md)
  Creates an `ImmersiveLensDefinition` object from a ILPD data blob, basically the JSON contents of a ILPD file..
### Instance Properties
- [var cameraID: String](immersivelensdefinition/cameraid.md)
  The unique identifier of the Immersive Camera associated with this LensDefinition.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivelensdefinition/encode(to:).md)
  Encodes this value into the given encoder.
- [func generateSTMap(device: any MTLDevice, cameraEye: ImmersiveLensDefinition.Eye, stmapType: ImmersiveLensDefinition.STMapType, into: any MTLTexture) async throws](immersivelensdefinition/generatestmap(device:cameraeye:stmaptype:into:).md)
  Generates an STMap for the given projection type and for the given camera eye into the provided texture asynchronously.
### Enumerations
- [ImmersiveLensDefinition.Eye](immersivelensdefinition/eye.md)
- [ImmersiveLensDefinition.STMapType](immersivelensdefinition/stmaptype.md)
  An enum listing the valid values for STMap generation output when using the [`generateSTMap(device:cameraEye:stmapType:into:)`](immersivelensdefinition/generatestmap(device:cameraeye:stmaptype:into:).md) function.

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
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [struct ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivelensdefinition)*