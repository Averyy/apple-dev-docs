# hv_vm_get_max_vcpu_count(_:)

**Framework**: Hypervisor  
**Kind**: func

Returns the maximum number of vCPUs that the hypervisor supports.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vm_get_max_vcpu_count(_ max_vcpu_count: UnsafeMutablePointer<UInt32>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

## Parameters

- `max_vcpu_count`: The maximum number of vCPUs on output. Undefined if the call doesn’t succeed.

## See Also

- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpuid_t>, hv_vcpu_options_t) -> hv_return_t](hv_vcpu_create(_:_:).md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpuid_t) -> hv_return_t](hv_vcpu_destroy(_:).md)
  Destroys the vCPU instance associated with the current thread.
- [typealias hv_vcpu_t](hv_vcpu_t.md)
  An opaque value that represents a vCPU instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vm_get_max_vcpu_count(_:))*