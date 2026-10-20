# LowLevelMaterialParameterMapping.Buffer

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The contents of a buffer slot, either a collection of packed constants or a single structured buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Buffer
```

## Topics

### Creating a buffer mapping
- [case buffer(LowLevelMaterialParameterMapping.BufferParameter)](./buffer/buffer%28_%29.md)
  A buffer slot containing a single structured buffer.
- [case constants([LowLevelMaterialParameterMapping.ConstantParameter])](./buffer/constants%28_%29.md)
  A buffer slot containing packed constants.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing parameter mappings
- [var buffers: [LowLevelMaterialParameterMapping.Buffer]](./buffers.md)
  The ordered buffer slot descriptions for this function.
- [LowLevelMaterialParameterMapping.BufferParameter](./bufferparameter.md)
  A structured buffer parameter.
- [var textures: [LowLevelMaterialParameterMapping.TextureParameter]](./textures.md)
  The ordered texture slot descriptions for this function.
- [LowLevelMaterialParameterMapping.TextureParameter](./textureparameter.md)
  A texture parameter.
- [LowLevelMaterialParameterMapping.ConstantParameter](./constantparameter.md)
  A constant parameter embedded within a buffer slot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/buffer)*