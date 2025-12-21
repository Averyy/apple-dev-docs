# hv_vcpu_options_t

**Framework**: Hypervisor  
**Kind**: typealias

Options for creating a new vCPU instance.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_vcpu_options_t = UInt64
```

## Topics

### Constants
- [var HV_VCPU_DEFAULT: Int](hv_vcpu_default.md)
  The default vCPU creation behavior.

## See Also

- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpuid_t>, hv_vcpu_options_t) -> hv_return_t](hv_vcpu_create(_:_:).md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpuid_t) -> hv_return_t](hv_vcpu_destroy(_:).md)
  Destroys the vCPU instance associated with the current thread.
- [vCPU Creation Behavior](1447317-vcpu-creation-behavior.md)
  An enumeration representing the default creation options for virtual CPUs.
- [typealias hv_vcpuid_t](hv_vcpuid_t.md)
  The type that describes a vCPU ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_options_t)*