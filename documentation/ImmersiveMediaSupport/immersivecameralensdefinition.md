# ImmersiveCameraLensDefinition

**Framework**: Immersive Media Support  
**Kind**: struct

This type holds the ILPD lens configuration parameters to generate camera calibration type instance.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ImmersiveCameraLensDefinition
```

#### Overview

This initializer method creates these types from ILPD data (JSON contents) reads from ILPD files. These lens definition metadata types are also used for STMap generation to transform AIV video frames of one lens projection type to another during content previews.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameralensdefinition)*