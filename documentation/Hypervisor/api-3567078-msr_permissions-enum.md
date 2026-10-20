# MSR Permissions

**Framework**: Hypervisor  
**Role**: API Collection

An enumeration that describes possible Model-Specific Register (MSR) permisssions.

## Topics

### Permissions
- [var HV_MSR_NONE: Int](./hv_msr_none.md)
  The Model-Specific Register (MSR) no-access permission.
- [var HV_MSR_READ: Int](./hv_msr_read.md)
  The Model-Specific Register (MSR) read permission.
- [var HV_MSR_WRITE: Int](./hv_msr_write.md)
  The Model-Specific Register (MSR) write permission.

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
- [typealias hv_msr_flags_t](./hv_msr_flags_t.md)
  The type representing the native Model-Specific Register (MSR) permissions.
- [Model-Specific Registers](./api-3727856-model-specific-registers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/3567078-msr_permissions-enum)*