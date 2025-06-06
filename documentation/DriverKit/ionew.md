# IONew

**Framework**: DriverKit  
**Kind**: macro

Allocates memory for an array of the specified type.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define IONew(type, count)
```

#### Return Value

A pointer to the allocated memory block, or `NULL` on failure.

#### Discussion

This is a general-purpose utility to allocate memory. There are no alignment guarantees on the returned memory, and alignment may vary depending on the configuration. To allocate memory for use in I/O transfers, create an [`IOBufferMemoryDescriptor`](iobuffermemorydescriptor.md) instead.

## Parameters

- `type`: The data type to store in the block of memory. The macro uses the size of this type to determine how much memory to allocate for each array entry.
- `count`: The number of array entries to allocate.

## See Also

- [IONewZero](ionewzero.md)
  Allocates memory for an array of the specified type and zero-initializes that memory.
- [IOMalloc](iomalloc.md)
  Allocates the specified amount of general-purpose memory.
- [IOMallocZero](iomalloczero.md)
  Allocates the specified amount of general-purpose memory and zero-initializes it.
- [OSTypeAlloc](ostypealloc.md)
  Allocates memory for a named class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ionew)*