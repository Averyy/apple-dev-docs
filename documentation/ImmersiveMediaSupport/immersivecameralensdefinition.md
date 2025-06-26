# ImmersiveCameraLensDefinition

**Framework**: Immersive Media Support  
**Kind**: struct

This type holds the ILPD Meirives lens configuration parameters using which a camera calibration type instance can be generated.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImmersiveCameraLensDefinition
```

#### Overview

Initializer method creates these types from ILPD data blobs(JSON contents) read from ILPD files. These lens definition metadata types are also used for STMap generation to transform AIV video frames of one lens projection type to another during content previews.

## Topics

### Initializers
- [init(from: Data) throws](immersivecameralensdefinition/init(from:)-4ivvl.md)
  Creates an `ImmersiveCameraLensDefinition` object from a ILPD data blob, basically the JSON contents of a ILPD file..
- [init(from: any Decoder) throws](immersivecameralensdefinition/init(from:)-4kenq.md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var cameraID: String](immersivecameralensdefinition/cameraid.md)
  The unique identifier of the immersive camera associated with this lens definition instance.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecameralensdefinition/encode(to:).md)
  Encodes this value into the given encoder.
- [func generateSTMap(device: any MTLDevice, cameraEye: ImmersiveCameraLensDefinition.Eye, stmapType: ImmersiveCameraLensDefinition.STMapType, into: any MTLTexture) async throws](immersivecameralensdefinition/generatestmap(device:cameraeye:stmaptype:into:).md)
  Generates an STMap for the given projection type and for the given camera eye into the provided texture asynchronously.
### Enumerations
- [ImmersiveCameraLensDefinition.Eye](immersivecameralensdefinition/eye.md)
  A value representing a camera lens eye.
- [ImmersiveCameraLensDefinition.STMapType](immersivecameralensdefinition/stmaptype.md)
  A value representing a camera lens projection type.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameralensdefinition)*