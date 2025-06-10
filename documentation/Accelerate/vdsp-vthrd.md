# vDSP_vthrD

**Framework**: Accelerate  
**Kind**: func

Calculates double-precision vector threshold to the specified range.

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
extern void vDSP_vthrD(const double * __A, vDSP_Stride __IA, const double * __B, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_vthr`](vdsp_vthr.md), except for the types of vectors `A` and `C`, and scalar `*B`.

## See Also

- [vDSP_vclip](vdsp_vclip.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipD](vdsp_vclipd.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [vDSP_vclipc](vdsp_vclipc.md)
  Calculates and counts the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipcD](vdsp_vclipcd.md)
  Calculates and counts the elements of a double-precision vector clipped to the specified range.
- [vDSP_viclip](vdsp_viclip.md)
  Calculates the elements of a single-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_viclipD](vdsp_viclipd.md)
  Calculates the elements of a double-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_vthr](vdsp_vthr.md)
  Calculates single-precision vector threshold to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vthrd)*