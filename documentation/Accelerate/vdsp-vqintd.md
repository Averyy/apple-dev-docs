# vDSP_vqintD

**Framework**: Accelerate  
**Kind**: func

Calculates double-precision vector quadratic interpolation.

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
extern void vDSP_vqintD(const double * __A, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __M);
```

#### Discussion

This function is the same as [`vDSP_vqint`](vdsp_vqint.md), except for the types of vectors `A`, `B`, and `C`.

## See Also

- [vDSP_vqint](vdsp_vqint.md)
  Calculates single-precision vector quadratic interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vqintd)*