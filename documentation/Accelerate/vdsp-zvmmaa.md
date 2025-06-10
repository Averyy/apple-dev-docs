# vDSP_zvmmaa

**Framework**: Accelerate  
**Kind**: func

Adds a single-precision complex vector to the sum of the product of two single-precision complex vectors and a second product of two single-precision complex vectors.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zvmmaa(const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __B, vDSP_Stride __IB, const DSPSplitComplex * __C, vDSP_Stride __IC, const DSPSplitComplex * __D, vDSP_Stride __ID, const DSPSplitComplex * __E, vDSP_Stride __IE, const DSPSplitComplex * __F, vDSP_Stride __IF, vDSP_Length __N);
```

#### Discussion

This function calculates the products of the first `N` complex elements of `A` and `B`, the products of the first `N` compex elements of `C` and `D`, adds the corresponding products, adds the first `N` complex elements of `E`, and writes the result to `F`:

![A diagram showing the operation of the vDSP_zvmmaa function. There are five rows and the top four rows are composed of two columns. The top two rows of the left column represent the input vectors A and B. The top two rows of the right column represent the input vectors C and D. The third row in both columns represent the intermediate result of the respective inputs. The left column of the forth row represents the intermediate result of adding the two products, and the right column of the forth row represnets input vector E. The bottom row represents the output vector, F. The diagram has connecting lines from the inputs to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/f76d49c4985d57b0527e80b505a7aa97/media-3110564%402x.png)

The operation is:

```swift
for (n = 0; n < N; ++n)
    F[n] = A[n] * B[n] + C[n] * D[n] + E[n];
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for first input vector.
- `__B`: Single-precision complex second input vector.
- `__IB`: Stride for second input vector.
- `__C`: Single-precision complex third input vector.
- `__IC`: Stride for third input vector.
- `__D`: SIngle-precision complex fourth input vector.
- `__ID`: Stride for fourth input vector.
- `__E`: Single-precision complex fifth input vector.
- `__IE`: Stride for fifth input vector.
- `__F`: Single-precision complex  output vector.
- `__IF`: Stride for output vector.
- `__N`: Number of elements to process in each vector.

## See Also

- [vDSP_zvmmaaD](vdsp_zvmmaad.md)
  Adds a double-precision complex vector to the sum of the product of two double-precision complex vectors and a second product of two double-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvmmaa)*