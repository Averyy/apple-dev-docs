# vDSP_zvmulD

**Framework**: Accelerate  
**Kind**: func

Multiplies a double-precision complex vector by the optionally conjugate of another double-precision complex vector.

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
extern void vDSP_zvmulD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __B, vDSP_Stride __IB, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N, int __Conjugate);
```

#### Discussion

This function calculates the products of the first `N` complex (optionally conjugates) of `A` by the corresponding complex elements of `B`, writing the result to `C`:

With `Conjugate` set to `+1`:

![A diagram showing the operation of the vDSP_zvmul function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/eac5aa3ca544001f7cdab42784467389/media-3213997%402x.png)

With `Conjugate` set to -`1`:

![A diagram showing the operation of the vDSP_zvmul function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/2a2adf7c67479061e9f22cdeb3661be9/media-3214013%402x.png)

The operation is:

```swift
If Conjugate is +1:

    for (n = 0; n < N; ++n)
        C[n] = A[n] * B[n];

If Conjugate is -1:

    for (n = 0; n < N; ++n)
        C[n] = conj(A[n]) * B[n];
```

## Parameters

- `__A`: Double-precision complex input vector.
- `__IA`: Stride for  .
- `__B`: Double-precision complex input vector.
- `__IB`: Stride for  .
- `__C`: Double-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.
- `__Conjugate`: Specifies whether to use conjugate for  .

## See Also

- [vDSP_zvmul](vdsp_zvmul.md)
  Multiplies a single-precision complex vector by the optionally conjugate of another single-precision complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvmuld)*