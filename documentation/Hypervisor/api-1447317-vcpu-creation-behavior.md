# vCPU Creation Behavior

**Framework**: Hypervisor

An enumeration representing the default creation options for virtual CPUs.

## Topics

### Constants
- [var HV_VCPU_DEFAULT: Int](hv_vcpu_default.md)
  The default vCPU creation behavior.
- [var HV_VCPU_ACCEL_RDPMC: Int](hv_vcpu_accel_rdpmc.md)
  Instructs the kernel, when set, to handle RDPMC VM exits directly rather than passing them to user space.
- [var HV_VCPU_TSC_RELATIVE: Int](hv_vcpu_tsc_relative.md)
  The value that represents the relative offset the system should add to the hypervisor TSC clock.

## See Also

- [func hv_vcpu_create(UnsafeMutablePointer<hv_vcpu_t>, UnsafeMutablePointer<UnsafeMutablePointer<hv_vcpu_exit_t>?>, hv_vcpu_config_t?) -> hv_return_t](hv_vcpu_create(_:_:_:).md)
  Creates a vCPU instance for the current thread.
- [func hv_vcpu_destroy(hv_vcpu_t) -> hv_return_t](hv_vcpu_destroy(_:).md)
  Destroys the vCPU instance associated with the current thread.
- [typealias hv_vcpu_options_t](hv_vcpu_options_t.md)
  Options for creating a new vCPU instance.
- [typealias hv_vcpuid_t](hv_vcpuid_t.md)
  The type that describes a vCPU ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/1447317-vcpu-creation-behavior)*