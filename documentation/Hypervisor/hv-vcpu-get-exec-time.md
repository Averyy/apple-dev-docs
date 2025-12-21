# hv_vcpu_get_exec_time(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vcpu_get_exec_time(_ vcpu: hv_vcpuid_t, _ time: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

> ❗ **Important**:  This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `time`: The execution time on output, in nanoseconds.

## See Also

- [func hv_vcpu_run(hv_vcpuid_t) -> hv_return_t](hv_vcpu_run(_:).md)
  Starts the execution of a vCPU.
- [func hv_vcpus_exit(UnsafeMutablePointer<hv_vcpu_t>, UInt32) -> hv_return_t](hv_vcpus_exit(_:_:).md)
  Forces an immediate exit of a set of vCPUs of the VM.
- [func hv_vcpu_get_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_get_pending_interrupt(_:_:_:).md)
  Gets pending interrupts for a vCPU.
- [func hv_vcpu_set_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, Bool) -> hv_return_t](hv_vcpu_set_pending_interrupt(_:_:_:).md)
  Sets pending interrupts for a vCPU.
- [struct hv_interrupt_type_t](hv_interrupt_type_t.md)
  The type that defines the vCPU’s interrupts.
- [Exits](exits.md)
  Describe virtual machine exit conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_exec_time(_:_:))*