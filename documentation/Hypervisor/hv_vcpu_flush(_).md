# hv_vcpu_flush(_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Flushes the cached state of a vCPU.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: This API has no effect and always returns HV_UNSUPPORTED

## Declaration

```swift
func hv_vcpu_flush(_ vcpu: hv_vcpuid_t) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_flush(hv_vcpuid_t vcpu);
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

#### Discussion

This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.

## See Also

### Runtime
- [func hv_vcpu_run_until(hv_vcpuid_t, UInt64) -> hv_return_t](./hv_vcpu_run_until%28_,_%29.md)
  Executes a vCPU until it reaches the deadline defined in absolute time units you provide.
- [func hv_vcpu_interrupt(UnsafeMutablePointer<hv_vcpuid_t>, UInt32) -> hv_return_t](./hv_vcpu_interrupt%28_,_%29.md)
  Forces the vCPU instances you provide to immediately exit the VM.
- [func hv_vcpu_get_exec_time(hv_vcpu_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_get_exec_time%28_,_%29.md)
  Returns, by reference, the cumulative execution time of a vCPU, in nanoseconds.
- [func hv_vcpu_run(hv_vcpu_t) -> hv_return_t](./hv_vcpu_run%28_%29.md)
  Starts the execution of a vCPU.
- [Execution Deadlines](./api-3553338-execution-deadlines.md)
  An enumeration that describes available execution deadlines available to vCPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_flush(_:))*