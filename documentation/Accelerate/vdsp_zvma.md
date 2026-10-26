# vDSP_zvma

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Adds a single-precision complex vector to the product of two single-precision complex vectors.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_zvma(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__B, vDSP_Stride __IB, const DSPSplitComplex *__C, vDSP_Stride __IC, const DSPSplitComplex *__D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function multiplies the first `N` complex elements of `A` by the corresponding complex elements of `B`, adds each product to the corresponding value in `C`, and writes the result to `D`:

![A diagram showing the operation of the vDSP_zvma function. There are five rows. The top two rows represents the first two inputs, vector A and vector B. The third row represents the intermediate result of the first two inputs. The forth row represents the third input, vector C. The bottom row represents the output, vector D. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3110565@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B[n] + C[n];
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for the `A`.
- `__B`: Single-precision complex input vector.
- `__IB`: Stride for `B`.
- `__C`: Single-precision complex input vector.
- `__IC`: Stride for `C`.
- `__D`: Single-precision complex output vector.
- `__ID`: Stride for `D`.
- `__N`: Number of elements to process in each of the input and output vectors.

## See Also

### Ternary Multiply-Add Operations
- [vDSP_zvmaD](./vdsp_zvmad.md)
  Adds a double-precision complex vector to the product of two double-precision complex vectors.
- [vDSP_zvsma](./vdsp_zvsma.md)
  Calculates the single-precision element-wise addition of the product of a complex vector and a complex scalar value, and a complex vector, using the specified stride.
- [vDSP_zvsmaD](./vdsp_zvsmad.md)
  Calculates the double-precision element-wise addition of the product of a complex vector and a complex scalar value, and a complex vector, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvma)*