# IOMemoryMap

**Framework**: DriverKit  
**Kind**: class

A reference to an existing block of memory in the current process or in a different process.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOMemoryMap;
```

#### Overview

Use an [`IOMemoryMap`](iomemorymap.md) object to share an existing block of memory. You don’t create instances of this class directly. Instead, call the [`CreateMapping`](iomemorydescriptor/createmapping.md) method of [`IOMemoryDescriptor`](iomemorydescriptor.md) to create a new memory map object for that descriptor’s contents. Use the methods of this class to get the address and size of the memory block, relative to the current process.

An [`IOMemoryMap`](iomemorymap.md) object doesn’t own the memory it references, and you must not attempt to free that memory.

## Topics

### Configuring the Memory Map
- [init](iomemorymap/init.md)
  Initializes the memory map object.
- [free](iomemorymap/free.md)
  Performs any final cleanup for the memory map object.
### Getting the Map Attributes
- [GetAddress](iomemorymap/getaddress.md)
  Returns the address of the memory block.
- [GetLength](iomemorymap/getlength.md)
  Returns the length of the memory block in bytes.
- [GetOffset](iomemorymap/getoffset.md)
  Returns the offset from the original start of the memory block.

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOBufferMemoryDescriptor](iobuffermemorydescriptor.md)
  A memory buffer allocated in the caller’s address space.
- [IOMemoryDescriptor](iomemorydescriptor.md)
  The base class for describing a location in memory.
- [Memory Utilities](memory-utilities.md)
  Allocate and deallocate memory and manage memory pointers in different address spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorymap)*