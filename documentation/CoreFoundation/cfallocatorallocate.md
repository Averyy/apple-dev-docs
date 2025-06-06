# CFAllocatorAllocate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Allocates memory using the specified allocator.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFAllocatorAllocate(_ allocator: CFAllocator!, _ size: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutableRawPointer!
```

#### Return Value

A pointer to the newly allocated memory.

## Parameters

- `allocator`: The allocator to use to allocate the memory. Pass   or kCFAllocatorDefault to use the current default allocator.
- `size`: The size of the memory to allocate.
- `hint`: A bitfield containing flags that suggest how memory is to be allocated.   indicates no hints. No hints are currently defined, so only   should be passed for this value.

## See Also

- [func CFAllocatorDeallocate(CFAllocator!, UnsafeMutableRawPointer!)](cfallocatordeallocate(_:_:).md)
  Deallocates a block of memory with a given allocator.
- [func CFAllocatorGetPreferredSizeForSize(CFAllocator!, CFIndex, CFOptionFlags) -> CFIndex](cfallocatorgetpreferredsizeforsize(_:_:_:).md)
  Obtains the number of bytes likely to be allocated upon a specific request.
- [func CFAllocatorReallocate(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorreallocate(_:_:_:_:).md)
  Reallocates memory using the specified allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorallocate(_:_:_:))*