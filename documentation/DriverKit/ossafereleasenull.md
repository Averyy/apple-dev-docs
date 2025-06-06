# OSSafeReleaseNULL

**Framework**: DriverKit  
**Kind**: macro

Frees memory that you allocated for a named class.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define OSSafeReleaseNULL(inst)
```

#### Discussion

Use this macro to free memory that you allocated [`OSTypeAlloc`](ostypealloc.md). If `inst` is `NULL`, this macro doesn’t attempt to free the memory.

## Parameters

- `inst`: The object that you want to free. After freeing the memory, the macro sets the value of   to  .

## See Also

- [IODelete](iodelete.md)
  Frees the memory associated with a valid, typed array.
- [IOSafeDeleteNULL](iosafedeletenull.md)
  Frees the memory associated with a typed array.
- [IOFree](iofree.md)
  Frees a memory block that contains general-purpose memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ossafereleasenull)*