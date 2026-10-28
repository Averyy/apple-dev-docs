# vDSP_vthrscD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates double-precision vector threshold with signed constant to the specified range.

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
extern void vDSP_vthrscD(const double *__A, vDSP_Stride __IA, const double *__B, const double *__C, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_vthrsc`](./vdsp_vthrsc.md), except for the types of vectors `A` and `D`, and scalars `*B` and `*C`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-2, -0.5, 0.5, 3]
var threshold: Double = 0
var constant: Double = 1
var d = [Double](repeating: 0, count: a.count)

// Apply a threshold: output `+constant` where `a[i]` is at least `threshold`, and `-constant` otherwise.
vDSP_vthrscD(a, 1, &threshold, &constant, &d, 1, vDSP_Length(a.count))

// Prints "[-1.0, -1.0, 1.0, 1.0]".
print(d)
```

**Objective-C**:

```objc
double a[4] = {-2, -0.5, 0.5, 3};
double threshold = 0;
double constant = 1;
double d[4];

// Apply a threshold: output `+constant` where `a[i]` is at least `threshold`, and `-constant` otherwise.
vDSP_vthrscD(a, 1, &threshold, &constant, d, 1, 4);

// Prints "[-1, -1, 1, 1]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## See Also

### Threshold Operations
- [vDSP_vthres](./vdsp_vthres.md)
  Calculates single-precision vector threshold with zero fill to the specified range.
- [vDSP_vthresD](./vdsp_vthresd.md)
  Calculates double-precision vector threshold with zero fill to the specified range.
- [vDSP_vthrsc](./vdsp_vthrsc.md)
  Calculates single-precision vector threshold with signed constant to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vthrscd)*