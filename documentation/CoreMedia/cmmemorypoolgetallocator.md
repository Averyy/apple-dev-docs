# CMMemoryPoolGetAllocator(_:)

**Framework**: Core Media  
**Kind**: func

Returns the allocator for the memory pool.

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
func CMMemoryPoolGetAllocator(_ pool: CMMemoryPool) -> CFAllocator
```

#### Return Value

The memory pool’s allocator.

## Parameters

- `pool`: The memory pool from which to retrieve its allocator.

## See Also

- [func CMMemoryPoolFlush(CMMemoryPool)](cmmemorypoolflush(_:).md)
  Deallocates all memory the pool holds.
- [func CMMemoryPoolInvalidate(CMMemoryPool)](cmmemorypoolinvalidate(_:).md)
  Invalidates the memory pool, which causes its allocator to stop recycling memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmemorypoolgetallocator(_:))*