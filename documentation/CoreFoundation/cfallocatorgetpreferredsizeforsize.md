# CFAllocatorGetPreferredSizeForSize(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Obtains the number of bytes likely to be allocated upon a specific request.

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
func CFAllocatorGetPreferredSizeForSize(_ allocator: CFAllocator!, _ size: CFIndex, _ hint: CFOptionFlags) -> CFIndex
```

#### Return Value

The number of bytes likely to be allocated upon a specific request.

#### Discussion

The return value depends on the allocator’s internal allocation strategy, and will be equal to or larger than `size`. Calling this function may help you better match your memory allocation or reallocation strategy to that of the allocator.

Note that the return value depends on the internal implementation of the allocator and the results may change from release to release or from platform to platform.

If no function callback is assigned to the `preferredSize` field of the allocator’s context (see the `CFAllocatorContext` structure), then the value of `size` is returned.

## Parameters

- `allocator`: The allocator to use, or   for the default allocator.
- `size`: The number of bytes to allocate. If the value is   or less, the result is the same value.
- `hint`: A bitfield of type  . Pass flags to the allocator that suggest how memory is to be allocated.   indicates no hints. No hints are currently defined, only   should be passed for this argument.

## See Also

- [func CFAllocatorAllocate(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorallocate(_:_:_:).md)
  Allocates memory using the specified allocator.
- [func CFAllocatorDeallocate(CFAllocator!, UnsafeMutableRawPointer!)](cfallocatordeallocate(_:_:).md)
  Deallocates a block of memory with a given allocator.
- [func CFAllocatorReallocate(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorreallocate(_:_:_:_:).md)
  Reallocates memory using the specified allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorgetpreferredsizeforsize(_:_:_:))*