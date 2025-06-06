# PGMapMemory

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that maps guest physical memory into a task.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGMapMemory = (OpaquePointer, UInt32, UInt64, Bool, UnsafeMutablePointer<PGPhysicalMemoryRange_t>) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the block successfully mapped memory; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `task`: The task to map the memory into.
- `rangeCount  `: The number of ranges to map.
- `virtualOffset   `: The offset from the task’s base address where mapping starts.
- `readOnly  `: A Boolean value that indicates whether the block maps memory for read access only.
- `ranges  `: The set of ranges to map.

## See Also

- [var mapMemory: PGMapMemory?](pgdevicedescriptor/mapmemory.md)
  A handler that the framework calls to map memory into the virtual machine.
- [var unmapMemory: PGUnmapMemory?](pgdevicedescriptor/unmapmemory.md)
  A handler that the framework calls to unmap memory from the virtual machine.
- [var readMemory: PGReadMemory?](pgdevicedescriptor/readmemory.md)
  A handler that the framework calls to read data from the guest’s memory.
- [typealias PGUnmapMemory](pgunmapmemory.md)
  The block signature for a routine that unmaps guest physical memory from a task.
- [typealias PGReadMemory](pgreadmemory.md)
  The block signature for a routine that copies data from guest physical memory into host memory.
- [struct PGPhysicalMemoryRange_s](pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgmapmemory)*