# CFAllocatorPreferredSizeCallBack

**Framework**: Core Foundation  
**Kind**: typealias

A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.

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
typealias CFAllocatorPreferredSizeCallBack = (CFIndex, CFOptionFlags, UnsafeMutableRawPointer?) -> CFIndex
```

#### Return Value

The actual size the allocator is likely to allocate given this request.

#### Discussion

A prototype for a function callback that determines whether there is enough free memory to satisfy a request. In implementing this function, return the actual size the allocator is likely to allocate given a request for a block of memory of size `size`. The `hint` argument is a bitfield that you should currently not use.

## Parameters

- `size`: The amount of memory requested.
- `hint`: A bitfield that is currently not used (always set to 0).
- `info`: An untyped pointer to program-defined data.

## See Also

- [typealias CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md)
  A prototype for a function callback that allocates memory of a requested size.
- [typealias CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md)
  A prototype for a function callback that provides a description of the specified data.
- [typealias CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md)
  A prototype for a function callback that deallocates a block of memory.
- [typealias CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md)
  A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [typealias CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md)
  A prototype for a function callback that releases the given data.
- [typealias CFAllocatorRetainCallBack](cfallocatorretaincallback.md)
  A prototype for a function callback that retains the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorpreferredsizecallback)*