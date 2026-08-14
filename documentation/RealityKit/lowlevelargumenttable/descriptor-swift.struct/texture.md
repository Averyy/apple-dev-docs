# LowLevelArgumentTable.Descriptor.Texture

**Framework**: RealityKit  
**Kind**: struct

A texture slot descriptor in an argument table.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Texture
```

## Topics

### Creating a texture descriptor
- [init(type: MTLTextureType)](lowlevelargumenttable/descriptor-swift.struct/texture/init(type:).md)
  Creates a texture slot descriptor with the given texture type.
### Configuring the texture type
- [var type: MTLTextureType](lowlevelargumenttable/descriptor-swift.struct/texture/type.md)
  The texture type expected at this slot.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var buffers: [LowLevelArgumentTable.Descriptor.Buffer]](lowlevelargumenttable/descriptor-swift.struct/buffers.md)
  The ordered list of buffer slots in this table.
- [LowLevelArgumentTable.Descriptor.Buffer](lowlevelargumenttable/descriptor-swift.struct/buffer.md)
  A buffer slot descriptor in an argument table.
- [var textures: [LowLevelArgumentTable.Descriptor.Texture]](lowlevelargumenttable/descriptor-swift.struct/textures.md)
  The ordered list of texture slots in this table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/descriptor-swift.struct/texture)*