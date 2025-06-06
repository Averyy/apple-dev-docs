# IOMalloc

**Framework**: DriverKit  
**Kind**: func

Allocates the specified amount of general-purpose memory.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void * IOMalloc(size_t length);
```

#### Return Value

A pointer to the allocated memory block, or `NULL` on failure.

#### Discussion

This is a general-purpose utility to allocate memory. There are no alignment guarantees on the returned memory, and alignment may vary depending on the configuration. To allocate memory for use in I/O transfers, create an [`IOBufferMemoryDescriptor`](iobuffermemorydescriptor.md) instead.

## Parameters

- `length`: The number of bytes to allocate.

## See Also

- [IONew](ionew.md)
  Allocates memory for an array of the specified type.
- [IONewZero](ionewzero.md)
  Allocates memory for an array of the specified type and zero-initializes that memory.
- [IOMallocZero](iomalloczero.md)
  Allocates the specified amount of general-purpose memory and zero-initializes it.
- [OSTypeAlloc](ostypealloc.md)
  Allocates memory for a named class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomalloc)*