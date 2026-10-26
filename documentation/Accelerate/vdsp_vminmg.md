# vDSP_vminmg

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the single-precision minimum magnitude of the corresponding values of two vectors using specified strides.

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
extern void vDSP_vminmg(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function compares the magnitudes (absolute values) of the first `N` elements of `A` with corresponding elements of `B`, leaving the lesser (or equal) values as corresponding elements of `C`:

```c
for (n = 0; n < N; ++n)
    C[n] = |A[n]| <= |B[n]| ? |A[n]| : |B[n]|;
```

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [-2, -0.5, 0.5, 3]
var b: [Float] = [1, 1, 1, 1]
var c = [Float](repeating: 0, count: a.count)

// Calculate the elementwise minimum magnitude of `a` and `b`.
vDSP_vminmg(a, 1, b, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1.0, 0.5, 0.5, 1.0]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {-2, -0.5, 0.5, 3};
float b[4] = {1, 1, 1, 1};
float c[4];

// Calculate the elementwise minimum magnitude of `a` and `b`.
vDSP_vminmg(a, 1, b, 1, c, 1, 4);

// Prints "[1, 0.5, 0.5, 1]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for `A`.
- `__B`: Single-precision real input vector.
- `__IB`: Stride for `B`.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Vector-to-Vector Minima
- [vDSP_vmin](./vdsp_vmin.md)
  Calculates the single-precision minimum of the corresponding values of two vectors using specified strides.
- [vDSP_vminD](./vdsp_vmind.md)
  Calculates the double-precision minimum of the corresponding values of two vectors using specified strides.
- [vDSP_vminmgD](./vdsp_vminmgd.md)
  Calculates the double-precision minimum magnitude of the corresponding values of two vectors using specified strides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vminmg)*