# hv_vmx_vcpu_read_shadow_vmcs(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Returns the current value of a shadow VMCS field of a vCPU.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func hv_vmx_vcpu_read_shadow_vmcs(_ vcpu: hv_vcpuid_t, _ field: UInt32, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

> ❗ **Important**:  This function must be called by the owning thread.

 This function must be called by the owning thread.

## Parameters

- `vcpu`: The vCPU ID.
- `field`: The ID of the shadow VMCS field to read.
- `value`: The pointer to the shadow VMCS field value the Hypervisor writes following a successful operation.

## See Also

- [func hv_vmx_vcpu_set_shadow_access(hv_vcpuid_t, UInt32, hv_shadow_flags_t) -> hv_return_t](hv_vmx_vcpu_set_shadow_access(_:_:_:).md)
  Set the access permissions of a shadow VMCS field of a vCPU.
- [func hv_vmx_vcpu_write_shadow_vmcs(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](hv_vmx_vcpu_write_shadow_vmcs(_:_:_:).md)
  Set the value of a shadow VMCS field of a vCPU.
- [typealias hv_shadow_flags_t](hv_shadow_flags_t.md)
  Shadow VMCS permissions for the set shadow access function.
- [Shadow Permissions](3567083-shadow_permissions-enum.md)
  Permissions that define access to the shadow VMCS fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vmx_vcpu_read_shadow_vmcs(_:_:_:))*