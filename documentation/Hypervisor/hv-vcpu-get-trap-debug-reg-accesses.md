# hv_vcpu_get_trap_debug_reg_accesses(_:_:)

**Framework**: Hypervisor  
**Kind**: func

Gets whether debug-register accesses exit the guest.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_get_trap_debug_reg_accesses(_ vcpu: hv_vcpu_t, _ value: UnsafeMutablePointer<Bool>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

This includes the registers `DBGBCR<n>_EL1`, `DBGBVR<n>_EL1`, `DBGWCR<n>_EL1`, `DBGWVR<n>_EL1` and `MDSCR_EL1`.

The equivalent system register is `MDCR_EL2.TDA`.

> ❗ **Important**:  This function must be called by the owning thread.

 This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `value`: Indicates whether debug-register accesses in the guest trap to the host on output.

## See Also

- [func hv_vcpu_get_trap_debug_exceptions(hv_vcpu_t, UnsafeMutablePointer<Bool>) -> hv_return_t](hv_vcpu_get_trap_debug_exceptions(_:_:).md)
  Gets whether debug exceptions exit the guest.
- [func hv_vcpu_set_trap_debug_exceptions(hv_vcpu_t, Bool) -> hv_return_t](hv_vcpu_set_trap_debug_exceptions(_:_:).md)
  Sets whether debug exceptions exit the guest.
- [func hv_vcpu_set_trap_debug_reg_accesses(hv_vcpu_t, Bool) -> hv_return_t](hv_vcpu_set_trap_debug_reg_accesses(_:_:).md)
  Sets whether debug-register accesses exit the guest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_trap_debug_reg_accesses(_:_:))*