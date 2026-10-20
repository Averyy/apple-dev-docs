# hv_vm_sync_tsc(_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Synchronizes guest timestamp counters (TSC) across all vCPUs.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vm_sync_tsc(_ tsc: UInt64) -> hv_return_t
```

```c
extern hv_return_t hv_vm_sync_tsc(uint64_t tsc);
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## Parameters

- `tsc`: The value of the guest TSC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_sync_tsc(_:))*