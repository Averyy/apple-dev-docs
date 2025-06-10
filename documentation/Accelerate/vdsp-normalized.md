# vDSP_normalizeD

**Framework**: Accelerate  
**Kind**: func

Computes double-precision mean and standard deviation, and then calculates new elements to have a zero mean and a unit standard deviation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_normalizeD(const double * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, double * __Mean, double * __StandardDeviation, vDSP_Length __N);
```

#### Discussion

This is the same as [`vDSP_normalize`](vdsp_normalize.md), except for the types of `A`, `C`, `Mean`, and `StandardDeviation`.

## See Also

- [vDSP_normalize](vdsp_normalize.md)
  Computes single-precision mean and standard deviation, and then calculates new elements to have a zero mean and a unit standard deviation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_normalized)*