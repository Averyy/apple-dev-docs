# CFAllocatorDeallocateCallBack

**Framework**: Core Foundation  
**Kind**: typealias

A prototype for a function callback that deallocates a block of memory.

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
typealias CFAllocatorDeallocateCallBack = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

A prototype for a function callback that deallocates a given block of memory. In implementing this function, make the block of memory pointed to by `ptr` available for subsequent reuse by the allocator but unavailable for continued use by the program. The `ptr` parameter cannot be NULL and if the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur.

## Parameters

- `ptr`: The block of memory to deallocate.
- `info`: An untyped pointer to program-defined data.

## See Also

- [typealias CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md)
  A prototype for a function callback that allocates memory of a requested size.
- [typealias CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md)
  A prototype for a function callback that provides a description of the specified data.
- [typealias CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md)
  A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [typealias CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md)
  A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [typealias CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md)
  A prototype for a function callback that releases the given data.
- [typealias CFAllocatorRetainCallBack](cfallocatorretaincallback.md)
  A prototype for a function callback that retains the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatordeallocatecallback)*