# vDSP_sve

**Framework**: Accelerate  
**Kind**: func

Calculates the sum of values in a single-precision vector.

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
extern void vDSP_sve(const float * __A, vDSP_Stride __I, float * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the sum of the first `N` elements of `A` and writes the result to `C`:

![A diagram showing the operation of the vDSP_sve function. There are three rows. The top row represents the input, vector A. The second row represents the summation operation. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://docs-assets.developer.apple.com/published/7d7fe867386f9f5fcb1aca5718af0765/media-3111277%402x.png)

The operation is:

```c
C[0] = sum(A[n], 0 <= n < N);
```

The following code shows an example of using [`vDSP_sve`](vdsp_sve.md):

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c: Float = .nan

vDSP_sve(a,
         stride,
         &c,
         n)

// Prints "sum 0.1500"
print(String(format: "sum %.4f", c))
```

## Parameters

- `__A`: Single-precision real input vector.
- `__I`: Stride for  .
- `__C`: Single-precision real output scalar.
- `__N`: The number of elements to process.

## See Also

- [vDSP_sveD](vdsp_sved.md)
  Calculates the sum of values in a double-precision vector.
- [vDSP_svemg](vdsp_svemg.md)
  Calculates the sum of magnitudes in a single-precision vector.
- [vDSP_svemgD](vdsp_svemgd.md)
  Calculates the sum of magnitudes in a double-precision vector.
- [vDSP_svesq](vdsp_svesq.md)
  Calculates the sum of squares in a single-precision vector.
- [vDSP_svesqD](vdsp_svesqd.md)
  Calculates the sum of squares in a double-precision vector.
- [vDSP_sve_svesq](vdsp_sve_svesq.md)
  Calculates the sum of values and the sum of squares in a single-precision vector.
- [vDSP_sve_svesqD](vdsp_sve_svesqd.md)
  Calculates the sum of values and the sum of squares in a double-precision vector.
- [vDSP_svs](vdsp_svs.md)
  Calculates the sum of signed squares in a single-precision vector.
- [vDSP_svsD](vdsp_svsd.md)
  Calculates the sum of signed squares in a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_sve)*