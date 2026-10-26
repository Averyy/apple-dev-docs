# vDSP_vthresD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates double-precision vector threshold with zero fill to the specified range.

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
extern void vDSP_vthresD(const double *__A, vDSP_Stride __IA, const double *__B, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_vthres`](./vdsp_vthres.md), except for the types of vectors `A` and `C` and scalar `*B`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-2, -0.5, 0.5, 3]
var threshold: Double = 0
var c = [Double](repeating: 0, count: a.count)

// Apply a threshold with zero fill: keep elements at least `threshold`, and set the rest to `0`.
vDSP_vthresD(a, 1, &threshold, &c, 1, vDSP_Length(a.count))

// Prints "[0.0, 0.0, 0.5, 3.0]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {-2, -0.5, 0.5, 3};
double threshold = 0;
double c[4];

// Apply a threshold with zero fill: keep elements at least `threshold`, and set the rest to `0`.
vDSP_vthresD(a, 1, &threshold, c, 1, 4);

// Prints "[0, 0, 0.5, 3]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## See Also

### Threshold Operations
- [vDSP_vthres](./vdsp_vthres.md)
  Calculates single-precision vector threshold with zero fill to the specified range.
- [vDSP_vthrsc](./vdsp_vthrsc.md)
  Calculates single-precision vector threshold with signed constant to the specified range.
- [vDSP_vthrscD](./vdsp_vthrscd.md)
  Calculates double-precision vector threshold with signed constant to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vthresd)*