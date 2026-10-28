# vDSP_zvdiv

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Divides two complex single-precision vectors.

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
extern void vDSP_zvdiv(const DSPSplitComplex *__B, vDSP_Stride __IB, const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function divides the first `N` elements of `A` by corresponding elements of `B`, leaving the result in `C`.

![](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3110562@2x.png)

The operation is:

```c
for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

## Parameters

- `__B`: Single-precision complex input vector. Note that `B` comes before `A`!
- `__IB`: Stride for `B`.
- `__A`: Single-precision complex input vector.
- `__IA`: Stride for `A`.
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Binary Division Operations
- [vDSP_zvdivD](./vdsp_zvdivd.md)
  Divides two complex double-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvdiv)*