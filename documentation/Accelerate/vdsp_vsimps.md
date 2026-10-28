# vDSP_vsimps

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs Simpson integration over a single-precision vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_vsimps(const float *__A, vDSP_Stride __IA, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

Performs the following operation:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557739@2x.png)

Integrates vector `A` using Simpson integration, storing results in vector `C`. Scalar `*B` specifies the  integration step size. This function can only be done out of place.

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for `A`.
- `__B`: Pointer to single-precision real input scalar.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for `C`
- `__N`: The number of elements to process.

## See Also

### Simpson Integration
- [vDSP_vsimpsD](./vdsp_vsimpsd.md)
  Performs Simpson integration over a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsimps)*