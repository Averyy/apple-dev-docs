# CFAllocatorAllocateCallBack

**Framework**: Core Foundation  
**Kind**: typealias

A prototype for a function callback that allocates memory of a requested size.

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
typealias CFAllocatorAllocateCallBack = (CFIndex, CFOptionFlags, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?
```

#### Return Value

A pointer to the start of the block.

## Parameters

- `allocSize`: This function allocates a block of memory of at least   bytes (always greater than 0).
- `hint`: A bitfield that is currently not used (always set to 0).
- `info`: An untyped pointer to program-defined data. Allocate memory for the data and assign a pointer to it. This data is often control information for the allocator. It may be  .

## See Also

- [typealias CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md)
  A prototype for a function callback that provides a description of the specified data.
- [typealias CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md)
  A prototype for a function callback that deallocates a block of memory.
- [typealias CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md)
  A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [typealias CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md)
  A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [typealias CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md)
  A prototype for a function callback that releases the given data.
- [typealias CFAllocatorRetainCallBack](cfallocatorretaincallback.md)
  A prototype for a function callback that retains the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorallocatecallback)*