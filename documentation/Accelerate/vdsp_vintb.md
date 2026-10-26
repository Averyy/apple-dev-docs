# vDSP_vintb

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the linear interpolation between the supplied single-precision vectors using the specified stride.

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
extern void vDSP_vintb(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, const float *__C, float *__D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function interpolates between the first `N` elements of `A` and `B` by taking the difference between corresponding elements, multiplying it by the constant `C`, and adding this to the corresponding element of `A`; results are left in corresponding elements of `D`:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557779@2x.png)

This example interpolates from `a` (all zeros) toward `b` `[10, 20, 30, 40]` using the interpolation constant `0.25`, computing `a + 0.25 · (b − a)` elementwise. The result is one quarter of the way from `a` to `b`: `[2.5, 5, 7.5, 10]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [0, 0, 0, 0]
var b: [Float] = [10, 20, 30, 40]
var t: Float = 0.25
var d = [Float](repeating: 0, count: a.count)

// Interpolate between `a` and `b` by the constant `t`, computing `a + t * (b - a)`.
vDSP_vintb(a, 1, b, 1, &t, &d, 1, vDSP_Length(a.count))

// Prints "[2.5, 5.0, 7.5, 10.0]".
print(d)
```

**Objective-C**:

```objc
float a[4] = {0, 0, 0, 0};
float b[4] = {10, 20, 30, 40};
float t = 0.25;
float d[4];

// Interpolate between `a` and `b` by the constant `t`, computing `a + t * (b - a)`.
vDSP_vintb(a, 1, b, 1, &t, d, 1, 4);

// Prints "[2.5, 5, 7.5, 10]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for `A`.
- `__B`: Single-precision real input vector.
- `__IB`: Stride for `B`.
- `__C`: Single-precision real input scalar: interpolation constant.
- `__D`: Single-precision real output vector.
- `__ID`: Stride for `D`.
- `__N`: The number of elements to process.

## See Also

### Vector-to-Vector Linear Interpolation
- [vDSP_vintbD](./vdsp_vintbd.md)
  Calculates the linear interpolation between the supplied double-precision vectors using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vintb)*