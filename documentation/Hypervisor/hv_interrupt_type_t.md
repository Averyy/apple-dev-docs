# hv_interrupt_type_t

**Framework**: Hypervisor  
**Kind**: struct  
**Role**: Structure

The type that defines the vCPU’s interrupts.

**Availability**:
- macOS

## Declaration

```swift
struct hv_interrupt_type_t
```

```c
typedef enum { ... } hv_interrupt_type_t;
```

#### Overview

To raise interrupts on a vCPU, call [`hv_vcpu_set_pending_interrupt(_:_:_:)`](./hv_vcpu_set_pending_interrupt%28_,_,_%29.md) prior to calling [`hv_vcpu_run(_:)`](./hv_vcpu_run%28_%29.md).

## Topics

### Instance properties
- [var rawValue: UInt32](./hv_interrupt_type_t/rawvalue.md)
  An unisgned 32-bit integer that describes the interrupts.
### Initializers
- [init(UInt32)](./hv_interrupt_type_t/init%28_%29.md)
  Creates a new interrupt instance with the value you provide.
- [init(rawValue: UInt32)](./hv_interrupt_type_t/init%28rawvalue%29.md)
  Creates a new interrupt instance with the integer value you provide.
### Interrupt levels
- [var HV_INTERRUPT_TYPE_FIQ: hv_interrupt_type_t](./hv_interrupt_type_fiq.md)
  ARM Fast Interrupt Request.
- [var HV_INTERRUPT_TYPE_IRQ: hv_interrupt_type_t](./hv_interrupt_type_irq.md)
  ARM Interrupt Request.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Runtime
- [func hv_vcpu_run(hv_vcpu_t) -> hv_return_t](./hv_vcpu_run%28_%29.md)
  Starts the execution of a vCPU.
- [func hv_vcpus_exit(UnsafeMutablePointer<hv_vcpu_t>, UInt32) -> hv_return_t](./hv_vcpus_exit%28_,_%29.md)
  Forces an immediate exit of a set of vCPUs of the VM.
- [func hv_vcpu_get_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, UnsafeMutablePointer<Bool>) -> hv_return_t](./hv_vcpu_get_pending_interrupt%28_,_,_%29.md)
  Gets pending interrupts for a vCPU.
- [func hv_vcpu_set_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, Bool) -> hv_return_t](./hv_vcpu_set_pending_interrupt%28_,_,_%29.md)
  Sets pending interrupts for a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_get_exec_time%28_,_%29.md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [Exits](./exits.md)
  Describe virtual machine exit conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_interrupt_type_t)*