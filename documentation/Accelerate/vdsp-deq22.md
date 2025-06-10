# vDSP_deq22

**Framework**: Accelerate  
**Kind**: func

Performs two-pole two-zero recursive filtering on a single-precision vector.

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
extern void vDSP_deq22(const float * __A, vDSP_Stride __IA, const float * __B, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function creates `N` new values in output vector `C`,  beginning with its third element. It performs two-pole two-zero recursive filtering on input vector `A`, which must contain at least `N` + 2 values; `C` must also contain at least `N` + 2 values.  Since the computation is recursive, the first two elements in `C` must be  initialized prior to calling this function. This function can only be done out of place.

![mathematical formula](https://docs-assets.developer.apple.com/published/7000eb8d07bbbbf865f8b7e4d091234f/media-2557789%402x.png)

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for  .
- `__B`: 5 single-precision inputs (filter coefficients), with stride 1.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for  .
- `__N`: Number of new output elements to produce.

## See Also

- [vDSP_deq22D](vdsp_deq22d.md)
  Performs two-pole two-zero recursive filtering on a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_deq22)*