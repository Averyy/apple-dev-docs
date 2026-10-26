# vDSP_vtrapz

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs trapezoidal integration over a single-precision vector.

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
extern void vDSP_vtrapz(const float *__A, vDSP_Stride __IA, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Performs the following operation:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557740@2x.png)

Estimates the integral of vector `A` using the trapezoidal rule. Scalar `*B` specifies the integration step size. This function can only be done out of place.

This example integrates the ramp `[0, 1, 2, 3]` with a step size of `1` using the trapezoidal rule. Each output element is the running area under the curve up to that point: the area of each trapezoid is the average of its two heights times the step, so the cumulative result is `[0, 0.5, 2, 4.5]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [0, 1, 2, 3]
var step: Float = 1
var c = [Float](repeating: 0, count: a.count)

// Integrate `a` using the trapezoidal rule with the given step size.
vDSP_vtrapz(a, 1, &step, &c, 1, vDSP_Length(a.count))

// Prints "[0.0, 0.5, 2.0, 4.5]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {0, 1, 2, 3};
float step = 1;
float c[4];

// Integrate `a` using the trapezoidal rule with the given step size.
vDSP_vtrapz(a, 1, &step, c, 1, 4);

// Prints "[0, 0.5, 2, 4.5]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for `A`.
- `__B`: Pointer to single-precision real input scalar: step size.
- `__C`: Single-precision real output vector.
- `__IC`: Address stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Trapezoidal Integration
- [vDSP_vtrapzD](./vdsp_vtrapzd.md)
  Performs trapezoidal integration over a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vtrapz)*