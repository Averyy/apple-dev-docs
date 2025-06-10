# hv_vcpu_get_sys_reg(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Gets the current value of a vCPU system register.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_get_sys_reg(_ vcpu: hv_vcpu_t, _ reg: hv_sys_reg_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

> ❗ **Important**:  This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `reg`: The ID of the system register.
- `value`: The value of the register   on output.

## See Also

- [func hv_vcpu_set_sys_reg(hv_vcpu_t, hv_sys_reg_t, UInt64) -> hv_return_t](hv_vcpu_set_sys_reg(_:_:_:).md)
  Sets the value of a vCPU system register.
- [struct hv_sys_reg_t](hv_sys_reg_t.md)
  The type of system registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_sys_reg(_:_:_:))*