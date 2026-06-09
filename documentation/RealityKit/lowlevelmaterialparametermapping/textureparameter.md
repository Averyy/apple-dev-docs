# LowLevelMaterialParameterMapping.TextureParameter

**Framework**: RealityKit  
**Kind**: struct

A texture parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TextureParameter
```

## Topics

### Accessing texture parameters
- [var textureIndex: Int](lowlevelmaterialparametermapping/textureparameter/textureindex.md)
  The slot index within the argument table’s texture array.
- [var metalType: MTLTextureType](lowlevelmaterialparametermapping/textureparameter/metaltype.md)
  The expected Metal texture type.
### Instance Properties
- [var name: String](lowlevelmaterialparametermapping/textureparameter/name.md)
  The name of the texture parameter as declared in the Metal shader.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var buffers: [LowLevelMaterialParameterMapping.Buffer]](lowlevelmaterialparametermapping/buffers.md)
  The ordered buffer slot descriptions for this function.
- [LowLevelMaterialParameterMapping.Buffer](lowlevelmaterialparametermapping/buffer.md)
  The contents of a buffer slot, either a collection of packed constants or a single structured buffer.
- [LowLevelMaterialParameterMapping.BufferParameter](lowlevelmaterialparametermapping/bufferparameter.md)
  A structured buffer parameter.
- [var textures: [LowLevelMaterialParameterMapping.TextureParameter]](lowlevelmaterialparametermapping/textures.md)
  The ordered texture slot descriptions for this function.
- [LowLevelMaterialParameterMapping.ConstantParameter](lowlevelmaterialparametermapping/constantparameter.md)
  A constant parameter embedded within a buffer slot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/textureparameter)*