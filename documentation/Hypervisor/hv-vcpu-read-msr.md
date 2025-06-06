# hv_vcpu_read_msr(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Returns, by reference, the current value of a Model-Specific Register (MSR) of a vCPU.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vcpu_read_msr(_ vcpu: hv_vcpuid_t, _ msr: UInt32, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `msr`: The ID of the MSR.
- `value`: The value of  , on output.

## See Also

- [Extending vCPU Capabilities Using Model-Specific Registers](extending-vcpu-capabilities-using-model-specific-registers.md)
  Configure specific client performance monitoring and enable other vCPU capabilities using Model-Specific Registers.
- [func hv_vcpu_write_msr(hv_vcpuid_t, UInt32, UInt64) -> hv_return_t](hv_vcpu_write_msr(_:_:_:).md)
  Sets the value of a Model-Specific Register (MSR) of a vCPU.
- [func hv_vcpu_enable_native_msr(hv_vcpuid_t, UInt32, Bool) -> hv_return_t](hv_vcpu_enable_native_msr(_:_:_:).md)
  Enables or disables a Model-Specific Register (MSR) that the VM uses natively.
- [func hv_vcpu_set_msr_access(hv_vcpuid_t, UInt32, hv_msr_flags_t) -> hv_return_t](hv_vcpu_set_msr_access(_:_:_:).md)
  Controls the guest access of a managed Model-Specific Register (MSR).
- [func hv_vcpu_enable_managed_msr(hv_vcpuid_t, UInt32, Bool) -> hv_return_t](hv_vcpu_enable_managed_msr(_:_:_:).md)
  Enables the guest access of a managed Model-Specific Register (MSR).
- [typealias hv_msr_flags_t](hv_msr_flags_t.md)
  The type representing the native Model-Specific Register (MSR) permissions.
- [Model-Specific Registers](3727856-model-specific-registers.md)
- [MSR Permissions](3567078-msr_permissions-enum.md)
  An enumeration that describes possible Model-Specific Register (MSR) permisssions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_read_msr(_:_:_:))*