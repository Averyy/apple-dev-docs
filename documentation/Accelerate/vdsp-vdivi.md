# vDSP_vdivi

**Framework**: Accelerate  
**Kind**: func

Divides two integer vectors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vdivi(const int * __B, vDSP_Stride __IB, const int * __A, vDSP_Stride __IA, int * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the first `N` elements of `A` divided by the corresponding element in `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_vdivi function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/297413dd5127448921730cc9d5e07d31/media-3110580%402x.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

The following code shows an example of using [`vDSP_vdiv`](vdsp_vdiv.md):

```swift
let stride = vDSP_Stride(1)

let a: [Int32] = [10, 20, 30, 40, 50]
let b: [Int32] = [ 1,  2,  3,  4,  5]

let n = vDSP_Length(a.count)

var c = [Int32](repeating: 0,
                count: a.count)

vDSP_vdivi(b, stride,
           a, stride,
           &c, stride,
           n)

// Prints "[10, 10, 10, 10, 10]"
print(c)
```

## Parameters

- `__B`: Integer input vector. Note that   comes before  !
- `__IB`: Stride for  .
- `__A`: Integer input vector.
- `__IA`: Stride for  .
- `__C`: Integer output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vaddi](vdsp_vaddi.md)
  Adds two integer vectors.
- [vDSP_veqvi](vdsp_veqvi.md)
  Calculates bitwise logical equivalence of two integer vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vdivi)*