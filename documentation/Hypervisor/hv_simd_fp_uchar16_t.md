# hv_simd_fp_uchar16_t

**Framework**: Hypervisor  
**Kind**: typealias  
**Role**: Type Alias

The value that represents an ARM SIMD and FP register.

**Availability**:
- macOS

## Declaration

```swift
typealias hv_simd_fp_uchar16_t = SIMD16<UInt8>
```

```c
typedef unsigned char __attribute__((ext_vector_type(16))) hv_simd_fp_uchar16_t;
```

## See Also

### SIMD & Floating-point registers
- [func hv_vcpu_get_simd_fp_reg(hv_vcpu_t, hv_simd_fp_reg_t, UnsafeMutablePointer<hv_simd_fp_uchar16_t>) -> hv_return_t](./hv_vcpu_get_simd_fp_reg%28_,_,_%29.md)
  Gets the current value of a vCPU SIMD and FP register.
- [func hv_vcpu_set_simd_fp_reg(hv_vcpu_t, hv_simd_fp_reg_t, hv_simd_fp_uchar16_t) -> hv_return_t](./hv_vcpu_set_simd_fp_reg%28_,_,_%29.md)
  Sets the value of a vCPU SIMD&FP register.
- [struct hv_simd_fp_reg_t](./hv_simd_fp_reg_t.md)
  The type that defines SIMD and floating-point registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_simd_fp_uchar16_t)*