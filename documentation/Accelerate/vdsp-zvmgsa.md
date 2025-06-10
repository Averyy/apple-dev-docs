# vDSP_zvmgsa

**Framework**: Accelerate  
**Kind**: func

Complex vector magnitudes square and add; single precision.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zvmgsa(const DSPSplitComplex * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Adds the squared magnitudes of complex vector `A` to real vector `B` and store the results in real vector `C`.

![mathematical formula](https://docs-assets.developer.apple.com/published/0ad10ac4a9f2fee9eb11fd8c0d4953d6/media-2557728%402x.png)

where  are the real parts of `A` and  are the imaginary parts.

## Parameters

- `__A`: Single-precision complex input vector
- `__IA`: Stride for 
- `__B`: Single-precision real input vector
- `__IB`: Stride for 
- `__C`: Single-precision real output vector
- `__IC`: Stride for 
- `__N`: The number of elements to process

## See Also

- [vDSP_vsq](vdsp_vsq.md)
  Computes the squared value of each element in the supplied single-precision vector.
- [vDSP_vsqD](vdsp_vsqd.md)
  Computes the squared value of each element in the supplied double-precision vector.
- [vDSP_vssq](vdsp_vssq.md)
  Computes the signed squared value of each element in the supplied single-precision vector.
- [vDSP_vssqD](vdsp_vssqd.md)
  Computes the signed squared value of each element in the supplied double-precision vector.
- [vDSP_zvmags](vdsp_zvmags.md)
  Computes the squared magnitude value of each element in the supplied complex single-precision vector.
- [vDSP_zvmagsD](vdsp_zvmagsd.md)
  Computes the squared magnitude value of each element in the supplied complex double-precision vector.
- [vDSP_zvmgsaD](vdsp_zvmgsad.md)
  Complex vector magnitudes square and add; double precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvmgsa)*