# vDSP_vlimD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision vector test limit using the specified stride.

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
extern void vDSP_vlimD(const double *__A, vDSP_Stride __IA, const double *__B, const double *__C, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_vlim`](./vdsp_vlim.md), except for the types of vectors `A`, `B`, `C`, and `D`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-2, -0.5, 0.5, 3]
var limit: Double = 0
var value: Double = 2
var d = [Double](repeating: 0, count: a.count)

// Apply a test limit: output `+value` where `a[i]` is at least `limit`, and `-value` otherwise.
vDSP_vlimD(a, 1, &limit, &value, &d, 1, vDSP_Length(a.count))

// Prints "[-2.0, -2.0, 2.0, 2.0]".
print(d)
```

**Objective-C**:

```objc
double a[4] = {-2, -0.5, 0.5, 3};
double limit = 0;
double value = 2;
double d[4];

// Apply a test limit: output `+value` where `a[i]` is at least `limit`, and `-value` otherwise.
vDSP_vlimD(a, 1, &limit, &value, d, 1, 4);

// Prints "[-2, -2, 2, 2]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## See Also

### Limit Operations
- [vDSP_vlim](./vdsp_vlim.md)
  Calculates the single-precision vector test limit using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vlimd)*