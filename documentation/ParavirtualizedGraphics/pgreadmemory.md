# PGReadMemory

**Framework**: Paravirtualized Graphics  
**Kind**: typealias  
**Role**: Type Alias

The block signature for a routine that copies data from guest physical memory into host memory.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```c
typedef _Bool (^)(unsigned long long, unsigned long long, void *) PGReadMemory;
```

## Return Value

Returns [`true`](../Swift/true.md) if the block copied the data successfully; otherwise [`false`](../Swift/false.md).

## Parameters

- `physicalAddress`: The physical guest address of the data to read.
- `length`: The number of bytes to read.
- `dst`: The destination for the copied data.

## See Also

### Managing Memory Operations
- [mapMemory](./pgdevicedescriptor/mapmemory.md)
  A handler that the framework calls to map memory into the virtual machine.
- [unmapMemory](./pgdevicedescriptor/unmapmemory.md)
  A handler that the framework calls to unmap memory from the virtual machine.
- [readMemory](./pgdevicedescriptor/readmemory.md)
  A handler that the framework calls to read data from the guest’s memory.
- [PGMapMemory](./pgmapmemory.md)
  The block signature for a routine that maps guest physical memory into a task.
- [PGUnmapMemory](./pgunmapmemory.md)
  The block signature for a routine that unmaps guest physical memory from a task.
- [struct PGPhysicalMemoryRange_s](./pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgreadmemory)*