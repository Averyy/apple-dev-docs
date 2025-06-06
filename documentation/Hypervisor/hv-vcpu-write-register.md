# hv_vcpu_write_register(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func

Sets the value of an architectural x86 register of a vCPU.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func hv_vcpu_write_register(_ vcpu: hv_vcpuid_t, _ reg: hv_x86_reg_t, _ value: UInt64) -> hv_return_t
```

#### Return Value

[`HV_SUCCESS`](hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](hv_return_t.md).

#### Discussion

> ❗ **Important**:  This function must be called by the owning thread.

 This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `reg`: The ID of the register. For possible values, see  .
- `value`: The new value of the register  .

## See Also

- [func hv_vcpu_read_register(hv_vcpuid_t, hv_x86_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t](hv_vcpu_read_register(_:_:_:).md)
  Returns, by reference, the current value of an architectural x86 register of a vCPU.
- [struct hv_x86_reg_t](hv_x86_reg_t.md)
  The type that defines x86 architectural registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_write_register(_:_:_:))*