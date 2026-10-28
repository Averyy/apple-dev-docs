# vDSP_vrsum

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs running sum integration over a single-precision vector.

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
extern void vDSP_vrsum(const float *__A, vDSP_Stride __IA, const float *__S, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

Performs the following operation:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557738@2x.png)

Integrates vector `A` using a running sum from vector `C`. Vector `A` is weighted by scalar `*S` and added to the previous output point. The first element  from vector `A` is not used in the sum.

This example integrates the ramp `[0, 1, 2, 3, 4]` with a weighting factor of `1`. Each output element is the running sum of the weighted inputs so far (the first input element is not added), giving the cumulative totals `[0, 1, 3, 6, 10]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [0, 1, 2, 3, 4]
var weight: Float = 1
var c = [Float](repeating: 0, count: a.count)

// Integrate `a` as a running sum, weighting each element by the given factor.
vDSP_vrsum(a, 1, &weight, &c, 1, vDSP_Length(a.count))

// Prints "[0.0, 1.0, 3.0, 6.0, 10.0]".
print(c)
```

**Objective-C**:

```objc
float a[5] = {0, 1, 2, 3, 4};
float weight = 1;
float c[5];

// Integrate `a` as a running sum, weighting each element by the given factor.
vDSP_vrsum(a, 1, &weight, c, 1, 5);

// Prints "[0, 1, 3, 6, 10]".
printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for `A`.
- `__S`: Points to single-precision real input scalar: weighting factor.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for `C`
- `__N`: The number of elements to process.

## See Also

### Running Sum Integration
- [vDSP_vrsumD](./vdsp_vrsumd.md)
  Performs running sum integration over a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrsum)*