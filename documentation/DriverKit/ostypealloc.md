# OSTypeAlloc

**Framework**: DriverKit  
**Kind**: macro

Allocates memory for a named class.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define OSTypeAlloc(type)
```

#### Return Value

A pointer to the allocated memory block, or `NULL` on failure.

#### Discussion

This is a general-purpose utility to allocate memory for DriverKit objects. Consider using object-specific creation methods instead. To allocate memory for use in I/O transfers, create an [`IOBufferMemoryDescriptor`](iobuffermemorydescriptor.md) instead.

## Parameters

- `type`: The name of the desired class as a raw token, not as a string or macro.

## See Also

- [IONew](ionew.md)
  Allocates memory for an array of the specified type.
- [IONewZero](ionewzero.md)
  Allocates memory for an array of the specified type and zero-initializes that memory.
- [IOMalloc](iomalloc.md)
  Allocates the specified amount of general-purpose memory.
- [IOMallocZero](iomalloczero.md)
  Allocates the specified amount of general-purpose memory and zero-initializes it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ostypealloc)*