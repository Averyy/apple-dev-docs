# Exits

**Framework**: Hypervisor

Describe virtual machine exit conditions.

## Topics

### Descriptor
- [struct hv_vcpu_exit_t](hv_vcpu_exit_t.md)
  Information about an exit from the vCPU to the host.
### Exit reasons
- [struct hv_exit_reason_t](hv_exit_reason_t.md)
  The type that describes the event that triggered a guest exit to the host.
- [typealias hv_exception_syndrome_t](hv_exception_syndrome_t.md)
  Type of a vCPU exception syndrome.
- [typealias hv_exception_address_t](hv_exception_address_t.md)
  Type of a vCPU exception virtual address.

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
- [struct hv_interrupt_type_t](hv_interrupt_type_t.md)
  The type that defines the vCPU’s interrupts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/exits)*