# IOMemoryDescriptor

**Framework**: DriverKit  
**Kind**: class

The base class for describing a location in memory.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOMemoryDescriptor;
```

#### Overview

The [`IOMemoryDescriptor`](iomemorydescriptor.md) class defines shared behavior for memory-related objects. Use the methods of this class to get information about a memory block and to map a memory block from another process into your driver’s memory space.

Don’t create instances of this class directly. When you want to allocate memory for your driver, create an [`IOBufferMemoryDescriptor`](iobuffermemorydescriptor.md) instead, which is a concrete implementation of this class.

## Topics

### Configuring the Buffer
- [init](iomemorydescriptor/init.md)
  Initializes the memory descriptor object.
- [free](iomemorydescriptor/free.md)
  Performs any final cleanup for the memory descriptor object.
### Getting the Buffer Length
- [GetLength](iomemorydescriptor/getlength.md)
  Returns the length of the memory block represented by this object.
### Mapping to the Caller’s Address Space
- [CreateMapping](iomemorydescriptor/createmapping.md)
  Maps the contents of the memory block to the address space of the current process.
- [Memory Map Options](3325558-memory_map_options.md)
  Options that describe how to configure a memory-mapped buffer.
### Performing Internal Tasks
- [Map](iomemorydescriptor/map.md)
  Maps memory internally.
### Type Methods
- [CreateSubMemoryDescriptor](iomemorydescriptor/createsubmemorydescriptor.md)
- [CreateWithMemoryDescriptors](iomemorydescriptor/createwithmemorydescriptors.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)
### Inherited By
- [IOBufferMemoryDescriptor](iobuffermemorydescriptor.md)

## See Also

- [IOBufferMemoryDescriptor](iobuffermemorydescriptor.md)
  A memory buffer allocated in the caller’s address space.
- [IOMemoryMap](iomemorymap.md)
  A reference to an existing block of memory in the current process or in a different process.
- [Memory Utilities](memory-utilities.md)
  Allocate and deallocate memory and manage memory pointers in different address spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor)*