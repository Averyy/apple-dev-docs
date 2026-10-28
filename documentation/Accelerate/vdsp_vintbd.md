# vDSP_vintbD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the linear interpolation between the supplied double-precision vectors using the specified stride.

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
extern void vDSP_vintbD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, const double *__C, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_vintb`](./vdsp_vintb.md), except for the types of vectors `A`, `B`, `C`, and `D`.

This example interpolates from `a` (all zeros) toward `b` `[10, 20, 30, 40]` using the interpolation constant `0.25`, computing `a + 0.25 · (b − a)` elementwise. The result is one quarter of the way from `a` to `b`: `[2.5, 5, 7.5, 10]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [0, 0, 0, 0]
var b: [Double] = [10, 20, 30, 40]
var t: Double = 0.25
var d = [Double](repeating: 0, count: a.count)

// Interpolate between `a` and `b` by the constant `t`, computing `a + t * (b - a)`.
vDSP_vintbD(a, 1, b, 1, &t, &d, 1, vDSP_Length(a.count))

// Prints "[2.5, 5.0, 7.5, 10.0]".
print(d)
```

**Objective-C**:

```objc
double a[4] = {0, 0, 0, 0};
double b[4] = {10, 20, 30, 40};
double t = 0.25;
double d[4];

// Interpolate between `a` and `b` by the constant `t`, computing `a + t * (b - a)`.
vDSP_vintbD(a, 1, b, 1, &t, d, 1, 4);

// Prints "[2.5, 5, 7.5, 10]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## See Also

### Vector-to-Vector Linear Interpolation
- [vDSP_vintb](./vdsp_vintb.md)
  Calculates the linear interpolation between the supplied single-precision vectors using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vintbd)*