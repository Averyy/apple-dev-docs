# unmapMemory

**Framework**: Paravirtualized Graphics  
**Kind**: property

A handler that the framework calls to unmap memory from the virtual machine.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var unmapMemory: PGUnmapMemory? { get set }
```

## See Also

- [var mapMemory: PGMapMemory?](pgdevicedescriptor/mapmemory.md)
  A handler that the framework calls to map memory into the virtual machine.
- [var readMemory: PGReadMemory?](pgdevicedescriptor/readmemory.md)
  A handler that the framework calls to read data from the guest’s memory.
- [typealias PGMapMemory](pgmapmemory.md)
  The block signature for a routine that maps guest physical memory into a task.
- [typealias PGUnmapMemory](pgunmapmemory.md)
  The block signature for a routine that unmaps guest physical memory from a task.
- [typealias PGReadMemory](pgreadmemory.md)
  The block signature for a routine that copies data from guest physical memory into host memory.
- [struct PGPhysicalMemoryRange_s](pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor/unmapmemory)*