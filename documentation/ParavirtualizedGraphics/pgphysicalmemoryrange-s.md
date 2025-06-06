# PGPhysicalMemoryRange_s

**Framework**: Paravirtualized Graphics  
**Kind**: struct

A range in the guest virtual machine’s physical memory address space.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
struct PGPhysicalMemoryRange_s
```

## Topics

### Creating a Memory Range
- [init()](pgphysicalmemoryrange_s/init.md)
  Creates a default memory range.
- [init(physicalAddress: UInt64, physicalLength: UInt64)](pgphysicalmemoryrange_s/init(physicaladdress:physicallength:).md)
  Creates a memory range.
### Inspecting Range Properties
- [var physicalAddress: UInt64](pgphysicalmemoryrange_s/physicaladdress.md)
  The starting address of the range in physical memory.
- [var physicalLength: UInt64](pgphysicalmemoryrange_s/physicallength.md)
  The length of the range.
### Type alias
- [typealias PGPhysicalMemoryRange_t](pgphysicalmemoryrange_t.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var mapMemory: PGMapMemory?](pgdevicedescriptor/mapmemory.md)
  A handler that the framework calls to map memory into the virtual machine.
- [var unmapMemory: PGUnmapMemory?](pgdevicedescriptor/unmapmemory.md)
  A handler that the framework calls to unmap memory from the virtual machine.
- [var readMemory: PGReadMemory?](pgdevicedescriptor/readmemory.md)
  A handler that the framework calls to read data from the guest’s memory.
- [typealias PGMapMemory](pgmapmemory.md)
  The block signature for a routine that maps guest physical memory into a task.
- [typealias PGUnmapMemory](pgunmapmemory.md)
  The block signature for a routine that unmaps guest physical memory from a task.
- [typealias PGReadMemory](pgreadmemory.md)
  The block signature for a routine that copies data from guest physical memory into host memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgphysicalmemoryrange_s)*