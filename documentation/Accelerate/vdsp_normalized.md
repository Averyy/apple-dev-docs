# vDSP_normalizeD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes double-precision mean and standard deviation, and then calculates new elements to have a zero mean and a unit standard deviation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_normalizeD(const double *__A, vDSP_Stride __IA, double *__C, vDSP_Stride __IC, double *__Mean, double *__StandardDeviation, vDSP_Length __N);
```

## Discussion

This is the same as [`vDSP_normalize`](./vdsp_normalize.md), except for the types of `A`, `C`, `Mean`, and `StandardDeviation`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [1, 2, 3, 4, 5]
var c = [Double](repeating: 0, count: a.count)
var mean: Double = 0
var standardDeviation: Double = 0

// Normalize `a` to zero mean and unit standard deviation, and return the mean and standard deviation.
vDSP_normalizeD(a, 1, &c, 1, &mean, &standardDeviation, vDSP_Length(a.count))

// Prints "[-1.414213562373095, -0.7071067811865475, 0.0, 0.7071067811865475, 1.414213562373095]".
print(c)
// Prints "3.0".
print(mean)
// Prints "1.4142135623730951".
print(standardDeviation)
```

**Objective-C**:

```objc
double a[5] = {1, 2, 3, 4, 5};
double c[5];
double mean;
double standardDeviation;

// Normalize `a` to zero mean and unit standard deviation, and return the mean and standard deviation.
vDSP_normalizeD(a, 1, c, 1, &mean, &standardDeviation, 5);

// Prints "[-1.41421, -0.707107, 0, 0.707107, 1.41421]".
printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
// Prints "3".
printf("%g\n", mean);
// Prints "1.41421".
printf("%g\n", standardDeviation);
```

## See Also

### Normalization Functions
- [vDSP_normalize](./vdsp_normalize.md)
  Computes single-precision mean and standard deviation, and then calculates new elements to have a zero mean and a unit standard deviation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_normalized)*