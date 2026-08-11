# LowLevelArgumentTable.Descriptor.Buffer

**Framework**: RealityKit  
**Kind**: struct

A buffer slot descriptor in an argument table.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Buffer
```

## Topics

### Creating a buffer descriptor
- [init(size: Int)](lowlevelargumenttable/descriptor-swift.struct/buffer/init(size:).md)
  Creates a buffer slot descriptor with the given size.
- [var size: Int](lowlevelargumenttable/descriptor-swift.struct/buffer/size.md)
  The minimum size, in bytes, that a buffer slice must have to be bound to this slot.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var buffers: [LowLevelArgumentTable.Descriptor.Buffer]](lowlevelargumenttable/descriptor-swift.struct/buffers.md)
  The ordered list of buffer slots in this table.
- [var textures: [LowLevelArgumentTable.Descriptor.Texture]](lowlevelargumenttable/descriptor-swift.struct/textures.md)
  The ordered list of texture slots in this table.
- [LowLevelArgumentTable.Descriptor.Texture](lowlevelargumenttable/descriptor-swift.struct/texture.md)
  A texture slot descriptor in an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/descriptor-swift.struct/buffer)*