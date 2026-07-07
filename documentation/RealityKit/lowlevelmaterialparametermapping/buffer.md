# LowLevelMaterialParameterMapping.Buffer

**Framework**: RealityKit  
**Kind**: enum

The contents of a buffer slot, either a collection of packed constants or a single structured buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Buffer
```

## Topics

### Creating a buffer mapping
- [case buffer(LowLevelMaterialParameterMapping.BufferParameter)](lowlevelmaterialparametermapping/buffer/buffer(_:).md)
  A buffer slot containing a single structured buffer.
- [case constants([LowLevelMaterialParameterMapping.ConstantParameter])](lowlevelmaterialparametermapping/buffer/constants(_:).md)
  A buffer slot containing packed constants.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var buffers: [LowLevelMaterialParameterMapping.Buffer]](lowlevelmaterialparametermapping/buffers.md)
  The ordered buffer slot descriptions for this function.
- [LowLevelMaterialParameterMapping.BufferParameter](lowlevelmaterialparametermapping/bufferparameter.md)
  A structured buffer parameter.
- [var textures: [LowLevelMaterialParameterMapping.TextureParameter]](lowlevelmaterialparametermapping/textures.md)
  The ordered texture slot descriptions for this function.
- [LowLevelMaterialParameterMapping.TextureParameter](lowlevelmaterialparametermapping/textureparameter.md)
  A texture parameter.
- [LowLevelMaterialParameterMapping.ConstantParameter](lowlevelmaterialparametermapping/constantparameter.md)
  A constant parameter embedded within a buffer slot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/buffer)*