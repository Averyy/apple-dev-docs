# hv_vcpus_exit(_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Forces an immediate exit of a set of vCPUs of the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpus_exit(_ vcpus: UnsafeMutablePointer<hv_vcpu_t>, _ vcpu_count: UInt32) -> hv_return_t
```

```c
extern hv_return_t hv_vcpus_exit(hv_vcpu_t *vcpus, uint32_t vcpu_count);
```

## Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## Parameters

- `vcpus`: An array of vCPU instances.
- `vcpu_count`: The number of vCPUs in the array.

## See Also

### Runtime
- [func hv_vcpu_run(hv_vcpu_t) -> hv_return_t](./hv_vcpu_run%28_%29.md)
  Starts the execution of a vCPU.
- [func hv_vcpu_get_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, UnsafeMutablePointer<Bool>) -> hv_return_t](./hv_vcpu_get_pending_interrupt%28_,_,_%29.md)
  Gets pending interrupts for a vCPU.
- [func hv_vcpu_set_pending_interrupt(hv_vcpu_t, hv_interrupt_type_t, Bool) -> hv_return_t](./hv_vcpu_set_pending_interrupt%28_,_,_%29.md)
  Sets pending interrupts for a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_get_exec_time%28_,_%29.md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [struct hv_interrupt_type_t](./hv_interrupt_type_t.md)
  The type that defines the vCPU’s interrupts.
- [Exits](./exits.md)
  Describe virtual machine exit conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpus_exit(_:_:))*