# hv_vcpuid_t

**Framework**: Hypervisor  
**Kind**: typealias

The type that describes a vCPU ID.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_vcpuid_t = UInt32
```

## See Also

- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpu_t>, UnsafeMutablePointer<UnsafeMutablePointer<hv_vcpu_exit_t>?>, hv_vcpu_config_t?) -> hv_return_t](hv_vcpu_create(_:_:_:).md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpu_t) -> hv_return_t](hv_vcpu_destroy(_:).md)
  Destroys the vCPU instance associated with the current thread.
- [typealias hv_vcpu_options_t](hv_vcpu_options_t.md)
  Options for creating a new vCPU instance.
- [vCPU Creation Behavior](1447317-vcpu-creation-behavior.md)
  An enumeration representing the default creation options for virtual CPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpuid_t)*