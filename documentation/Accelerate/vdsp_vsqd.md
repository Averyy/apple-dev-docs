# vDSP_vsqD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes the squared value of each element in the supplied double-precision vector.

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
extern void vDSP_vsqD(const double *__A, vDSP_Stride __IA, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_vsq`](./vdsp_vsq.md), except for the types of vectors `A` and `C`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-2, -0.5, 0.5, 3]
var c = [Double](repeating: 0, count: a.count)

// Square each element of `a`.
vDSP_vsqD(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[4.0, 0.25, 0.25, 9.0]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {-2, -0.5, 0.5, 3};
double c[4];

// Square each element of `a`.
vDSP_vsqD(a, 1, c, 1, 4);

// Prints "[4, 0.25, 0.25, 9]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## See Also

### Single-Vector Squaring
- [vDSP_vsq](./vdsp_vsq.md)
  Computes the squared value of each element in the supplied single-precision vector.
- [vDSP_vssq](./vdsp_vssq.md)
  Computes the signed squared value of each element in the supplied single-precision vector.
- [vDSP_vssqD](./vdsp_vssqd.md)
  Computes the signed squared value of each element in the supplied double-precision vector.
- [vDSP_zvmags](./vdsp_zvmags.md)
  Computes the squared magnitude value of each element in the supplied complex single-precision vector.
- [vDSP_zvmagsD](./vdsp_zvmagsd.md)
  Computes the squared magnitude value of each element in the supplied complex double-precision vector.
- [vDSP_zvmgsa](./vdsp_zvmgsa.md)
  Complex vector magnitudes square and add; single precision.
- [vDSP_zvmgsaD](./vdsp_zvmgsad.md)
  Complex vector magnitudes square and add; double precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsqd)*