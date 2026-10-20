# hv_vcpu_get_simd_fp_reg(_:_:_:)

**Framework**: Hypervisor  
**Kind**: func  
**Role**: Function

Gets the current value of a vCPU SIMD and FP register.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func hv_vcpu_get_simd_fp_reg(_ vcpu: hv_vcpu_t, _ reg: hv_simd_fp_reg_t, _ value: UnsafeMutablePointer<hv_simd_fp_uchar16_t>) -> hv_return_t
```

```c
extern hv_return_t hv_vcpu_get_simd_fp_reg(hv_vcpu_t vcpu, hv_simd_fp_reg_t reg, hv_simd_fp_uchar16_t *value);
```

#### Return Value

[`HV_SUCCESS`](./hv_success.md) if the operation was successful, otherwise an error code specified in [`hv_return_t`](./hv_return_t.md).

#### Discussion

> ❗ **Important**:  This function must be called by the owning thread.

## Parameters

- `vcpu`: The vCPU instance.
- `reg`: The ID of the SIMD and FP register.
- `value`: The value of the register `reg` on output.

## See Also

### SIMD & Floating-point registers
- [func hv_vcpu_set_simd_fp_reg(hv_vcpu_t, hv_simd_fp_reg_t, hv_simd_fp_uchar16_t) -> hv_return_t](./hv_vcpu_set_simd_fp_reg%28_,_,_%29.md)
  Sets the value of a vCPU SIMD&FP register.
- [typealias hv_simd_fp_uchar16_t](./hv_simd_fp_uchar16_t.md)
  The value that represents an ARM SIMD and FP register.
- [struct hv_simd_fp_reg_t](./hv_simd_fp_reg_t.md)
  The type that defines SIMD and floating-point registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_vcpu_get_simd_fp_reg(_:_:_:))*