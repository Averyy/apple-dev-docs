# Shadow Permissions

**Framework**: Hypervisor

Permissions that define access to the shadow VMCS fields.

## Topics

### Permissions
- [var HV_SHADOW_VMCS_NONE: Int](hv_shadow_vmcs_none.md)
  The value that indicates no access to the shadow VMCS fields.
- [var HV_SHADOW_VMCS_READ: Int](hv_shadow_vmcs_read.md)
  The value that indicates read access to the shadow VMCS fields.
- [var HV_SHADOW_VMCS_WRITE: Int](hv_shadow_vmcs_write.md)
  The value that indicates read access to the write access shadow VMCS fields.

## See Also

- [func hv_vmx_vcpu_read_shadow_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_read_shadow_vmcs(_:_:_:).md)
  Returns the current value of a shadow VMCS field of a vCPU.
- [func hv_vmx_vcpu_set_shadow_access(hv_vcpuid_t, UInt32, hv_shadow_flags_t) -> hv_return_t](hv_vmx_vcpu_set_shadow_access(_:_:_:).md)
  Set the access permissions of a shadow VMCS field of a vCPU.
- [func hv_vmx_vcpu_write_shadow_vmcs(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](hv_vmx_vcpu_write_shadow_vmcs(_:_:_:).md)
  Set the value of a shadow VMCS field of a vCPU.
- [typealias hv_shadow_flags_t](hv_shadow_flags_t.md)
  Shadow VMCS permissions for the set shadow access function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/3567083-shadow_permissions-enum)*