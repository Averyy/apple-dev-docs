# LowLevelMaterialParameterMapping.BufferParameter

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A structured buffer parameter.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BufferParameter
```

## Topics

### Accessing the buffer size
- [var size: Int](./bufferparameter/size.md)
  The byte size of the buffer parameter.
### Instance Properties
- [var name: String](./bufferparameter/name.md)
  The name of the buffer parameter as declared in the Metal shader.

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
- [var textures: [LowLevelMaterialParameterMapping.TextureParameter]](./textures.md)
  The ordered texture slot descriptions for this function.
- [LowLevelMaterialParameterMapping.TextureParameter](./textureparameter.md)
  A texture parameter.
- [LowLevelMaterialParameterMapping.ConstantParameter](./constantparameter.md)
  A constant parameter embedded within a buffer slot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping/bufferparameter)*