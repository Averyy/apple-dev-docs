# vDSP_zvmgsaD

**Framework**: Accelerate  
**Kind**: func

Complex vector magnitudes square and add; double precision.

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
extern void vDSP_zvmgsaD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_zvmgsa`](vdsp_zvmgsa.md), except for the types of vectors `A`, `B`, and `C`.

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
- [vDSP_zvmgsa](vdsp_zvmgsa.md)
  Complex vector magnitudes square and add; single precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvmgsad)*