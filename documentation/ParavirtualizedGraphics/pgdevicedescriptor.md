# PGDeviceDescriptor

**Framework**: Paravirtualized Graphics  
**Kind**: class

A description of the paravirtualized graphics device to create.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class PGDeviceDescriptor
```

## Topics

### Specifying the GPU
- [var device: (any MTLDevice)?](pgdevicedescriptor/device.md)
  The Metal device object to use to back the virtual graphics device.
### Managing Tasks
- [var createTask: PGCreateTask?](pgdevicedescriptor/createtask.md)
  A handler that the framework calls to create a task object.
- [var destroyTask: PGDestroyTask?](pgdevicedescriptor/destroytask.md)
  A handler that the framework calls to destroy a task object.
- [typealias PGCreateTask](pgcreatetask.md)
  The block signature for a routine that creates a task.
- [typealias PGDestroyTask](pgdestroytask.md)
  The block signature for a routine that destroys a task.
### Managing Memory Operations
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
- [struct PGPhysicalMemoryRange_s](pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.
### Specifying Trace Behavior
- [var addTraceRange: PGAddTraceRange?](pgdevicedescriptor/addtracerange.md)
  A handler that the framework calls to add a trace range.
- [var removeTraceRange: PGRemoveTraceRange?](pgdevicedescriptor/removetracerange.md)
  A handler that the framework calls to remove a trace range.
- [typealias PGAddTraceRange](pgaddtracerange.md)
  The block signature for a routine that adds a trace range.
- [typealias PGRemoveTraceRange](pgremovetracerange.md)
  The block signature for a routine that removes a trace range.
- [typealias PGTraceRangeHandler](pgtracerangehandler.md)
  The block signature for a routine that handles trace requests.
### Handling Interrupts
- [var raiseInterrupt: PGRaiseInterrupt?](pgdevicedescriptor/raiseinterrupt.md)
  A handler that the system calls to raise an interrupt in the guest environment.
- [typealias PGRaiseInterrupt](pgraiseinterrupt.md)
  The block signature for a routine that raises interrupts in the guest environment.
### Specifying Virtual Device Properties
- [var mmioLength: Int](pgdevicedescriptor/mmiolength.md)
  The length in bytes of the memory-mapped IO section.
### Instance Properties
- [var displayPortCount: UInt32](pgdevicedescriptor/displayportcount.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func PGNewDeviceWithDescriptor(PGDeviceDescriptor) -> (any PGDevice)?](pgnewdevicewithdescriptor(_:).md)
  Creates a new paravirtualized graphics device.
- [protocol PGDevice](pgdevice.md)
  A paravirtualized GPU device object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor)*