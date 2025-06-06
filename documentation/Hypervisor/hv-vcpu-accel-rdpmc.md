# HV_VCPU_ACCEL_RDPMC

**Framework**: Hypervisor  
**Kind**: var

Instructs the kernel, when set, to handle RDPMC VM exits directly rather than passing them to user space.

**Availability**:
- macOS ?+

## Declaration

```swift
var HV_VCPU_ACCEL_RDPMC: Int { get }
```

## Mentions

- [Extending vCPU Capabilities Using Model-Specific Registers](extending-vcpu-capabilities-using-model-specific-registers.md)

#### Discussion

When the guest issues RDPMC instructions, a VM exit occurs. When set, this flag instructs the kernel to handle RDRPMC VM exits directly, and more efficiently, than passing them on to user space.

## See Also

- [var HV_VCPU_DEFAULT: Int](hv_vcpu_default.md)
  The default vCPU creation behavior.
- [var HV_VCPU_TSC_RELATIVE: Int](hv_vcpu_tsc_relative.md)
  The value that represents the relative offset the system should add to the hypervisor TSC clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_accel_rdpmc)*