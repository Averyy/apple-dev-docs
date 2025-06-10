# vDSP_vthresD

**Framework**: Accelerate  
**Kind**: func

Calculates double-precision vector threshold with zero fill to the specified range.

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
extern void vDSP_vthresD(const double * __A, vDSP_Stride __IA, const double * __B, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_vthres`](vdsp_vthres.md), except for the types of vectors `A` and `C` and scalar `*B`.

## See Also

- [vDSP_vthres](vdsp_vthres.md)
  Calculates single-precision vector threshold with zero fill to the specified range.
- [vDSP_vthrsc](vdsp_vthrsc.md)
  Calculates single-precision vector threshold with signed constant to the specified range.
- [vDSP_vthrscD](vdsp_vthrscd.md)
  Calculates double-precision vector threshold with signed constant to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vthresd)*