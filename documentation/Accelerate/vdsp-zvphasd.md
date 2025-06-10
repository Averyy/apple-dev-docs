# vDSP_zvphasD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision element-wise phase values, in radians, of the supplied complex vector using the specified stride.

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
extern void vDSP_zvphasD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_zvphas`](vdsp_zvphas.md), except for the types of vectors `A` and `C`.

## See Also

- [vDSP_zvphas](vdsp_zvphas.md)
  Calculates the single-precision element-wise phase values, in radians, of the supplied complex vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvphasd)*