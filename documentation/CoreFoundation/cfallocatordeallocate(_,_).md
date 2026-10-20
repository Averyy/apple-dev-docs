# CFAllocatorDeallocate(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Deallocates a block of memory with a given allocator.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFAllocatorDeallocate(_ allocator: CFAllocator!, _ ptr: UnsafeMutableRawPointer!)
```

```c
extern void CFAllocatorDeallocate(CFAllocatorRef allocator, void *ptr);
```

#### Discussion

If the allocator does not specify a `deallocate` callback function, the memory is not deallocated.

##### Special Considerations

You must use the same allocator to deallocate memory as was used to allocate it.

## Parameters

- `allocator`: The allocator that was used to allocate the block of memory pointed to by `ptr`.
- `ptr`: An untyped pointer to a block of memory to deallocate using `allocator`.

## See Also

### Managing Memory with an Allocator
- [func CFAllocatorAllocate(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorallocate%28_,_,_%29.md)
  Allocates memory using the specified allocator.
- [func CFAllocatorGetPreferredSizeForSize(CFAllocator!, CFIndex, CFOptionFlags) -> CFIndex](./cfallocatorgetpreferredsizeforsize%28_,_,_%29.md)
  Obtains the number of bytes likely to be allocated upon a specific request.
- [func CFAllocatorReallocate(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorreallocate%28_,_,_,_%29.md)
  Reallocates memory using the specified allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatordeallocate(_:_:))*