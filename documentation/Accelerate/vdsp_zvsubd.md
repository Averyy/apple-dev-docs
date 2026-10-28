# vDSP_zvsubD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Subtracts two double-precision complex vectors.

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
extern void vDSP_zvsubD(const DSPDoubleSplitComplex *__A, vDSP_Stride __IA, const DSPDoubleSplitComplex *__B, vDSP_Stride __IB, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function calculates the differences of the first `N` complex elements of `A` and `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zvsub function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3214021@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] - B[n];
```

## Parameters

- `__A`: Double-precision complex input vector.
- `__IA`: Stride for `A`.
- `__B`: Double-precision complex input vector.
- `__IB`: Stride for `B`.
- `__C`: Double-precision complex output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Binary Subtraction Operations
- [vDSP_zvsub](./vdsp_zvsub.md)
  Subtracts two single-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvsubd)*