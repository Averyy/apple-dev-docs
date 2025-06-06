# Memory Utilities

**Framework**: DriverKit

Allocate and deallocate memory and manage memory pointers in different address spaces.

## Topics

### Allocation
- [IONew](ionew.md)
  Allocates memory for an array of the specified type.
- [IONewZero](ionewzero.md)
  Allocates memory for an array of the specified type and zero-initializes that memory.
- [IOMalloc](iomalloc.md)
  Allocates the specified amount of general-purpose memory.
- [IOMallocZero](iomalloczero.md)
  Allocates the specified amount of general-purpose memory and zero-initializes it.
- [OSTypeAlloc](ostypealloc.md)
  Allocates memory for a named class.
### Deallocation
- [IODelete](iodelete.md)
  Frees the memory associated with a valid, typed array.
- [IOSafeDeleteNULL](iosafedeletenull.md)
  Frees the memory associated with a typed array.
- [OSSafeReleaseNULL](ossafereleasenull.md)
  Frees memory that you allocated for a named class.
- [IOFree](iofree.md)
  Frees a memory block that contains general-purpose memory.
### Address Utilities
- [IOVMPageSize](iovmpagesize.md)
  The number of bytes in a virtual memory page.
### Addresses
- [IOVirtualAddress](iovirtualaddress.md)
  An address in the virtual memory space of the process.
- [IOPhysicalAddress](iophysicaladdress.md)
  An address in physical memory.
- [IOPhysicalAddress32](iophysicaladdress32.md)
  A 32-bit address in physical memory.
- [IOPhysicalAddress64](iophysicaladdress64.md)
  A 64-bit address in physical memory.
- [IOPhysicalLength](iophysicallength.md)
  A type that represents the length of a memory block.
- [IOPhysicalLength32](iophysicallength32.md)
  A type that represents the length of a memory block in a 32-bit address space.
- [IOPhysicalLength64](iophysicallength64.md)
  A type that represents the length of a memory block in a 64-bit address space.
- [IOCacheMode](iocachemode.md)
  A memory-cache mode.
### Byte Counts
- [IOByteCount](iobytecount.md)
  A type that represents a number of bytes.
- [IOByteCount32](iobytecount32.md)
  A type that represents a number of bytes in a 32-bit address space.
- [IOByteCount64](iobytecount64.md)
  A type that represents a number of bytes in a 64-bit address space.

## See Also

- [IOBufferMemoryDescriptor](iobuffermemorydescriptor.md)
  A memory buffer allocated in the caller’s address space.
- [IOMemoryDescriptor](iomemorydescriptor.md)
  The base class for describing a location in memory.
- [IOMemoryMap](iomemorymap.md)
  A reference to an existing block of memory in the current process or in a different process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/memory-utilities)*