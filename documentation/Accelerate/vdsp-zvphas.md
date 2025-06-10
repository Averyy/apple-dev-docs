# vDSP_zvphas

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision element-wise phase values, in radians, of the supplied complex vector using the specified stride.

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
extern void vDSP_zvphas(const DSPSplitComplex * __A, vDSP_Stride __IA, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Finds the phase values, in radians, of complex vector `A` and store the results in real vector `C`. The results are between -pi and +pi. The sign of the result is the sign of the second coordinate in the input vector, except that the `vDSP_zvphas` function does not necessarily respect the sign of a zero input.

This performs the following operation:

```objc
for (n = 0; n < N; ++n)
   C[n] = atan2(Im(A[n]), Re(A[n]));
```

> **Note**:  If both the inputs are `+0` or `-0`, the vDSP_zvphas function may return any value in `[-pi, +pi]`. If only one input is zero, the vDSP_zvphas function may return the result atan2 returns when the corresponding input is `+0` or `-0`.

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for  .
- `__C`: Single-precision real output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_zvphasD](vdsp_zvphasd.md)
  Calculates the double-precision element-wise phase values, in radians, of the supplied complex vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvphas)*