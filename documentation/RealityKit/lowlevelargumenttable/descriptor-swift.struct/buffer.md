# LowLevelArgumentTable.Descriptor.Buffer

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A buffer slot descriptor in an argument table.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Buffer
```

## Topics

### Creating a buffer descriptor
- [init(size: Int)](./buffer/init%28size%29.md)
  Creates a buffer slot descriptor with the given size.
- [var size: Int](./buffer/size.md)
  The minimum size, in bytes, that a buffer slice must have to be bound to this slot.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Specifying resources
- [var buffers: [LowLevelArgumentTable.Descriptor.Buffer]](./buffers.md)
  The ordered list of buffer slots in this table.
- [var textures: [LowLevelArgumentTable.Descriptor.Texture]](./textures.md)
  The ordered list of texture slots in this table.
- [LowLevelArgumentTable.Descriptor.Texture](./texture.md)
  A texture slot descriptor in an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/descriptor-swift.struct/buffer)*