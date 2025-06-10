# vDSP_venvlp

**Framework**: Accelerate  
**Kind**: func

Calculates whether each element in a single-precision vector falls within a specified range.

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
extern void vDSP_venvlp(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const float * __C, vDSP_Stride __IC, float * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

Finds the extrema of `C`. For the first `N` elements of `C`, the corresponding element of `A` provides an upper-threshold value, and the corresponding element of `B` provides a  lower-threshold value. If the value of an element of `C` falls outside the range defined by these thresholds, it is copied to the corresponding element of `D`. If its value is within the range, the corresponding element of `D` is set to zero:

![mathematical formula](https://docs-assets.developer.apple.com/published/eef54ab339547f4d43088ea9c2e7d3f8/media-2557782%402x.png)

## Parameters

- `__A`: Single-precision real input vector: high envelope.
- `__IA`: Stride for  .
- `__B`: Single-precision real input vector: low envelope.
- `__IB`: Stride for  .
- `__C`: Single-precision real input vector.
- `__IC`: Stride for  .
- `__D`: Single-precision real output vector.
- `__ID`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_venvlpD](vdsp_venvlpd.md)
  Calculates whether each element in a double-precision vector falls within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_venvlp)*