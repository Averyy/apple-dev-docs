# hv_vm_get_max_vcpu_count(_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Returns the maximum number of vCPUs that the hypervisor supports.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vm_get_max_vcpu_count(_ max_vcpu_count: UnsafeMutablePointer<UInt32>) -> hv_return_t
```

```c
extern hv_return_t hv_vm_get_max_vcpu_count(uint32_t *max_vcpu_count);
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

## Parameters

- `max_vcpu_count`: The maximum number of vCPUs on output. Undefined if the call doesn’t succeed.

## See Also

### Creation and destruction
- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpu_t>, UnsafeMutablePointer<UnsafeMutablePointer<hv_vcpu_exit_t>?>, hv_vcpu_config_t?) -> hv_return_t](./hv_vcpu_create%28_,_,_%29.md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpu_t) -> hv_return_t](./hv_vcpu_destroy%28_%29.md)
  Destroys the vCPU instance associated with the current thread.
- [typealias hv_vcpu_t](./hv_vcpu_t.md)
  An opaque value that represents a vCPU instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_get_max_vcpu_count(_:))*