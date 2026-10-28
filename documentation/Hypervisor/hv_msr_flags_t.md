# hv_msr_flags_t

**Framework**: Hypervisor  
**Kind**: typealias  
**Role**: Type Alias

The type representing the native Model-Specific Register (MSR) permissions.

**Availability**:
- macOS

## Declaration

```swift
typealias hv_msr_flags_t = UInt32
```

```c
typedef uint32_t hv_msr_flags_t;
```

## Discussion

This type represents the native MSR permissions for `hv_vm_enable_managed_msr()`. The [MSR Permissions](./api-3567078-msr_permissions-enum.md) enumeration describes the available permission values.

## See Also

### Model-Specific Registers
- [Extending vCPU Capabilities Using Model-Specific Registers](./extending-vcpu-capabilities-using-model-specific-registers.md)
  Configure specific client performance monitoring and enable other vCPU capabilities using Model-Specific Registers.
- [func hv_vcpu_read_msr(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_read_msr%28_,_,_%29.md)
  Returns, by reference, the current value of a Model-Specific Register (MSR) of a vCPU.
- [func hv_vcpu_write_msr(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](./hv_vcpu_write_msr%28_,_,_%29.md)
  Sets the value of a Model-Specific Register (MSR) of a vCPU.
- [func hv_vcpu_enable_native_msr(hv_vcpuid_t, UInt32, Bool) -> hv_return_t](./hv_vcpu_enable_native_msr%28_,_,_%29.md)
  Enables or disables a Model-Specific Register (MSR) that the VM uses natively.
- [func hv_vcpu_set_msr_access(hv_vcpuid_t, UInt32, hv_msr_flags_t) -> hv_return_t](./hv_vcpu_set_msr_access%28_,_,_%29.md)
  Controls the guest access of a managed Model-Specific Register (MSR).
- [func hv_vcpu_enable_managed_msr(hv_vcpuid_t, UInt32, Bool) -> hv_return_t](./hv_vcpu_enable_managed_msr%28_,_,_%29.md)
  Enables the guest access of a managed Model-Specific Register (MSR).
- [Model-Specific Registers](./api-3727856-model-specific-registers.md)
- [MSR Permissions](./api-3567078-msr_permissions-enum.md)
  An enumeration that describes possible Model-Specific Register (MSR) permisssions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_msr_flags_t)*