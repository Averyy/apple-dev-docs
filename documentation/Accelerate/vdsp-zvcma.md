# vDSP_zvcma

**Framework**: Accelerate  
**Kind**: func

Adds a single-precision complex vector to the product of a single-precision complex vector and the conjugate of another complex single-precision vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zvcma(const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __B, vDSP_Stride __IB, const DSPSplitComplex * __C, vDSP_Stride __IC, const DSPSplitComplex * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function multiplies of the first `N` complex conjugates of `A` by the corresponding complex elements of `B`, adds each product to the corresponding value in `C`, and writes the result to `D`:

![A diagram showing the operation of the vDSP_zvcma function. The top row represents the first input, vector A. The second row represents the second input, vector B. The third row represents the product of the elements of vectors A and B. The forth row represents the third input, C. The fifth row represents the sum of the products and elements of C.](https://docs-assets.developer.apple.com/published/c5f4089484f91aa0fce6b95c8b8af3b8/media-3214023%402x.png)

The operation is:

```swift
for (n = 0; n < N; ++n)
      D[n] = conj(A[n]) * B[n] + C[n];
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for  .
- `__B`: Single-precision complex input vector.
- `__IB`: Stride for  .
- `__C`: Single-precision complex input vector.
- `__IC`: Stride for  .
- `__D`: Single-precision complex output vector.
- `__ID`: Stride for  .
- `__N`: Number of elements.

## See Also

- [vDSP_zvcmaD](vdsp_zvcmad.md)
  Adds a double-precision complex vector to the product of a double-precision complex vector and the conjugate of another complex double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvcma)*