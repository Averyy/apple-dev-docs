# hv_vcpu_run(_:)

**Framework**: Hypervisor  
**Kind**: func

Starts the execution of a vCPU.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_run(_ vcpu: hv_vcpu_t) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

Call blocks until the next exit of the vCPU. The owning thread must call this function.

On an Apple Silicon, if the exit is of type [`HV_EXIT_REASON_VTIMER_ACTIVATED`](hv_exit_reason_vtimer_activated.md), the VTimer is automatically masked. As a result, no timer fires until the timer is unmasked with [`hv_vcpu_set_vtimer_mask(_:_:)`](hv_vcpu_set_vtimer_mask(_:_:).md).

On an Intel-based Mac, [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md) exits from causes external to the guest. To avoid the overhead of spurious exits use [`hv_vcpu_run_until(_:_:)`](hv_vcpu_run_until(_:_:).md) with the deadline [`HV_DEADLINE_FOREVER`](hv_deadline_forever.md).

## Parameters

- `vcpu`: The instance of the vCPU.

## See Also

- [func hv_vcpus_exit(UnsafeMutablePointer<hv_vcpu_t>, UInt32) -> hv_return_t](hv_vcpus_exit(_:_:).md)
  Forces an immediate exit of a set of vCPUs of the VM.
- [func hv_vcpu_get_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_get_pending_interrupt(_:_:_:).md)
  Gets pending interrupts for a vCPU.
- [func hv_vcpu_set_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, Bool) -> hv_return_t](hv_vcpu_set_pending_interrupt(_:_:_:).md)
  Sets pending interrupts for a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_exec_time(_:_:).md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [struct hv_interrupt_type_t](hv_interrupt_type_t.md)
  The type that defines the vCPU’s interrupts.
- [Exits](exits.md)
  Describe virtual machine exit conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_run(_:))*