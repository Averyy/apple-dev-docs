# vDSP_vintb

**Framework**: Accelerate  
**Kind**: func

Calculates the linear interpolation between the supplied single-precision vectors using the specified stride.

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
extern void vDSP_vintb(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const float * __C, float * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function interpolates between the first `N` elements of `A` and `B` by taking the difference between corresponding elements, multiplying it by the constant `C`, and adding this to the corresponding element of `A`; results are left in corresponding elements of `D`:

![mathematical formula](https://docs-assets.developer.apple.com/published/ebf2a42d79af172d79432307dfe488fc/media-2557779%402x.png)

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for  .
- `__B`: Single-precision real input vector.
- `__IB`: Stride for  .
- `__C`: Single-precision real input scalar: interpolation constant.
- `__D`: Single-precision real output vector.
- `__ID`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vintbD](vdsp_vintbd.md)
  Calculates the linear interpolation between the supplied double-precision vectors using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vintb)*