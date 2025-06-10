# vDSP_zvdiv

**Framework**: Accelerate  
**Kind**: func

Divides two complex single-precision vectors.

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
extern void vDSP_zvdiv(const DSPSplitComplex * __B, vDSP_Stride __IB, const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function divides the first `N` elements of `A` by corresponding elements of `B`, leaving the result in `C`.

![None](https://docs-assets.developer.apple.com/published/297413dd5127448921730cc9d5e07d31/media-3110562%402x.png)

The operation is:

```swift
for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

## Parameters

- `__B`: Single-precision complex input vector. Note that   comes before  !
- `__IB`: Stride for  .
- `__A`: Single-precision complex input vector.
- `__IA`: Stride for  .
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_zvdivD](vdsp_zvdivd.md)
  Divides two complex double-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvdiv)*