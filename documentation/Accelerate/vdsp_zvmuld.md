# vDSP_zvmulD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Multiplies a double-precision complex vector by the optionally conjugate of another double-precision complex vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_zvmulD(const DSPDoubleSplitComplex *__A, vDSP_Stride __IA, const DSPDoubleSplitComplex *__B, vDSP_Stride __IB, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N, int __Conjugate);
```

#### Discussion

This function calculates the products of the first `N` complex (optionally conjugates) of `A` by the corresponding complex elements of `B`, writing the result to `C`:

With `Conjugate` set to `+1`:

![A diagram showing the operation of the vDSP_zvmul function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3213997@2x.png)

With `Conjugate` set to -`1`:

![A diagram showing the operation of the vDSP_zvmul function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3214013@2x.png)

The operation is:

```c
If Conjugate is +1:

    for (n = 0; n < N; ++n)
        C[n] = A[n] * B[n];

If Conjugate is -1:

    for (n = 0; n < N; ++n)
        C[n] = conj(A[n]) * B[n];
```

## Parameters

- `__A`: Double-precision complex input vector.
- `__IA`: Stride for `A`.
- `__B`: Double-precision complex input vector.
- `__IB`: Stride for `B`.
- `__C`: Double-precision complex output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.
- `__Conjugate`: Specifies whether to use conjugate for `A`.

## See Also

### Binary Optional Conjugate-Multiply Operations
- [vDSP_zvmul](./vdsp_zvmul.md)
  Multiplies a single-precision complex vector by the optionally conjugate of another single-precision complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvmuld)*