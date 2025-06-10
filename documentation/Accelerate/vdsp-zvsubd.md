# vDSP_zvsubD

**Framework**: Accelerate  
**Kind**: func

Subtracts two double-precision complex vectors.

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
extern void vDSP_zvsubD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __B, vDSP_Stride __IB, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the differences of the first `N` complex elements of `A` and `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zvsub function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/d02e51e60822b05be74e985b5cb8deb3/media-3214021%402x.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] - B[n];
```

## Parameters

- `__A`: Double-precision complex input vector.
- `__IA`: Stride for  .
- `__B`: Double-precision complex input vector.
- `__IB`: Stride for  .
- `__C`: Double-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_zvsub](vdsp_zvsub.md)
  Subtracts two single-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvsubd)*