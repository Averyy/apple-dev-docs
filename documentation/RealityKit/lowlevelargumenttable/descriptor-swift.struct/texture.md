# LowLevelArgumentTable.Descriptor.Texture

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A texture slot descriptor in an argument table.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Texture
```

## Topics

### Creating a texture descriptor
- [init(type: MTLTextureType)](./texture/init%28type%29.md)
  Creates a texture slot descriptor with the given texture type.
### Configuring the texture type
- [var type: MTLTextureType](./texture/type.md)
  The texture type expected at this slot.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Specifying resources
- [var buffers: [LowLevelArgumentTable.Descriptor.Buffer]](./buffers.md)
  The ordered list of buffer slots in this table.
- [LowLevelArgumentTable.Descriptor.Buffer](./buffer.md)
  A buffer slot descriptor in an argument table.
- [var textures: [LowLevelArgumentTable.Descriptor.Texture]](./textures.md)
  The ordered list of texture slots in this table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/descriptor-swift.struct/texture)*