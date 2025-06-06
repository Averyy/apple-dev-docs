# PGUnmapMemory

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that unmaps guest physical memory from a task.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGUnmapMemory = (OpaquePointer, UInt64, UInt64) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the block successfully unmapped memory; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `task`: The task to unmap memory from.
- `virtualOffset`: The offset from the task’s base address where unmapping starts.
- `length`: The number of bytes to unmap.

## See Also

- [var mapMemory: PGMapMemory?](pgdevicedescriptor/mapmemory.md)
  A handler that the framework calls to map memory into the virtual machine.
- [var unmapMemory: PGUnmapMemory?](pgdevicedescriptor/unmapmemory.md)
  A handler that the framework calls to unmap memory from the virtual machine.
- [var readMemory: PGReadMemory?](pgdevicedescriptor/readmemory.md)
  A handler that the framework calls to read data from the guest’s memory.
- [typealias PGMapMemory](pgmapmemory.md)
  The block signature for a routine that maps guest physical memory into a task.
- [typealias PGReadMemory](pgreadmemory.md)
  The block signature for a routine that copies data from guest physical memory into host memory.
- [struct PGPhysicalMemoryRange_s](pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgunmapmemory)*