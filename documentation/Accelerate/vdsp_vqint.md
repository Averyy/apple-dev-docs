# vDSP_vqint

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates single-precision vector quadratic interpolation.

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
extern void vDSP_vqint(const float *__A, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __M);
```

## Discussion

Generates `C` by interpolating between neighboring values of `A` as controlled by values in `B`. The integer portion of each element in `B` is the zero-based index of the second element of a triple of adjacent values in vector `A`.

The value of the corresponding element of `C` is derived from these three values by quadratic interpolation, using the fractional part of the value in `B`. The calculation is equivalent to the following pseudocode:

```objc
for (n = 0; n < N; ++n)
{
    b = max(trunc(B[n]), 1);
    a = B[n] - b;
    C[n] = (A[b-1]*(a**2-a)
           + A[b]*(2-2*a**2)
           + A[b+1]*(a**2+a))
           / 2;
}
```

Argument `M` is not used in the calculation. However, the integer parts of the values in `B` must be less than or equal to `M` - 2.

This example uses `a` as the lookup table `[0, 10, 40, 90]` (samples of `10·x²`) and `b` as fractional indices. The function fits a parabola through each triple of neighboring table entries and evaluates it at the fractional position, so index `1.5` gives `22.5`, producing `[10, 22.5, 40, 62.5]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [0, 10, 40, 90]
var b: [Float] = [1.0, 1.5, 2.0, 2.5]
var c = [Float](repeating: 0, count: b.count)

// Quadratically interpolate values from the lookup table `a` at the fractional indices in `b`.
vDSP_vqint(a, b, 1, &c, 1, vDSP_Length(b.count), vDSP_Length(a.count))

// Prints "[10.0, 22.5, 40.0, 62.5]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {0, 10, 40, 90};
float b[4] = {1.0, 1.5, 2.0, 2.5};
float c[4];

// Quadratically interpolate values from the lookup table `a` at the fractional indices in `b`.
vDSP_vqint(a, b, 1, c, 1, 4, 4);

// Prints "[10, 22.5, 40, 62.5]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: Single-precision real input vector with a stride of 1.
- `__B`: Single-precision real input vector. Integer parts are indices into `A` and fractional parts are interpolation constants
- `__IB`: Stride for `B`.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for `C`.
- `__N`: Count for `C`.
- `__M`: Length of `A`. Must be greater than or equal to 3.

## See Also

### Vector-to-Vector Quadratic Interpolation
- [vDSP_vqintD](./vdsp_vqintd.md)
  Calculates double-precision vector quadratic interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vqint)*