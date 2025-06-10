# vDSP_vminD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision minimum of the corresponding values of two vectors using specified strides.

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
extern void vDSP_vminD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function compares the first `N` elements of `A` with corresponding elements of `B`, leaving the lesser (or equal) values as corresponding elements of `C`:

```c
for (n = 0; n < N; ++n)
    C[n] = A[n] <= B[n] ? A[n] : B[n];
```

## Parameters

- `__A`: Double-precision real input vector.
- `__IA`: Stride for  .
- `__B`: Double-precision real input vector.
- `__IB`: Stride for  .
- `__C`: Double-precision real output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vmin](vdsp_vmin.md)
  Calculates the single-precision minimum of the corresponding values of two vectors using specified strides.
- [vDSP_vminmg](vdsp_vminmg.md)
  Calculates the single-precision minimum magnitude of the corresponding values of two vectors using specified strides.
- [vDSP_vminmgD](vdsp_vminmgd.md)
  Calculates the double-precision minimum magnitude of the corresponding values of two vectors using specified strides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vmind)*