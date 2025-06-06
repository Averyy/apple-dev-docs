# IOSafeDeleteNULL

**Framework**: DriverKit  
**Kind**: macro

Frees the memory associated with a typed array.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define IOSafeDeleteNULL(ptr, type, count)
```

#### Discussion

Use this macro to free memory that you allocated with [`IONew`](ionew.md) or [`IONewZero`](ionewzero.md). If `ptr` is `NULL`, this macro doesn’t attempt to free the memory.

## Parameters

- `ptr`: The pointer to the memory block to free. You may specify   for this parameter. After freeing the memory, the macro sets the value of   to  .
- `type`: The data type stored in the memory block. The macro uses the type to determine its size.
- `count`: The number of array entries in the memory block

## See Also

- [IODelete](iodelete.md)
  Frees the memory associated with a valid, typed array.
- [OSSafeReleaseNULL](ossafereleasenull.md)
  Frees memory that you allocated for a named class.
- [IOFree](iofree.md)
  Frees a memory block that contains general-purpose memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iosafedeletenull)*