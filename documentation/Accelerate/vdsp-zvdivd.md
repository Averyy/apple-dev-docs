# vDSP_zvdivD

**Framework**: Accelerate  
**Kind**: func

Divides two complex double-precision vectors.

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
extern void vDSP_zvdivD(const DSPDoubleSplitComplex * __B, vDSP_Stride __IB, const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function divides the first `N` elements of `A` by corresponding elements of `B`, leaving the result in `C`.

![None](https://docs-assets.developer.apple.com/published/57c182e7513f7755d5f3f6feab0ee211/media-3213994%402x.png)

The operation is:

```swift
for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

## Parameters

- `__B`: Double-precision complex input vector. Note that   comes before  !
- `__IB`: Stride for  .
- `__A`: Double-precision complex input vector.
- `__IA`: Stride for  .
- `__C`: Double-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_zvdiv](vdsp_zvdiv.md)
  Divides two complex single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvdivd)*