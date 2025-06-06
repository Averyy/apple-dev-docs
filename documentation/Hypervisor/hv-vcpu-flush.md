# hv_vcpu_flush(_:)

**Framework**: Hypervisor  
**Kind**: func

Flushes the cached state of a vCPU.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vcpu_flush(_ vcpu: hv_vcpuid_t) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.

## See Also

- [func hv_vcpu_run_until(hv_vcpuid_t, UInt64) -> hv_return_t](hv_vcpu_run_until(_:_:).md)
  Executes a vCPU until it reaches the deadline defined in absolute time units you provide.
- [func hv_vcpu_interrupt(UnsafeMutablePointer<hv_vcpuid_t>, UInt32) -> hv_return_t](hv_vcpu_interrupt(_:_:).md)
  Forces the vCPU instances you provide to immediately exit the VM.
- [func hv_vcpu_invalidate_tlb(hv_vcpuid_t) -> hv_return_t](hv_vcpu_invalidate_tlb(_:).md)
  Invalidates the translation look-aside buffer (TLB) of a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_exec_time(_:_:).md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [func hv_vcpu_run(hv_vcpu_t) -> hv_return_t](hv_vcpu_run(_:).md)
  Starts the execution of a vCPU.
- [Execution Deadlines](3553338-execution-deadlines.md)
  An enumeration that describes available execution deadlines available to vCPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_flush(_:))*