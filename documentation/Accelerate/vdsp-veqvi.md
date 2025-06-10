# vDSP_veqvi

**Framework**: Accelerate  
**Kind**: func

Calculates bitwise logical equivalence of two integer vectors.

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
extern void vDSP_veqvi(const int * __A, vDSP_Stride __IA, const int * __B, vDSP_Stride __IB, int * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the bitwise logical equivalence of the first `N` elements of `A` and `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_veqvi function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/81aa154786fbc7cf499aa374638ba04f/media-3111142%402x.png)

The operation is:

```swift
for (n = 0; n < N; ++n)
    C[n] = ~(A[n] ^ B[n]);
```

The following code shows an example of using [`vDSP_veqvi`](vdsp_veqvi.md):

```swift
let stride = vDSP_Stride(1)

let a: [Int32] = [0, 0, 1, 1]
let b: [Int32] = [0, 1, 0, 1]

let n = vDSP_Length(a.count)

var c = [Int32](repeating: 0,
                count: a.count)

vDSP_veqvi(b, stride,
           a, stride,
           &c, stride,
           n)

// Prints "[-1, -2, -2, -1]"
print(c)
```

## Parameters

- `__A`: Integer input vector.
- `__IA`: Stride for  .
- `__B`: Integer input vector.
- `__IB`: Stride for  .
- `__C`: Integer output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vaddi](vdsp_vaddi.md)
  Adds two integer vectors.
- [vDSP_vdivi](vdsp_vdivi.md)
  Divides two integer vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_veqvi)*