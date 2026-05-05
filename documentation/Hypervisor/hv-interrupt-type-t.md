# hv_interrupt_type_t

**Framework**: Hypervisor  
**Kind**: struct

The type that defines the vCPU’s interrupts.

**Availability**:
- macOS ?+

## Declaration

```swift
struct hv_interrupt_type_t
```

#### Overview

To raise interrupts on a vCPU, call [`hv_vcpu_set_pending_interrupt(_:_:_:)`](hv_vcpu_set_pending_interrupt(_:_:_:).md) prior to calling [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md).

## Topics

### Instance properties
- [var rawValue: UInt32](hv_interrupt_type_t/rawvalue.md)
  An unisgned 32-bit integer that describes the interrupts.
### Initializers
- [init(UInt32)](hv_interrupt_type_t/init(_:).md)
  Creates a new interrupt instance with the value you provide.
- [init(rawValue: UInt32)](hv_interrupt_type_t/init(rawvalue:).md)
  Creates a new interrupt instance with the integer value you provide.
### Interrupt levels
- [var HV_INTERRUPT_TYPE_FIQ: hv_interrupt_type_t](hv_interrupt_type_fiq.md)
  ARM Fast Interrupt Request.
- [var HV_INTERRUPT_TYPE_IRQ: hv_interrupt_type_t](hv_interrupt_type_irq.md)
  ARM Interrupt Request.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func hv_vcpu_run(hv_vcpuid_t) -> hv_return_t](hv_vcpu_run(_:).md)
  Starts the execution of a vCPU.
- [func hv_vcpus_exit(UnsafeMutablePointer<hv_vcpu_t>, UInt32) -> hv_return_t](hv_vcpus_exit(_:_:).md)
  Forces an immediate exit of a set of vCPUs of the VM.
- [func hv_vcpu_get_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_get_pending_interrupt(_:_:_:).md)
  Gets pending interrupts for a vCPU.
- [func hv_vcpu_set_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, Bool) -> hv_return_t](hv_vcpu_set_pending_interrupt(_:_:_:).md)
  Sets pending interrupts for a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpuid_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_exec_time(_:_:).md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [Exits](exits.md)
  Describe virtual machine exit conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_interrupt_type_t)*