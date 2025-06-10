# vDSP_vrsum

**Framework**: Accelerate  
**Kind**: func

Performs running sum integration over a single-precision vector.

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
extern void vDSP_vrsum(const float * __A, vDSP_Stride __IA, const float * __S, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Performs the following operation:

![mathematical formula](https://docs-assets.developer.apple.com/published/7f5bbf226b2a3bb27003c1cf42a5220a/media-2557738%402x.png)

Integrates vector `A` using a running sum from vector `C`. Vector `A` is weighted by scalar `*S` and added to the previous output point. The first element  from vector `A` is not used in the sum.

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for  .
- `__S`: Points to single-precision real input scalar: weighting factor.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for 
- `__N`: The number of elements to process.

## See Also

- [vDSP_vrsumD](vdsp_vrsumd.md)
  Performs running sum integration over a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrsum)*