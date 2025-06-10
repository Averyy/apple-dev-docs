# vDSP_zvmaD

**Framework**: Accelerate  
**Kind**: func

Adds a double-precision complex vector to the product of two double-precision complex vectors.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zvmaD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __B, vDSP_Stride __IB, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, const DSPDoubleSplitComplex * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function multiplies the first `N` complex elements of `A` by the corresponding complex elements of `B`, adds each product to the corresponding value in `C`, and writes the result to `D`:

![A diagram showing the operation of the vDSP_zvma function. There are five rows. The top two rows represents the first two inputs, vector A and vector B. The third row represents the intermediate result of the first two inputs. The forth row represents the third input, vector C. The bottom row represents the output, vector D. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/493dec4716baeb680cd0bfcf23c1f4b8/media-3214016%402x.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B[n] + C[n];
```

## Parameters

- `__A`: Double-precision complex input vector.
- `__IA`: Stride for the  .
- `__B`: Double-precision complex input vector.
- `__IB`: Stride for  .
- `__C`: Double-precision complex input vector.
- `__IC`: Stride for  .
- `__D`: Double-precision complex output vector.
- `__ID`: Stride for  .
- `__N`: Number of elements to process in each of the input and output vectors.

## See Also

- [vDSP_zvma](vdsp_zvma.md)
  Adds a single-precision complex vector to the product of two single-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvmad)*