# hv_vcpu_set_simd_fp_reg(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Sets the value of a vCPU SIMD&FP register.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_set_simd_fp_reg(_ vcpu: hv_vcpu_t, _ reg: hv_simd_fp_reg_t, _ value: hv_simd_fp_uchar16_t) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_set_simd_fp_reg(hv_vcpu_t vcpu, hv_simd_fp_reg_t reg, hv_simd_fp_uchar16_t value);
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

#### Discussion

This function must be called by the owning thread.

## Parameters

- `vcpu`: The instance of the vCPU.
- `reg`: The ID of the SIMD&FP register.
- `value`: The new value of the register.

## See Also

### SIMD & Floating-point registers
- [func hv_vcpu_get_simd_fp_reg(hv_vcpu_t, hv_simd_fp_reg_t, UnsafeMutablePointer<hv_simd_fp_uchar16_t>) -> hv_return_t](./hv_vcpu_get_simd_fp_reg%28_,_,_%29.md)
  Gets the current value of a vCPU SIMD and FP register.
- [typealias hv_simd_fp_uchar16_t](./hv_simd_fp_uchar16_t.md)
  The value that represents an ARM SIMD and FP register.
- [struct hv_simd_fp_reg_t](./hv_simd_fp_reg_t.md)
  The type that defines SIMD and floating-point registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_set_simd_fp_reg(_:_:_:))*