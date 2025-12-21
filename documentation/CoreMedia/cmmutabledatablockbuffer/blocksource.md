# CMMutableDataBlockBuffer.BlockSource

**Framework**: Core Media  
**Kind**: struct

Provides ability to allocate memory for blocks using custom allocator

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct BlockSource
```

## Topics

### Initializers
- [init(allocate: (Int) -> UnsafeMutableRawBufferPointer, deallocate: (UnsafeMutableRawBufferPointer) -> Void)](cmmutabledatablockbuffer/blocksource/init(allocate:deallocate:).md)
### Instance Properties
- [var allocate: (Int) -> UnsafeMutableRawBufferPointer](cmmutabledatablockbuffer/blocksource/allocate.md)
- [var deallocate: (UnsafeMutableRawBufferPointer) -> Void](cmmutabledatablockbuffer/blocksource/deallocate.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/blocksource)*