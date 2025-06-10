# vDSP_vmaxD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision maximum of the corresponding values of two vectors using specified strides.

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
extern void vDSP_vmaxD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function compares the first `N` elements of `A` with corresponding elements of `B`, leaving the greater (or equal) values as corresponding elements of `C`:

```c
for (n = 0; n < N; ++n)
    C[n] = B[n] <= A[n] ? A[n] : B[n];
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

- [vDSP_vmax](vdsp_vmax.md)
  Calculates the single-precision maximum of the corresponding values of two vectors using specified strides.
- [vDSP_vmaxmg](vdsp_vmaxmg.md)
  Calculates the single-precision maximum magnitude of the corresponding values of two vectors using specified strides.
- [vDSP_vmaxmgD](vdsp_vmaxmgd.md)
  Calculates the double-precision maximum magnitude of the corresponding values of two vectors using specified strides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vmaxd)*