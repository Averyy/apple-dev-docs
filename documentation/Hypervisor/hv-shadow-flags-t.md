# hv_shadow_flags_t

**Framework**: Hypervisor  
**Kind**: typealias

Shadow VMCS permissions for the set shadow access function.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_shadow_flags_t = UInt64
```

## See Also

- [func hv_vmx_vcpu_read_shadow_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vmx_vcpu_read_shadow_vmcs(_:_:_:).md)
  Returns the current value of a shadow VMCS field of a vCPU.
- [func hv_vmx_vcpu_set_shadow_access(hv_vcpuid_t, UInt32, hv_shadow_flags_t) -> hv_return_t](hv_vmx_vcpu_set_shadow_access(_:_:_:).md)
  Set the access permissions of a shadow VMCS field of a vCPU.
- [func hv_vmx_vcpu_write_shadow_vmcs(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](hv_vmx_vcpu_write_shadow_vmcs(_:_:_:).md)
  Set the value of a shadow VMCS field of a vCPU.
- [Shadow Permissions](3567083-shadow_permissions-enum.md)
  Permissions that define access to the shadow VMCS fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_shadow_flags_t)*