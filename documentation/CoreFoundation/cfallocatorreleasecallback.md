# CFAllocatorReleaseCallBack

**Framework**: Core Foundation  
**Kind**: typealias

A prototype for a function callback that releases the given data.

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
typealias CFAllocatorReleaseCallBack = (UnsafeRawPointer?) -> Void
```

#### Discussion

A prototype for a function callback that releases the data pointed to by the `info` field. In implementing this function, release (or free) the data you have defined for the allocator context.

## Parameters

- `info`: The data to be released.

## See Also

- [typealias CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md)
  A prototype for a function callback that allocates memory of a requested size.
- [typealias CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md)
  A prototype for a function callback that provides a description of the specified data.
- [typealias CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md)
  A prototype for a function callback that deallocates a block of memory.
- [typealias CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md)
  A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [typealias CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md)
  A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [typealias CFAllocatorRetainCallBack](cfallocatorretaincallback.md)
  A prototype for a function callback that retains the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorreleasecallback)*