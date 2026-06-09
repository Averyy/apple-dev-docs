# ImmersiveCameraLensDefinition

**Framework**: Immersive Media Support  
**Kind**: struct

This type holds the ILPD lens configuration parameters to generate a camera calibration type instance.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ImmersiveCameraLensDefinition
```

#### Overview

Initializer method creates these types from ILPD data blobs (JSON contents) read from ILPD files. These lens definition metadata types are also used for STMap generation to transform AIV video frames of one lens projection type to another during content previews.

## Topics

### Initializers
- [init(from: Data) throws](immersivecameralensdefinition/init(from:).md)
  Creates an `ImmersiveCameraLensDefinition` object from a ILPD data blob, basically the JSON contents of a ILPD file..
### Instance Properties
- [var cameraID: String](immersivecameralensdefinition/cameraid.md)
  The unique identifier of the immersive camera associated with this lens definition instance.
### Instance Methods
- [func generateSTMap(device: any MTLDevice, cameraEye: ImmersiveCameraLensDefinition.Eye, stmapType: ImmersiveCameraLensDefinition.STMapType, into: any MTLTexture) async throws](immersivecameralensdefinition/generatestmap(device:cameraeye:stmaptype:into:).md)
  Generates an STMap for the given projection type and for the given camera eye into the provided texture asynchronously.
### Enumerations
- [ImmersiveCameraLensDefinition.Eye](immersivecameralensdefinition/eye.md)
  A value that represents a camera lens eye.
- [ImmersiveCameraLensDefinition.STMapType](immersivecameralensdefinition/stmaptype.md)
  A value that represents a camera lens projection type.

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
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [enum ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.
- [class ImmersiveImageMask](immersiveimagemask.md)
  An object that holds all the information needed to load immersive media masks from image data or from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameralensdefinition)*