# Execution Deadlines

**Framework**: Hypervisor

An enumeration that describes available execution deadlines available to vCPUs.

## Topics

### Deadlines
- [var HV_DEADLINE_FOREVER: UInt](hv_deadline_forever.md)
  The value that indicates a vCPU deadline that never expires.

## See Also

- [func hv_vcpu_run_until(hv_vcpuid_t, UInt64) -> hv_return_t](hv_vcpu_run_until(_:_:).md)
  Executes a vCPU until it reaches the deadline defined in absolute time units you provide.
- [func hv_vcpu_interrupt(UnsafeMutablePointer<hv_vcpuid_t>, UInt32) -> hv_return_t](hv_vcpu_interrupt(_:_:).md)
  Forces the vCPU instances you provide to immediately exit the VM.
- [func hv_vcpu_invalidate_tlb(hv_vcpuid_t) -> hv_return_t](hv_vcpu_invalidate_tlb(_:).md)
  Invalidates the translation look-aside buffer (TLB) of a vCPU.
- [func hv_vcpu_flush(hv_vcpuid_t) -> hv_return_t](hv_vcpu_flush(_:).md)
  Flushes the cached state of a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_exec_time(_:_:).md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [func hv_vcpu_run(hv_vcpu_t) -> hv_return_t](hv_vcpu_run(_:).md)
  Starts the execution of a vCPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/3553338-execution-deadlines)*