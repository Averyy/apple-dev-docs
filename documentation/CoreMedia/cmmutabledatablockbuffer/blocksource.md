# CMMutableDataBlockBuffer.BlockSource

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

Provides ability to allocate memory for blocks using custom allocator

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
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
- [init(allocate: (Int) -> UnsafeMutableRawBufferPointer, deallocate: (UnsafeMutableRawBufferPointer) -> Void)](./blocksource/init%28allocate,deallocate%29.md)
### Instance Properties
- [var allocate: (Int) -> UnsafeMutableRawBufferPointer](./blocksource/allocate.md)
- [var deallocate: (UnsafeMutableRawBufferPointer) -> Void](./blocksource/deallocate.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/blocksource)*