# IOBufferMemoryDescriptor

**Framework**: DriverKit  
**Kind**: class

A memory buffer allocated in the caller’s address space.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOBufferMemoryDescriptor;
```

#### Overview

Use an [`IOBufferMemoryDescriptor`](iobuffermemorydescriptor.md) to share data between your driver and other processes, including the kernel. You create memory buffers in your driver’s process space, but you can pass the buffer to any API that expects an [`IOMemoryDescriptor`](iomemorydescriptor.md) object. Some DriverKit APIs pass your buffer to another process, which can then map the buffer to its own address space and access the contents.

Typically, you create memory buffer objects to store data moving in and out of your driver. For example, a network interface driver might create a buffer to store packet data it receives from the associated device. You are responsible for managing the contents of the buffer yourself, typically by mapping it to a known data type. Except where noted, you are also responsible for releasing buffers that you allocate.

## Topics

### Creating a Memory Buffer
- [Create](iobuffermemorydescriptor/create.md)
  Creates a new memory buffer descriptor object in the current process space.
- [init](iobuffermemorydescriptor/init.md)
  Initializes the buffer memory descriptor object.
- [free](iobuffermemorydescriptor/free.md)
  Performs any final cleanup for the memory buffer descriptor object.
### Managing the Buffer Contents
- [SetLength](iobuffermemorydescriptor/setlength.md)
  Changes the length of the memory buffer.
- [GetAddressRange](iobuffermemorydescriptor/getaddressrange.md)
  Returns the address and length of the memory buffer.
- [IOAddressSegment](ioaddresssegment.md)
  A structure that describes the location and size of a block of memory.

## Relationships

### Inherits From
- [IOMemoryDescriptor](iomemorydescriptor.md)

## See Also

- [IOMemoryDescriptor](iomemorydescriptor.md)
  The base class for describing a location in memory.
- [IOMemoryMap](iomemorymap.md)
  A reference to an existing block of memory in the current process or in a different process.
- [Memory Utilities](memory-utilities.md)
  Allocate and deallocate memory and manage memory pointers in different address spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iobuffermemorydescriptor)*