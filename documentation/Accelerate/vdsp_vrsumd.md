# vDSP_vrsumD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs running sum integration over a double-precision vector.

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
extern void vDSP_vrsumD(const double *__A, vDSP_Stride __IA, const double *__S, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_vrsum`](./vdsp_vrsum.md), except for the types of vectors `A` and `C` and scalar `*S`.

This example integrates the ramp `[0, 1, 2, 3, 4]` with a weighting factor of `1`. Each output element is the running sum of the weighted inputs so far (the first input element is not added), giving the cumulative totals `[0, 1, 3, 6, 10]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [0, 1, 2, 3, 4]
var weight: Double = 1
var c = [Double](repeating: 0, count: a.count)

// Integrate `a` as a running sum, weighting each element by the given factor.
vDSP_vrsumD(a, 1, &weight, &c, 1, vDSP_Length(a.count))

// Prints "[0.0, 1.0, 3.0, 6.0, 10.0]".
print(c)
```

**Objective-C**:

```objc
double a[5] = {0, 1, 2, 3, 4};
double weight = 1;
double c[5];

// Integrate `a` as a running sum, weighting each element by the given factor.
vDSP_vrsumD(a, 1, &weight, c, 1, 5);

// Prints "[0, 1, 3, 6, 10]".
printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
```

## See Also

### Running Sum Integration
- [vDSP_vrsum](./vdsp_vrsum.md)
  Performs running sum integration over a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrsumd)*