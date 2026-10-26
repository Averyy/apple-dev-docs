# vDSP_normalize

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes single-precision mean and standard deviation, and then calculates new elements to have a zero mean and a unit standard deviation.

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
extern void vDSP_normalize(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, float *__Mean, float *__StandardDeviation, vDSP_Length __N);
```

#### Discussion

The function calculates values for `Mean` and `StandardDeviation`, then calculates new values for `A` to have a zero mean and unit standard deviation.

For iOS 9.0 and later or macOS 10.11 and later, the production of new elements may be omitted by passing `NULL` for `C`. In this case `A` remains unchanged.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [1, 2, 3, 4, 5]
var c = [Float](repeating: 0, count: a.count)
var mean: Float = 0
var standardDeviation: Float = 0

// Normalize `a` to zero mean and unit standard deviation, and return the mean and standard deviation.
vDSP_normalize(a, 1, &c, 1, &mean, &standardDeviation, vDSP_Length(a.count))

// Prints "[-1.4142134, -0.7071067, 5.9604645e-08, 0.7071068, 1.4142137]".
print(c)
// Prints "3.0".
print(mean)
// Prints "1.4142135".
print(standardDeviation)
```

**Objective-C**:

```objc
float a[5] = {1, 2, 3, 4, 5};
float c[5];
float mean;
float standardDeviation;

// Normalize `a` to zero mean and unit standard deviation, and return the mean and standard deviation.
vDSP_normalize(a, 1, c, 1, &mean, &standardDeviation, 5);

// Prints "[-1.41421, -0.707107, 5.96046e-08, 0.707107, 1.41421]".
printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
// Prints "3".
printf("%g\n", mean);
// Prints "1.41421".
printf("%g\n", standardDeviation);
```

## Parameters

- `__A`: Single-precision input vector.
- `__IA`: Stride for `A`.
- `__C`: Single-precision output vector, or `NULL` (see Discussion below).
- `__IC`: Stride for `C`.
- `__Mean`: Single-precision mean of the elements of `A`.
- `__StandardDeviation`: Single-precision standard deviation of the elements of `A`.
- `__N`: Number of elements in `A`.

## See Also

### Normalization Functions
- [vDSP_normalizeD](./vdsp_normalized.md)
  Computes double-precision mean and standard deviation, and then calculates new elements to have a zero mean and a unit standard deviation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_normalize)*