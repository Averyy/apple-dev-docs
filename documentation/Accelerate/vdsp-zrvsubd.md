# vDSP_zrvsubD

**Framework**: Accelerate  
**Kind**: func

Subtracts a double-precision real vector from a double-precision complex vector.

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
extern void vDSP_zrvsubD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function subtracts the first `N` real elements of `B` from corresponding complex elements of `A`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zrvsub function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/d02e51e60822b05be74e985b5cb8deb3/media-3213990%402x.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] - B[n];
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

- [vDSP_zrvsub](vdsp_zrvsub.md)
  Subtracts a single-precision real vector from a single-precision complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zrvsubd)*