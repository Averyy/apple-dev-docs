# hv_vcpu_set_pending_interrupt(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Sets pending interrupts for a vCPU.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_set_pending_interrupt(_ vcpu: hv_vcpu_t, _ type: hv_interrupt_type_t, _ pending: Bool) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_set_pending_interrupt(hv_vcpu_t vcpu, hv_interrupt_type_t type, bool pending);
```

## Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## Discussion

> ❗ **Important**:  This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `type`: The interrupt from `Interrupt Constants`.
- `pending`: A Boolean that indicates whether the interrupt is pending.

## See Also

### Runtime
- [func hv_vcpu_run(hv_vcpu_t) -> hv_return_t](./hv_vcpu_run%28_%29.md)
  Starts the execution of a vCPU.
- [func hv_vcpus_exit(UnsafeMutablePointer<hv_vcpu_t>, UInt32) -> hv_return_t](./hv_vcpus_exit%28_,_%29.md)
  Forces an immediate exit of a set of vCPUs of the VM.
- [func hv_vcpu_get_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, UnsafeMutablePointer<Bool>) -> hv_return_t](./hv_vcpu_get_pending_interrupt%28_,_,_%29.md)
  Gets pending interrupts for a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_get_exec_time%28_,_%29.md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [struct hv_interrupt_type_t](./hv_interrupt_type_t.md)
  The type that defines the vCPU’s interrupts.
- [Exits](./exits.md)
  Describe virtual machine exit conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_set_pending_interrupt(_:_:_:))*