# vDSP_vtrapz

**Framework**: Accelerate  
**Kind**: func

Performs trapezoidal integration over a single-precision vector.

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
extern void vDSP_vtrapz(const float * __A, vDSP_Stride __IA, const float * __B, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Performs the following operation:

![mathematical formula](https://docs-assets.developer.apple.com/published/2eae896846e312c7347e6c8392862388/media-2557740%402x.png)

Estimates the integral of vector `A` using the trapezoidal rule. Scalar `*B` specifies the integration step size. This function can only be done out of place.

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for  .
- `__B`: Pointer to single-precision real input scalar: step size.
- `__C`: Single-precision real output vector.
- `__IC`: Address stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vtrapzD](vdsp_vtrapzd.md)
  Performs trapezoidal integration over a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vtrapz)*