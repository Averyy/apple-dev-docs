# MaterialParameterTypes.TextureCoordinateTransform

**Framework**: RealityKit  
**Kind**: struct

An object that defines a transformation the framework applies to a material’s UV-mapped textures.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct TextureCoordinateTransform
```

#### Overview

An entity’s UV texture coordinates define how RealityKit maps image textures onto an entity. This object defines a transformation to texture coordinates that changes the way this material maps textures onto an entity. You might, for example, continuously rotate, translate, or scale the texture coordinates and animate materials to create special effects, such as fire or flowing liquids.

## Topics

### Creating a texture coordinate transform
- [init(offset: SIMD2<Float>, scale: SIMD2<Float>, rotation: Float)](materialparametertypes/texturecoordinatetransform/init(offset:scale:rotation:).md)
  Creates a texture coordinate transform object.
### Accessing the transform values
- [var offset: SIMD2<Float>](materialparametertypes/texturecoordinatetransform/offset.md)
  The amount by which the framework offsets the entity’s UV texture coordinates.
- [var scale: SIMD2<Float>](materialparametertypes/texturecoordinatetransform/scale.md)
  The amount by which the framework scale the UV texture coordinates.
- [var rotation: Float](materialparametertypes/texturecoordinatetransform/rotation.md)
  The amount by which the framework rotates the UV texture coordinates you specify in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialparametertypes/texturecoordinatetransform)*