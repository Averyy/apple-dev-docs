# vDSP_vlintD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the interpolation between the neighboring elements of a double-precision vector using the specified stride.

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
extern void vDSP_vlintD(const double *__A, const double *__B, vDSP_Stride __IB, double *__C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __M);
```

## Mentions

- [Using linear interpolation to construct new data points](./using-linear-interpolation-to-construct-new-data-points.md)

#### Discussion

Performs the following operation:

```objc
for (int n = 0; n < N; ++n){
    double b = B[n*IB];
    double index = trunc(b); // The integer part of B.
    double alpha = b - index; // The fractional part of B.
 
    double a0 = A[(int)index]; // The indexed A value.
    double a1 = A[(int)index + 1]; // The next indexed A value.
 
    C[n*IC] = a0 + (alpha * (a1 -a0)); // The interpolated value.
}
```

The function generates vector `C` by interpolating between neighboring values of vector `A` as controlled by vector `B`. The operation treats the integer portion of each element in `B` as the zero-based index of the first element of a pair of adjacent values in vector `A`.

The function uses the fractional part of the value in `B` to calculate the corresponding element of `C` from the two adjacent values.

The calculation doesn’t use the argument `M`. However, the integer parts of the values in `B` must be greater than or equal to zero and less than or equal to `M` - 2.

This example uses `a` as a lookup table `[0, 10, 20, 30]` and `b` as fractional indices into it. For each index, the function linearly interpolates between the two neighboring table entries — for example index `0.5` gives `5` (halfway between `0` and `10`) and index `2.25` gives `22.5` — producing `[0, 5, 15, 22.5]`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [0, 10, 20, 30]
var b: [Double] = [0.0, 0.5, 1.5, 2.25]
var c = [Double](repeating: 0, count: b.count)

// Linearly interpolate values from the lookup table `a` at the fractional indices in `b`.
vDSP_vlintD(a, b, 1, &c, 1, vDSP_Length(b.count), vDSP_Length(a.count))

// Prints "[0.0, 5.0, 15.0, 22.5]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {0, 10, 20, 30};
double b[4] = {0.0, 0.5, 1.5, 2.25};
double c[4];

// Linearly interpolate values from the lookup table `a` at the fractional indices in `b`.
vDSP_vlintD(a, b, 1, c, 1, 4, 4);

// Prints "[0, 5, 15, 22.5]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: The double-precision input vector.
- `__B`: The vector that controls the interpolation. The integer part of each element in the control vector is the zero-based index of the first element of a pair of adjacent values in the source array. The fractional part defines the linear interpolation between the values at those indices.
- `__IB`: The stride between elements in the vector `__B`.
- `__C`: The double-precision output vector.
- `__IC`: The stride between elements in the vector `__C`.
- `__N`: The number of elements in the output vector.
- `__M`: The number of elements in the input vector.

## See Also

### Single-Vector Linear Interpolation
- [Using linear interpolation to construct new data points](./using-linear-interpolation-to-construct-new-data-points.md)
  Fill the gaps in arrays of numerical data using linear interpolation.
- [vDSP_vlint](./vdsp_vlint.md)
  Calculates the interpolation between the neighboring elements of a single-precision vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vlintd)*