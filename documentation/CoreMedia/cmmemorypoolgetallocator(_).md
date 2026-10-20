# CMMemoryPoolGetAllocator(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern CFAllocatorRefCMMemoryPoolGetAllocator(CMMemoryPoolRef pool);
```

#### Return Value

The memory pool’s allocator.

## Parameters

- `pool`: The memory pool from which to retrieve its allocator.

## See Also

### Managing a Memory Pool
- [func CMMemoryPoolFlush(CMMemoryPool)](./cmmemorypoolflush%28_%29.md)
  Deallocates all memory the pool holds.
- [func CMMemoryPoolInvalidate(CMMemoryPool)](./cmmemorypoolinvalidate%28_%29.md)
  Invalidates the memory pool, which causes its allocator to stop recycling memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmemorypoolgetallocator(_:))*