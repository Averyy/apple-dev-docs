# PGMapMemory

**Framework**: Paravirtualized Graphics  
**Kind**: typealias  
**Role**: Type Alias

The block signature for a routine that maps guest physical memory into a task.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```c
typedef _Bool (^)(struct PGTask_s *, unsigned int, unsigned long long, _Bool, struct PGPhysicalMemoryRange_s *) PGMapMemory;
```

## Return Value

Returns [`true`](../Swift/true.md) if the block successfully mapped memory; otherwise [`false`](../Swift/false.md).

## Parameters

- `task`: The task to map the memory into.
- `rangeCount  `: The number of ranges to map.
- `virtualOffset   `: The offset from the task’s base address where mapping starts.
- `readOnly  `: A Boolean value that indicates whether the block maps memory for read access only.
- `ranges  `: The set of ranges to map.

## See Also

### Managing Memory Operations
- [mapMemory](./pgdevicedescriptor/mapmemory.md)
  A handler that the framework calls to map memory into the virtual machine.
- [unmapMemory](./pgdevicedescriptor/unmapmemory.md)
  A handler that the framework calls to unmap memory from the virtual machine.
- [readMemory](./pgdevicedescriptor/readmemory.md)
  A handler that the framework calls to read data from the guest’s memory.
- [PGUnmapMemory](./pgunmapmemory.md)
  The block signature for a routine that unmaps guest physical memory from a task.
- [PGReadMemory](./pgreadmemory.md)
  The block signature for a routine that copies data from guest physical memory into host memory.
- [struct PGPhysicalMemoryRange_s](./pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgmapmemory)*