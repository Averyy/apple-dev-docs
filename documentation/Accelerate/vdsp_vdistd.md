# vDSP_vdistD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of two pairs of vectors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_vdistD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The [`vDSP_vdist`](./vdsp_vdist.md) and [`vDSP_vdistD`](./vdsp_vdistd.md) functions calculate the square roots of the sum of the squares of corresponding elements of vectors `A` and `B`, using the following operation:

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

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [3, 5, 8]
var b: [Double] = [4, 12, 15]
var c = [Double](repeating: 0, count: a.count)

// Calculate the hypotenuse of a right triangle with legs `a[i]` and `b[i]`.
vDSP_vdistD(a, 1, b, 1, &c, 1, vDSP_Length(a.count))

// Prints "[5.0, 13.0, 17.0]".
print(c)
```

**Objective-C**:

```objc
double a[3] = {3, 5, 8};
double b[3] = {4, 12, 15};
double c[3];

// Calculate the hypotenuse of a right triangle with legs `a[i]` and `b[i]`.
vDSP_vdistD(a, 1, b, 1, c, 1, 3);

// Prints "[5, 13, 17]".
printf("[%g, %g, %g]\n", c[0], c[1], c[2]);
```

## Parameters

- `__A`: A vector that contains the lengths of the first set of legs of the triangles.
- `__IA`: The distance between the elements in the input vector `A`.
- `__B`: A vector that contains the lengths of the second set of legs of the triangles.
- `__IB`: The distance between the elements in the input vector `B`.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector `C`.
- `__N`: The number of elements to process.

## See Also

### Vector distance computation
- [vDSP_vdist](./vdsp_vdist.md)
  Calculates the single-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of two pairs of vectors.
- [vDSP_distancesq](./vdsp_distancesq.md)
  Calculates the single-precision distance squared between two points in n-dimensional space.
- [vDSP_distancesqD](./vdsp_distancesqd.md)
  Calculates the double-precision distance squared between two points in n-dimensional space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vdistd)*