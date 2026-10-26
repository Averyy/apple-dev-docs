# PGPhysicalMemoryRange_s

**Framework**: Paravirtualized Graphics  
**Kind**: struct  
**Role**: Structure

A range in the guest virtual machine’s physical memory address space.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
struct PGPhysicalMemoryRange_s
```

```c
struct PGPhysicalMemoryRange_s;
```

## Topics

### Creating a Memory Range
- [init()](./pgphysicalmemoryrange_s/init%28%29.md)
  Creates a default memory range.
- [init(physicalAddress: UInt64, physicalLength: UInt64)](./pgphysicalmemoryrange_s/init%28physicaladdress,physicallength%29.md)
  Creates a memory range.
### Inspecting Range Properties
- [var physicalAddress: UInt64](./pgphysicalmemoryrange_s/physicaladdress.md)
  The starting address of the range in physical memory.
- [var physicalLength: UInt64](./pgphysicalmemoryrange_s/physicallength.md)
  The length of the range.
### Type alias
- [typealias PGPhysicalMemoryRange_t](./pgphysicalmemoryrange_t.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

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
- [PGReadMemory](./pgreadmemory.md)
  The block signature for a routine that copies data from guest physical memory into host memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgphysicalmemoryrange_s)*