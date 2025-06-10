# vDSP_vdistD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of two pairs of vectors.

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
extern void vDSP_vdistD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The [`vDSP_vdist`](vdsp_vdist.md) and [`vDSP_vdistD`](vdsp_vdistd.md) functions calculate the square roots of the sum of the squares of corresponding elements of vectors `A` and `B`, using the following operation:

```objc
for (n = 0; n < N; ++n)
    C[n] = sqrt(A[n]*A[n] + B[n]*B[n]);
```

For example, the following code calculates the hypotenuse of four Pythagorean triples:

```swift
let a: [Float] = [3, 6, 5, 9]
let b: [Float] = [4, 8, 12, 12]

var c: [Float] = [0, 0, 0, 0]

let stride = vDSP_Stride(1)

vDSP_vdist(a, stride,
           b, stride,
           &c, stride,
           vDSP_Length(c.count))
```

On return, `c` contains `[5.0, 10.0, 13.0, 15.0]`.

## Parameters

- `__A`: A vector that contains the lengths of the first set of legs of the triangles.
- `__IA`: The distance between the elements in the input vector  .
- `__B`: A vector that contains the lengths of the second set of legs of the triangles.
- `__IB`: The distance between the elements in the input vector  .
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vdist](vdsp_vdist.md)
  Calculates the single-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of two pairs of vectors.
- [vDSP_distancesq](vdsp_distancesq.md)
  Calculates the single-precision distance squared between two points in n-dimensional space.
- [vDSP_distancesqD](vdsp_distancesqd.md)
  Calculates the double-precision distance squared between two points in n-dimensional space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vdistd)*