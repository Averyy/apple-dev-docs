# CMMemoryPoolInvalidate(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Invalidates the memory pool, which causes its allocator to stop recycling memory.

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
func CMMemoryPoolInvalidate(_ pool: CMMemoryPool)
```

```c
extern void CMMemoryPoolInvalidate(CMMemoryPoolRef pool);
```

## Parameters

- `pool`: The memory pool to invalidate.

## See Also

### Managing a Memory Pool
- [func CMMemoryPoolGetAllocator(CMMemoryPool) -> CFAllocator](./cmmemorypoolgetallocator%28_%29.md)
  Returns the allocator for the memory pool.
- [func CMMemoryPoolFlush(CMMemoryPool)](./cmmemorypoolflush%28_%29.md)
  Deallocates all memory the pool holds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmemorypoolinvalidate(_:))*