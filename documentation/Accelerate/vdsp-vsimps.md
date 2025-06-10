# vDSP_vsimps

**Framework**: Accelerate  
**Kind**: func

Performs Simpson integration over a single-precision vector.

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
extern void vDSP_vsimps(const float * __A, vDSP_Stride __IA, const float * __B, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Performs the following operation:

![mathematical formula](https://docs-assets.developer.apple.com/published/e2e0a3c8ce0a8fb153d5be3415fd503f/media-2557739%402x.png)

Integrates vector `A` using Simpson integration, storing results in vector `C`. Scalar `*B` specifies the  integration step size. This function can only be done out of place.

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for  .
- `__B`: Pointer to single-precision real input scalar.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for 
- `__N`: The number of elements to process.

## See Also

- [vDSP_vsimpsD](vdsp_vsimpsd.md)
  Performs Simpson integration over a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsimps)*