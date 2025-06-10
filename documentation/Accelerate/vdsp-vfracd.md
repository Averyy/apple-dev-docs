# vDSP_vfracD

**Framework**: Accelerate  
**Kind**: func

Truncates the elements of a double-precision vector to fractions.

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
extern void vDSP_vfracD(const double * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_vfrac`](vdsp_vfrac.md), except for the types of vectors `A` and C.

## See Also

- [vDSP_vfrac](vdsp_vfrac.md)
  Truncates the elements of a single-precision vector to fractions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfracd)*