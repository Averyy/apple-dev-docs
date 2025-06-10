# vDSP_vtrapzD

**Framework**: Accelerate  
**Kind**: func

Performs trapezoidal integration over a double-precision vector.

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
extern void vDSP_vtrapzD(const double * __A, vDSP_Stride __IA, const double * __B, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_vtrapz`](vdsp_vtrapz.md), except for the types of vectors `A` and `C` and scalar `*B`.

## See Also

- [vDSP_vtrapz](vdsp_vtrapz.md)
  Performs trapezoidal integration over a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vtrapzd)*