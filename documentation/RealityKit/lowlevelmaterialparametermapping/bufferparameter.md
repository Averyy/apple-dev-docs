# LowLevelMaterialParameterMapping.BufferParameter

**Framework**: RealityKit  
**Kind**: struct

A structured buffer parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BufferParameter
```

## Topics

### Accessing the buffer size
- [var size: Int](lowlevelmaterialparametermapping/bufferparameter/size.md)
  The byte size of the buffer parameter.
### Instance Properties
- [var name: String](lowlevelmaterialparametermapping/bufferparameter/name.md)
  The name of the buffer parameter as declared in the Metal shader.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var buffers: [LowLevelMaterialParameterMapping.Buffer]](lowlevelmaterialparametermapping/buffers.md)
  The ordered buffer slot descriptions for this function.
- [LowLevelMaterialParameterMapping.Buffer](lowlevelmaterialparametermapping/buffer.md)
  The contents of a buffer slot, either a collection of packed constants or a single structured buffer.
- [var textures: [LowLevelMaterialParameterMapping.TextureParameter]](lowlevelmaterialparametermapping/textures.md)
  The ordered texture slot descriptions for this function.
- [LowLevelMaterialParameterMapping.TextureParameter](lowlevelmaterialparametermapping/textureparameter.md)
  A texture parameter.
- [LowLevelMaterialParameterMapping.ConstantParameter](lowlevelmaterialparametermapping/constantparameter.md)
  A constant parameter embedded within a buffer slot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/bufferparameter)*