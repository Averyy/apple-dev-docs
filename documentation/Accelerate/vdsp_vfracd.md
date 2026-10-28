# vDSP_vfracD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Truncates the elements of a double-precision vector to fractions.

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
extern void vDSP_vfracD(const double *__A, vDSP_Stride __IA, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_vfrac`](./vdsp_vfrac.md), except for the types of vectors `A` and C.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-2, -0.5, 0.5, 3]
var c = [Double](repeating: 0, count: a.count)

// Take the fractional part of each element of `a`, truncating toward zero.
vDSP_vfracD(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[0.0, -0.5, 0.5, 0.0]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {-2, -0.5, 0.5, 3};
double c[4];

// Take the fractional part of each element of `a`, truncating toward zero.
vDSP_vfracD(a, 1, c, 1, 4);

// Prints "[0, -0.5, 0.5, 0]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## See Also

### Single-Vector Fractional Part Extraction
- [vDSP_vfrac](./vdsp_vfrac.md)
  Truncates the elements of a single-precision vector to fractions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfracd)*