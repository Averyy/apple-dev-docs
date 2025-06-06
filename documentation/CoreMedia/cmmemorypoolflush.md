# CMMemoryPoolFlush(_:)

**Framework**: Core Media  
**Kind**: func

Deallocates all memory the pool holds.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMMemoryPoolFlush(_ pool: CMMemoryPool)
```

## Parameters

- `pool`: The memory pool to flush.

## See Also

- [func CMMemoryPoolGetAllocator(CMMemoryPool) -> CFAllocator](cmmemorypoolgetallocator(_:).md)
  Returns the allocator for the memory pool.
- [func CMMemoryPoolInvalidate(CMMemoryPool)](cmmemorypoolinvalidate(_:).md)
  Invalidates the memory pool, which causes its allocator to stop recycling memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmemorypoolflush(_:))*