# CMMutableDataBlockBuffer.MemoryPool

**Framework**: Core Media  
**Kind**: class

Optimize memory allocations when working with large block buffers.

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
final class MemoryPool
```

#### Overview

This is a memory allocation service that holds a pool of recently deallocated memory. Its purpose is to speed up subsequent allocations of the same size. You should use a pool in cases where you need to repeatedly allocate large blocks of memory, such as a video encoding app that outputs compressed data.

This object allocates memory by page. It doesn’t sub-allocate memory within pages, so don’t use it to allocate small blocks. A pool instance deallocates memory if it isn’t reused in `ageOutDuration`, so that short-term peak usage doesn’t cause persistent bloat.

## Topics

### Initializers
- [init(ageOutDuration: TimeInterval)](cmmutabledatablockbuffer/memorypool/init(ageoutduration:).md)
### Instance Methods
- [func flush()](cmmutabledatablockbuffer/memorypool/flush.md)
  Release all memory that the pool was waiting to deallocate.
- [func makeBlockBuffer(copying: UnsafePointer<AudioBufferList>) -> CMMutableDataBlockBuffer](cmmutabledatablockbuffer/memorypool/makeblockbuffer(copying:).md)
  Creates a block buffer by copying the given audio buffer list.
- [func makeBlockBuffer(count: Int) -> CMMutableDataBlockBuffer](cmmutabledatablockbuffer/memorypool/makeblockbuffer(count:).md)
  Creates a block buffer with `count` number of bytes.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/memorypool)*