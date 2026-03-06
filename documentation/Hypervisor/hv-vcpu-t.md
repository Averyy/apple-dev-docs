# hv_vcpu_t

**Framework**: Hypervisor  
**Kind**: typealias

An opaque value that represents a vCPU instance.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_vcpu_t = UInt64
```

## See Also

- [func hv_vm_get_max_vcpu_count(UnsafeMutablePointer<UInt32>) -> hv_return_t](hv_vm_get_max_vcpu_count(_:).md)
  Returns the maximum number of vCPUs that the hypervisor supports.
- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpuid_t>, hv_vcpu_options_t) -> hv_return_t](hv_vcpu_create(_:_:).md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpuid_t) -> hv_return_t](hv_vcpu_destroy(_:).md)
  Destroys the vCPU instance associated with the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_t)*