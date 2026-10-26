# vDSP_vminD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision minimum of the corresponding values of two vectors using specified strides.

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
extern void vDSP_vminD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function compares the first `N` elements of `A` with corresponding elements of `B`, leaving the lesser (or equal) values as corresponding elements of `C`:

```c
for (n = 0; n < N; ++n)
    C[n] = A[n] <= B[n] ? A[n] : B[n];
```

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-2, -0.5, 0.5, 3]
var b: [Double] = [2, 2, 2, 2]
var c = [Double](repeating: 0, count: a.count)

// Calculate the elementwise minimum of `a` and `b`.
vDSP_vminD(a, 1, b, 1, &c, 1, vDSP_Length(a.count))

// Prints "[-2.0, -0.5, 0.5, 2.0]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {-2, -0.5, 0.5, 3};
double b[4] = {2, 2, 2, 2};
double c[4];

// Calculate the elementwise minimum of `a` and `b`.
vDSP_vminD(a, 1, b, 1, c, 1, 4);

// Prints "[-2, -0.5, 0.5, 2]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: Double-precision real input vector.
- `__IA`: Stride for `A`.
- `__B`: Double-precision real input vector.
- `__IB`: Stride for `B`.
- `__C`: Double-precision real output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Vector-to-Vector Minima
- [vDSP_vmin](./vdsp_vmin.md)
  Calculates the single-precision minimum of the corresponding values of two vectors using specified strides.
- [vDSP_vminmg](./vdsp_vminmg.md)
  Calculates the single-precision minimum magnitude of the corresponding values of two vectors using specified strides.
- [vDSP_vminmgD](./vdsp_vminmgd.md)
  Calculates the double-precision minimum magnitude of the corresponding values of two vectors using specified strides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vmind)*