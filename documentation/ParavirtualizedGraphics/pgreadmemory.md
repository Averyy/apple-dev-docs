# PGReadMemory

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that copies data from guest physical memory into host memory.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGReadMemory = (UInt64, UInt64, UnsafeMutableRawPointer) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the block copied the data successfully; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `physicalAddress`: The physical guest address of the data to read.
- `length`: The number of bytes to read.
- `dst`: The destination for the copied data.

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
- [struct PGPhysicalMemoryRange_s](pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgreadmemory)*