# hv_simd_fp_uchar16_t

**Framework**: Hypervisor  
**Kind**: typealias

The value that represents an ARM SIMD and FP register.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias hv_simd_fp_uchar16_t = SIMD16<UInt8>
```

## See Also

- [func hv_vcpu_get_simd_fp_reg(hv_vcpu_t, hv_simd_fp_reg_t, UnsafeMutablePointer<hv_simd_fp_uchar16_t>) -> hv_return_t](hv_vcpu_get_simd_fp_reg(_:_:_:).md)
  Gets the current value of a vCPU SIMD and FP register.
- [func hv_vcpu_set_simd_fp_reg(hv_vcpu_t, hv_simd_fp_reg_t, hv_simd_fp_uchar16_t) -> hv_return_t](hv_vcpu_set_simd_fp_reg(_:_:_:).md)
  Sets the value of a vCPU SIMD&FP register.
- [struct hv_simd_fp_reg_t](hv_simd_fp_reg_t.md)
  The type that defines SIMD and floating-point registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_simd_fp_uchar16_t)*