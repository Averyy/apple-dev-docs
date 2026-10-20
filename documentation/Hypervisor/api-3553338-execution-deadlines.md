# Execution Deadlines

**Framework**: Hypervisor  
**Role**: API Collection

An enumeration that describes available execution deadlines available to vCPUs.

## Topics

### Deadlines
- [var HV_DEADLINE_FOREVER: UInt](./hv_deadline_forever.md)
  The value that indicates a vCPU deadline that never expires.

## See Also

### Runtime
- [func hv_vcpu_run_until(hv_vcpuid_t, UInt64) -> hv_return_t](./hv_vcpu_run_until%28_,_%29.md)
  Executes a vCPU until it reaches the deadline defined in absolute time units you provide.
- [func hv_vcpu_interrupt(UnsafeMutablePointer<hv_vcpuid_t>, UInt32) -> hv_return_t](./hv_vcpu_interrupt%28_,_%29.md)
  Forces the vCPU instances you provide to immediately exit the VM.
- [func hv_vcpu_flush(hv_vcpuid_t) -> hv_return_t](./hv_vcpu_flush%28_%29.md)
  Flushes the cached state of a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_get_exec_time%28_,_%29.md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [func hv_vcpu_run(hv_vcpu_t) -> hv_return_t](./hv_vcpu_run%28_%29.md)
  Starts the execution of a vCPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/3553338-execution-deadlines)*