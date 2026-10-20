# LowLevelMaterialParameterMapping.ConstantParameter

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A constant parameter embedded within a buffer slot.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ConstantParameter
```

## Topics

### Accessing the parameter type
- [var metalType: MTLDataType](./constantparameter/metaltype.md)
  The Metal data type of this constant.
### Instance Properties
- [var name: String](./constantparameter/name.md)
  The name of the constant as declared in the Metal shader.
- [var offset: Int](./constantparameter/offset.md)
  The byte offset of this constant within its buffer slot.

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
- [LowLevelMaterialParameterMapping.TextureParameter](./textureparameter.md)
  A texture parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/constantparameter)*