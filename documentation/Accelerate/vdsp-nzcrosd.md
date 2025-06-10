# vDSP_nzcrosD

**Framework**: Accelerate  
**Kind**: func

Counts and finds the zero crossings in a double-precision vector.

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
extern void vDSP_nzcrosD(const double * __A, vDSP_Stride __IA, vDSP_Length __B, vDSP_Length * __C, vDSP_Length * __D, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_nzcros`](vdsp_nzcros.md), except for the type of the input vector.

## See Also

- [vDSP_nzcros](vdsp_nzcros.md)
  Counts and finds the zero crossings in a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_nzcrosd)*