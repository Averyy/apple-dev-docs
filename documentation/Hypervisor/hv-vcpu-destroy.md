# hv_vcpu_destroy(_:)

**Framework**: Hypervisor  
**Kind**: func

Destroys the vCPU instance associated with the current thread.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_destroy(_ vcpu: hv_vcpu_t) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

> ❗ **Important**:  This function must be called by the owning thread.

 This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.

## See Also

- [func hv_vm_get_max_vcpu_count(UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vm_get_max_vcpu_count(_:).md)
  Returns the maximum number of vCPUs that the hypervisor supports.
- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpu_t>, UnsafeMutablePointer<UnsafeMutablePointer<hv_vcpu_exit_t>?>, hv_vcpu_config_t?) -> hv_return_t](hv_vcpu_create(_:_:_:).md)
  Creates a vCPU instance for the current thread.
- [typealias hv_vcpu_t](hv_vcpu_t.md)
  An opaque value that represents a vCPU instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_destroy(_:))*