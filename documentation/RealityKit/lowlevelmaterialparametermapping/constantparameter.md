# LowLevelMaterialParameterMapping.ConstantParameter

**Framework**: RealityKit  
**Kind**: struct

A constant parameter embedded within a buffer slot.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ConstantParameter
```

## Topics

### Accessing the parameter type
- [var metalType: MTLDataType](lowlevelmaterialparametermapping/constantparameter/metaltype.md)
  The Metal data type of this constant.
### Instance Properties
- [var name: String](lowlevelmaterialparametermapping/constantparameter/name.md)
  The name of the constant as declared in the Metal shader.
- [var offset: Int](lowlevelmaterialparametermapping/constantparameter/offset.md)
  The byte offset of this constant within its buffer slot.

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
- [LowLevelMaterialParameterMapping.TextureParameter](lowlevelmaterialparametermapping/textureparameter.md)
  A texture parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/constantparameter)*