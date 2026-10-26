# vDSP_vqintD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates double-precision vector quadratic interpolation.

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
extern void vDSP_vqintD(const double *__A, const double *__B, vDSP_Stride __IB, double *__C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __M);
```

#### Discussion

This function is the same as [`vDSP_vqint`](./vdsp_vqint.md), except for the types of vectors `A`, `B`, and `C`.

This example uses `a` as the lookup table `[0, 10, 40, 90]` (samples of `10·x²`) and `b` as fractional indices. The function fits a parabola through each triple of neighboring table entries and evaluates it at the fractional position, so index `1.5` gives `22.5`, producing `[10, 22.5, 40, 62.5]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [0, 10, 40, 90]
var b: [Double] = [1.0, 1.5, 2.0, 2.5]
var c = [Double](repeating: 0, count: b.count)

// Quadratically interpolate values from the lookup table `a` at the fractional indices in `b`.
vDSP_vqintD(a, b, 1, &c, 1, vDSP_Length(b.count), vDSP_Length(a.count))

// Prints "[10.0, 22.5, 40.0, 62.5]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {0, 10, 40, 90};
double b[4] = {1.0, 1.5, 2.0, 2.5};
double c[4];

// Quadratically interpolate values from the lookup table `a` at the fractional indices in `b`.
vDSP_vqintD(a, b, 1, c, 1, 4, 4);

// Prints "[10, 22.5, 40, 62.5]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## See Also

### Vector-to-Vector Quadratic Interpolation
- [vDSP_vqint](./vdsp_vqint.md)
  Calculates single-precision vector quadratic interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vqintd)*