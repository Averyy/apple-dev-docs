# CMMutableDataBlockBuffer.BlockSource

**Framework**: Core Media  
**Kind**: struct

Provides ability to allocate memory for blocks using custom allocator

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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