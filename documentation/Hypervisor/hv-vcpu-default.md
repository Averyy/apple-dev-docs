# HV_VCPU_DEFAULT

**Framework**: Hypervisor  
**Kind**: var

The default vCPU creation behavior.

**Availability**:
- macOS ?+

## Declaration

```swift
var HV_VCPU_DEFAULT: Int { get }
```

## See Also

- [var HV_VCPU_ACCEL_RDPMC: Int](hv_vcpu_accel_rdpmc.md)
  Instructs the kernel, when set, to handle RDPMC VM exits directly rather than passing them to user space.
- [var HV_VCPU_TSC_RELATIVE: Int](hv_vcpu_tsc_relative.md)
  The value that represents the relative offset the system should add to the hypervisor TSC clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_default)*