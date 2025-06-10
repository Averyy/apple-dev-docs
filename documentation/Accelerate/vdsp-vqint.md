# vDSP_vqint

**Framework**: Accelerate  
**Kind**: func

Calculates single-precision vector quadratic interpolation.

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
extern void vDSP_vqint(const float * __A, const float * __B, vDSP_Stride __IB, float * __C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __M);
```

#### Discussion

Generates `C` by interpolating between neighboring values of `A` as controlled by values in `B`. The integer portion of each element in `B` is the zero-based index of the second element of a triple of adjacent values in vector `A`.

The value of the corresponding element of `C` is derived from these three values by quadratic interpolation, using the fractional part of the value in `B`. The calculation is equivalent to the following pseudocode:

```objc
for (n = 0; n < N; ++n)
{
    b = max(trunc(B[n]), 1);
    a = B[n] - b;
    C[n] = (A[b-1]*(a**2-a)
           + A[b]*(2-2*a**2)
           + A[b+1]*(a**2+a))
           / 2;
}
```

Argument `M` is not used in the calculation. However, the integer parts of the values in `B` must be less than or equal to `M` - 2.

## Parameters

- `__A`: Single-precision real input vector with a stride of 1.
- `__B`: Single-precision real input vector. Integer parts are indices into   and fractional parts are interpolation constants
- `__IB`: Stride for  .
- `__C`: Single-precision real output vector.
- `__IC`: Stride for  .
- `__N`: Count for  .
- `__M`: Length of  . Must be greater than or equal to 3.

## See Also

- [vDSP_vqintD](vdsp_vqintd.md)
  Calculates double-precision vector quadratic interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vqint)*