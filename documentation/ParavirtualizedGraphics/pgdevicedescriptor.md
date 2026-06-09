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
### Managing Memory Operations
- [struct PGPhysicalMemoryRange_s](pgphysicalmemoryrange_s.md)
  A range in the guest virtual machine’s physical memory address space.
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

- [protocol PGDevice](pgdevice.md)
  A paravirtualized GPU device object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor)*