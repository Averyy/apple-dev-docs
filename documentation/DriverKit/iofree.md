# IOFree

**Framework**: DriverKit  
**Kind**: func

Frees a memory block that contains general-purpose memory.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void IOFree(void * address, size_t length);
```

#### Discussion

Use this macro to free memory that you allocated with [`IOMalloc`](iomalloc.md) or [`IOMallocZero`](iomalloczero.md).

## Parameters

- `address`: The pointer to the memory block to free. The memory block must be one that you previously allocated with   or  .
- `length`: The size of the memory block, which must match the block’s original allocation size.

## See Also

- [IODelete](iodelete.md)
  Frees the memory associated with a valid, typed array.
- [IOSafeDeleteNULL](iosafedeletenull.md)
  Frees the memory associated with a typed array.
- [OSSafeReleaseNULL](ossafereleasenull.md)
  Frees memory that you allocated for a named class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iofree)*