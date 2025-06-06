# IODelete

**Framework**: DriverKit  
**Kind**: macro

Frees the memory associated with a valid, typed array.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define IODelete(ptr, type, count)
```

#### Discussion

Use this macro to free memory that you allocated with [`IONew`](ionew.md) or [`IONewZero`](ionewzero.md). It is a programmer error to pass a `NULL` pointer to this macro.

## Parameters

- `ptr`: The pointer to the memory block to free. This pointer must not be  .
- `type`: The data type stored in the memory block. The macro uses the type to determine its size.
- `count`: The number of array entries in the memory block

## See Also

- [IOSafeDeleteNULL](iosafedeletenull.md)
  Frees the memory associated with a typed array.
- [OSSafeReleaseNULL](ossafereleasenull.md)
  Frees memory that you allocated for a named class.
- [IOFree](iofree.md)
  Frees a memory block that contains general-purpose memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodelete)*