# vDSP_venvlpD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates whether each element in a double-precision vector falls within a specified range.

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
extern void vDSP_venvlpD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, const double *__C, vDSP_Stride __IC, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_venvlp`](./vdsp_venvlp.md), except for the types of vectors `A`, `B`, `C`, and `D`.

The following code shows an example of using this function:

**Swift**:

```swift
var high: [Double] = [2, 2, 2, 2]
var low: [Double] = [-2, -2, -2, -2]
var signal: [Double] = [-3, -1, 1, 3]
var d = [Double](repeating: 0, count: signal.count)

// Keep each element of `signal` that lies outside the `low` through `high` band, and set the rest to `0`.
vDSP_venvlpD(high, 1, low, 1, signal, 1, &d, 1, vDSP_Length(signal.count))

// Prints "[-3.0, 0.0, 0.0, 3.0]".
print(d)
```

**Objective-C**:

```objc
double high[4] = {2, 2, 2, 2};
double low[4] = {-2, -2, -2, -2};
double signal[4] = {-3, -1, 1, 3};
double d[4];

// Keep each element of `signal` that lies outside the `low` through `high` band, and set the rest to `0`.
vDSP_venvlpD(high, 1, low, 1, signal, 1, d, 1, 4);

// Prints "[-3, 0, 0, 3]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## See Also

### Vector-to-Vector Extrema Finding
- [vDSP_venvlp](./vdsp_venvlp.md)
  Calculates whether each element in a single-precision vector falls within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_venvlpd)*