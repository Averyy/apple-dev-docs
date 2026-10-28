# vDSP_vmaxmg

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the single-precision maximum magnitude of the corresponding values of two vectors using specified strides.

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
extern void vDSP_vmaxmg(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function compares the magnitudes (absolute values) of the first `N` elements of `A` with corresponding elements of `B`, leaving the greater (or equal) values as corresponding elements of `C`:

```c
for (n = 0; n < N; ++n)
    C[n] = |B[n]| <= |A[n]| ? |A[n]| : |B[n]|;
```

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [-2, -0.5, 0.5, 3]
var b: [Float] = [1, 1, 1, 1]
var c = [Float](repeating: 0, count: a.count)

// Calculate the elementwise maximum magnitude of `a` and `b`.
vDSP_vmaxmg(a, 1, b, 1, &c, 1, vDSP_Length(a.count))

// Prints "[2.0, 1.0, 1.0, 3.0]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {-2, -0.5, 0.5, 3};
float b[4] = {1, 1, 1, 1};
float c[4];

// Calculate the elementwise maximum magnitude of `a` and `b`.
vDSP_vmaxmg(a, 1, b, 1, c, 1, 4);

// Prints "[2, 1, 1, 3]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for `A`.
- `__B`: Single-precision real input vector.
- `__IB`: Stride for `B`.
- `__C`: Single-precision real output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process

## See Also

### Vector-to-Vector Maxima
- [vDSP_vmax](./vdsp_vmax.md)
  Calculates the single-precision maximum of the corresponding values of two vectors using specified strides.
- [vDSP_vmaxD](./vdsp_vmaxd.md)
  Calculates the double-precision maximum of the corresponding values of two vectors using specified strides.
- [vDSP_vmaxmgD](./vdsp_vmaxmgd.md)
  Calculates the double-precision maximum magnitude of the corresponding values of two vectors using specified strides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vmaxmg)*