# hv_vcpu_options_t

**Framework**: Hypervisor  
**Kind**: typealias  
**Role**: Type Alias

Options for creating a new vCPU instance.

**Availability**:
- macOS

## Declaration

```swift
typealias hv_vcpu_options_t = UInt64
```

```c
typedef uint64_t hv_vcpu_options_t;
```

## Topics

### Constants
- [var HV_VCPU_DEFAULT: Int](./hv_vcpu_default.md)
  The default vCPU creation behavior.

## See Also

### Creation and destruction
- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpu_t>, UnsafeMutablePointer<UnsafeMutablePointer<hv_vcpu_exit_t>?>, hv_vcpu_config_t?) -> hv_return_t](./hv_vcpu_create%28_,_,_%29.md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpu_t) -> hv_return_t](./hv_vcpu_destroy%28_%29.md)
  Destroys the vCPU instance associated with the current thread.
- [vCPU Creation Behavior](./api-1447317-vcpu-creation-behavior.md)
  An enumeration representing the default creation options for virtual CPUs.
- [typealias hv_vcpuid_t](./hv_vcpuid_t.md)
  The type that describes a vCPU ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_options_t)*