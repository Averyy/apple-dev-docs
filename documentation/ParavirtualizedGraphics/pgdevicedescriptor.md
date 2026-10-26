# PGDeviceDescriptor

**Framework**: Paravirtualized Graphics  
**Kind**: class  
**Role**: Class

A description of the paravirtualized graphics device to create.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class PGDeviceDescriptor
```

```objc
@interface PGDeviceDescriptor : NSObject
```

## Topics

### Specifying the GPU
- [var device: (any MTLDevice)?](./pgdevicedescriptor/device.md)
  The Metal device object to use to back the virtual graphics device.
### Managing Memory Operations
- [struct PGPhysicalMemoryRange_s](./pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.
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
### Handling Interrupts
- [var raiseInterrupt: PGRaiseInterrupt?](./pgdevicedescriptor/raiseinterrupt.md)
  A handler that the system calls to raise an interrupt in the guest environment.
- [typealias PGRaiseInterrupt](./pgraiseinterrupt.md)
  The block signature for a routine that raises interrupts in the guest environment.
### Specifying Virtual Device Properties
- [var mmioLength: Int](./pgdevicedescriptor/mmiolength.md)
  The length in bytes of the memory-mapped IO section.
### Instance Properties
- [var displayPortCount: UInt32](./pgdevicedescriptor/displayportcount.md)
### Managing Tasks
- [createTask](./pgdevicedescriptor/createtask.md)
  A handler that the framework calls to create a task object.
- [destroyTask](./pgdevicedescriptor/destroytask.md)
  A handler that the framework calls to destroy a task object.
- [PGCreateTask](./pgcreatetask.md)
  The block signature for a routine that creates a task.
- [PGDestroyTask](./pgdestroytask.md)
  The block signature for a routine that destroys a task.
- [PGTask_t](./pgtask_t.md)
  An opaque data pointer representing a specific virtual task.
### Specifying Trace Behavior
- [addTraceRange](./pgdevicedescriptor/addtracerange.md)
  A handler that the framework calls to add a trace range.
- [removeTraceRange](./pgdevicedescriptor/removetracerange.md)
  A handler that the framework calls to remove a trace range.
- [PGAddTraceRange](./pgaddtracerange.md)
  The block signature for a routine that adds a trace range.
- [PGRemoveTraceRange](./pgremovetracerange.md)
  The block signature for a routine that removes a trace range.
- [PGTraceRangeHandler](./pgtracerangehandler.md)
  The block signature for a routine that handles trace requests.
- [PGTraceRange_t](./pgtracerange_t.md)
  An opaque data pointer representing a specific trace.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Devices
- [protocol PGDevice](./pgdevice.md)
  A paravirtualized GPU device object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor)*