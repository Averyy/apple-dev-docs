# vDSP_viclipD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the elements of a double-precision vector inverted-clipped to the specified range using the specified stride.

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
extern void vDSP_viclipD(const double *__A, vDSP_Stride __IA, const double *__B, const double *__C, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_viclip`](./vdsp_viclip.md), except for the types of vectors `A`, `B`, `C`, and `D`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-2, -0.5, 0.5, 3]
var low: Double = -1
var high: Double = 1
var d = [Double](repeating: 0, count: a.count)

// Inverted-clip each element of `a`; values within `low` through `high` move out to the nearer bound.
vDSP_viclipD(a, 1, &low, &high, &d, 1, vDSP_Length(a.count))

// Prints "[-2.0, -1.0, 1.0, 3.0]".
print(d)
```

**Objective-C**:

```objc
double a[4] = {-2, -0.5, 0.5, 3};
double low = -1;
double high = 1;
double d[4];

// Inverted-clip each element of `a`; values within `low` through `high` move out to the nearer bound.
vDSP_viclipD(a, 1, &low, &high, d, 1, 4);

// Prints "[-2, -1, 1, 3]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## See Also

### Clipping Operations
- [vDSP_vclip](./vdsp_vclip.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipD](./vdsp_vclipd.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [vDSP_vclipc](./vdsp_vclipc.md)
  Calculates and counts the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipcD](./vdsp_vclipcd.md)
  Calculates and counts the elements of a double-precision vector clipped to the specified range.
- [vDSP_viclip](./vdsp_viclip.md)
  Calculates the elements of a single-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_vthr](./vdsp_vthr.md)
  Calculates single-precision vector threshold to the specified range.
- [vDSP_vthrD](./vdsp_vthrd.md)
  Calculates double-precision vector threshold to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_viclipd)*