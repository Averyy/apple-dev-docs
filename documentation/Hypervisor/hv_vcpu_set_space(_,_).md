# hv_vcpu_set_space(_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Associates the vCPU instance with an allocated address space.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func hv_vcpu_set_space(_ vcpu: hv_vcpuid_t, _ asid: hv_vm_space_t) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_set_space(hv_vcpuid_t vcpu, hv_vm_space_t asid);
```

## Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## Discussion

> ❗ **Important**:  This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `asid`: The address space ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_set_space(_:_:))*