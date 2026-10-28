# vDSP_venvlp

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates whether each element in a single-precision vector falls within a specified range.

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
extern void vDSP_venvlp(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, const float *__C, vDSP_Stride __IC, float *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

Finds the extrema of `C`. For the first `N` elements of `C`, the corresponding element of `A` provides an upper-threshold value, and the corresponding element of `B` provides a  lower-threshold value. If the value of an element of `C` falls outside the range defined by these thresholds, it is copied to the corresponding element of `D`. If its value is within the range, the corresponding element of `D` is set to zero:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557782@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
var high: [Float] = [2, 2, 2, 2]
var low: [Float] = [-2, -2, -2, -2]
var signal: [Float] = [-3, -1, 1, 3]
var d = [Float](repeating: 0, count: signal.count)

// Keep each element of `signal` that lies outside the `low` through `high` band, and set the rest to `0`.
vDSP_venvlp(high, 1, low, 1, signal, 1, &d, 1, vDSP_Length(signal.count))

// Prints "[-3.0, 0.0, 0.0, 3.0]".
print(d)
```

**Objective-C**:

```objc
float high[4] = {2, 2, 2, 2};
float low[4] = {-2, -2, -2, -2};
float signal[4] = {-3, -1, 1, 3};
float d[4];

// Keep each element of `signal` that lies outside the `low` through `high` band, and set the rest to `0`.
vDSP_venvlp(high, 1, low, 1, signal, 1, d, 1, 4);

// Prints "[-3, 0, 0, 3]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## Parameters

- `__A`: Single-precision real input vector: high envelope.
- `__IA`: Stride for `A`.
- `__B`: Single-precision real input vector: low envelope.
- `__IB`: Stride for `B`.
- `__C`: Single-precision real input vector.
- `__IC`: Stride for `C`.
- `__D`: Single-precision real output vector.
- `__ID`: Stride for `D`.
- `__N`: The number of elements to process.

## See Also

### Vector-to-Vector Extrema Finding
- [vDSP_venvlpD](./vdsp_venvlpd.md)
  Calculates whether each element in a double-precision vector falls within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_venvlp)*