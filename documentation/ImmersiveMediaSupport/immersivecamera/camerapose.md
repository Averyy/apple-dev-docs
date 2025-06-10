# ImmersiveCamera.CameraPose

**Framework**: Immersive Media Support  
**Kind**: struct

A struct representing the pose (position and orientation) of the immersive camera.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CameraPose
```

## Topics

### Initializers
- [init(from: any Decoder) throws](immersivecamera/camerapose/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(position: simd_float3, rotation: simd_float3)](immersivecamera/camerapose/init(position:rotation:).md)
  Initializes using the given camera position and camera rotation.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecamera/camerapose/encode(to:).md)
  Encodes this value into the given encoder.
### Type Properties
- [static let zero: ImmersiveCamera.CameraPose](immersivecamera/camerapose/zero.md)
  Default camera pose holding the default value of zero vector for position and zero vector for rotation of the immersive camera.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecamera/camerapose)*