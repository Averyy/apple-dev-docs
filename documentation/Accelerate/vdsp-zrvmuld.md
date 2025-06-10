# vDSP_zrvmulD

**Framework**: Accelerate  
**Kind**: func

Multiplies a double-precision complex vector by a double-precision real vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zrvmulD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the products of the first `N` complex elements of `A` to the corresponding real elements of `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zrvadd function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/eac5aa3ca544001f7cdab42784467389/media-3213977%402x.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] * B[n];
```

## Parameters

- `__A`: Double-precision complex input vector.
- `__IA`: Stride for  .
- `__B`: Double-precision real input vector.
- `__IB`: Stride for  .
- `__C`: Double-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_zrvmul](vdsp_zrvmul.md)
  Multiplies a single-precision complex vector by a single-precision real vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zrvmuld)*