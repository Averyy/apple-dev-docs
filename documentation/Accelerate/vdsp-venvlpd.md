# vDSP_venvlpD

**Framework**: Accelerate  
**Kind**: func

Calculates whether each element in a double-precision vector falls within a specified range.

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
extern void vDSP_venvlpD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, const double * __C, vDSP_Stride __IC, double * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_venvlp`](vdsp_venvlp.md), except for the types of vectors `A`, `B`, `C`, and `D`.

## See Also

- [vDSP_venvlp](vdsp_venvlp.md)
  Calculates whether each element in a single-precision vector falls within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_venvlpd)*