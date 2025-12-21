# hv_vcpu_run_until(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Executes a vCPU until it reaches the deadline defined in absolute time units you provide.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func hv_vcpu_run_until(_ vcpu: hv_vcpuid_t, _ deadline: UInt64) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

If the deadline you specify is other than [`HV_DEADLINE_FOREVER`](hv_deadline_forever.md), this call uses the VMX preemption timer. If the hardware doesn’t support the VMX preemption timer, it returns [`HV_UNSUPPORTED`](hv_unsupported.md).

This function supersedes [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md) on Intel-based Mac computers. Unlike [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md), it doesn’t return on transparently handled VMEXITs.

## Parameters

- `vcpu`: The instance of the vCPU.
- `deadline`: The timer deadline in mach absolute time units. Use the special value   to specify a deadline that never expires.

## See Also

- [func hv_vcpu_interrupt(UnsafeMutablePointer<hv_vcpuid_t>, UInt32) -> hv_return_t](hv_vcpu_interrupt(_:_:).md)
  Forces the vCPU instances you provide to immediately exit the VM.
- [func hv_vcpu_invalidate_tlb(hv_vcpuid_t) -> hv_return_t](hv_vcpu_invalidate_tlb(_:).md)
  Invalidates the translation look-aside buffer (TLB) of a vCPU.
- [func hv_vcpu_flush(hv_vcpuid_t) -> hv_return_t](hv_vcpu_flush(_:).md)
  Flushes the cached state of a vCPU.
- [func hv_vcpu_get_exec_time(hv_vcpuid_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_get_exec_time(_:_:).md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [func hv_vcpu_run(hv_vcpuid_t) -> hv_return_t](hv_vcpu_run(_:).md)
  Starts the execution of a vCPU.
- [Execution Deadlines](3553338-execution-deadlines.md)
  An enumeration that describes available execution deadlines available to vCPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_run_until(_:_:))*