# hv_vcpu_write_msr(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Sets the value of a Model-Specific Register (MSR) of a vCPU.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vcpu_write_msr(_ vcpu: hv_vcpuid_t, _ msr: UInt32, _ value: UInt64) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_write_msr(hv_vcpuid_t vcpu, uint32_t msr, uint64_t value);
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

#### Discussion

This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `msr`: The ID of the MSR.
- `value`: The new value for `msr`.

## See Also

### Model-Specific Registers
- [Extending vCPU Capabilities Using Model-Specific Registers](./extending-vcpu-capabilities-using-model-specific-registers.md)
  Configure specific client performance monitoring and enable other vCPU capabilities using Model-Specific Registers.
- [func hv_vcpu_read_msr(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t](./hv_vcpu_read_msr%28_,_,_%29.md)
  Returns, by reference, the current value of a Model-Specific Register (MSR) of a vCPU.
- [func hv_vcpu_enable_native_msr(hv_vcpuid_t, UInt32, Bool) -> hv_return_t](./hv_vcpu_enable_native_msr%28_,_,_%29.md)
  Enables or disables a Model-Specific Register (MSR) that the VM uses natively.
- [func hv_vcpu_set_msr_access(hv_vcpuid_t, UInt32, hv_msr_flags_t) -> hv_return_t](./hv_vcpu_set_msr_access%28_,_,_%29.md)
  Controls the guest access of a managed Model-Specific Register (MSR).
- [func hv_vcpu_enable_managed_msr(hv_vcpuid_t, UInt32, Bool) -> hv_return_t](./hv_vcpu_enable_managed_msr%28_,_,_%29.md)
  Enables the guest access of a managed Model-Specific Register (MSR).
- [typealias hv_msr_flags_t](./hv_msr_flags_t.md)
  The type representing the native Model-Specific Register (MSR) permissions.
- [Model-Specific Registers](./api-3727856-model-specific-registers.md)
- [MSR Permissions](./api-3567078-msr_permissions-enum.md)
  An enumeration that describes possible Model-Specific Register (MSR) permisssions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_write_msr(_:_:_:))*