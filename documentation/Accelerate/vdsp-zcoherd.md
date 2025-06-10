# vDSP_zcoherD

**Framework**: Accelerate  
**Kind**: func

Computes the coherence function of two double-precision vectors.

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
extern void vDSP_zcoherD(const double * __A, const double * __B, const DSPDoubleSplitComplex * __C, double * __D, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_zcoher`](vdsp_zcoher.md), except for the types of vectors `A`, `B`, `C`, and `D`.

## See Also

- [vDSP_zcoher](vdsp_zcoher.md)
  Computes the coherence function of two single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zcoherd)*