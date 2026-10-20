# LowLevelMaterialParameterMapping.TextureParameter

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A texture parameter.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TextureParameter
```

## Topics

### Accessing texture parameters
- [var textureIndex: Int](./textureparameter/textureindex.md)
  The slot index within the argument table’s texture array.
- [var metalType: MTLTextureType](./textureparameter/metaltype.md)
  The expected Metal texture type.
### Instance Properties
- [var name: String](./textureparameter/name.md)
  The name of the texture parameter as declared in the Metal shader.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing parameter mappings
- [var buffers: [LowLevelMaterialParameterMapping.Buffer]](./buffers.md)
  The ordered buffer slot descriptions for this function.
- [LowLevelMaterialParameterMapping.Buffer](./buffer.md)
  The contents of a buffer slot, either a collection of packed constants or a single structured buffer.
- [LowLevelMaterialParameterMapping.BufferParameter](./bufferparameter.md)
  A structured buffer parameter.
- [var textures: [LowLevelMaterialParameterMapping.TextureParameter]](./textures.md)
  The ordered texture slot descriptions for this function.
- [LowLevelMaterialParameterMapping.ConstantParameter](./constantparameter.md)
  A constant parameter embedded within a buffer slot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/textureparameter)*