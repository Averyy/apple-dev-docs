# reallocate

**Framework**: Core Foundation  
**Kind**: property

A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.

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
var reallocate: CFAllocatorReallocateCallBack!
```

#### Discussion

When implementing this function, change the size of the block of memory pointed to by `ptr` to the size specified by `newsize` and return the pointer to the larger block of memory. Return `NULL` on any reallocation failure, leaving the old block of memory untouched. Also return `NULL` immediately if any of the following conditions apply:

The `ptr` parameter is `NULL`.

The `newsize` parameter is not greater than 0.

Leave the contents of the old block of memory unchanged up to the lesser of the new or old sizes. If the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur. The hint argument is a bitfield that you should currently not use (that is, assign 0). If you set this callback to `NULL` the `CFAllocatorReallocate(_:_:_:_:)` function returns `NULL` in most cases when it attempts to use this allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/reallocate)*