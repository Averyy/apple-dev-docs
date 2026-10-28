# vDSP_zrvmulD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Multiplies a double-precision complex vector by a double-precision real vector.

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
extern void vDSP_zrvmulD(const DSPDoubleSplitComplex *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function calculates the products of the first `N` complex elements of `A` to the corresponding real elements of `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zrvadd function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3213977@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] * B[n];
```

## Parameters

- `__A`: Double-precision complex input vector.
- `__IA`: Stride for `IA`.
- `__B`: Double-precision real input vector.
- `__IB`: Stride for `B`.
- `__C`: Double-precision complex output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Binary (Complex-Real) Multiplication Operations
- [vDSP_zrvmul](./vdsp_zrvmul.md)
  Multiplies a single-precision complex vector by a single-precision real vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zrvmuld)*