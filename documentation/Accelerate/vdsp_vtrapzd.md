# vDSP_vtrapzD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs trapezoidal integration over a double-precision vector.

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
extern void vDSP_vtrapzD(const double *__A, vDSP_Stride __IA, const double *__B, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_vtrapz`](./vdsp_vtrapz.md), except for the types of vectors `A` and `C` and scalar `*B`.

This example integrates the ramp `[0, 1, 2, 3]` with a step size of `1` using the trapezoidal rule. Each output element is the running area under the curve up to that point: the area of each trapezoid is the average of its two heights times the step, so the cumulative result is `[0, 0.5, 2, 4.5]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [0, 1, 2, 3]
var step: Double = 1
var c = [Double](repeating: 0, count: a.count)

// Integrate `a` using the trapezoidal rule with the given step size.
vDSP_vtrapzD(a, 1, &step, &c, 1, vDSP_Length(a.count))

// Prints "[0.0, 0.5, 2.0, 4.5]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {0, 1, 2, 3};
double step = 1;
double c[4];

// Integrate `a` using the trapezoidal rule with the given step size.
vDSP_vtrapzD(a, 1, &step, c, 1, 4);

// Prints "[0, 0.5, 2, 4.5]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## See Also

### Trapezoidal Integration
- [vDSP_vtrapz](./vdsp_vtrapz.md)
  Performs trapezoidal integration over a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vtrapzd)*