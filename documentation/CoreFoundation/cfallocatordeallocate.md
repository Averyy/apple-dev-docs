# CFAllocatorDeallocate(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Deallocates a block of memory with a given allocator.

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
func CFAllocatorDeallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutableRawPointer!)
```

#### Discussion

If the allocator does not specify a `deallocate` callback function, the memory is not deallocated.

##### Special Considerations

You must use the same allocator to deallocate memory as was used to allocate it.

## Parameters

- `allocator`: The allocator that was used to allocate the block of memory pointed to by  .
- `ptr`: An untyped pointer to a block of memory to deallocate using  .

## See Also

- [func CFAllocatorAllocate(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorallocate(_:_:_:).md)
  Allocates memory using the specified allocator.
- [func CFAllocatorGetPreferredSizeForSize(CFAllocator!, CFIndex, CFOptionFlags) -> CFIndex](cfallocatorgetpreferredsizeforsize(_:_:_:).md)
  Obtains the number of bytes likely to be allocated upon a specific request.
- [func CFAllocatorReallocate(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorreallocate(_:_:_:_:).md)
  Reallocates memory using the specified allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatordeallocate(_:_:))*