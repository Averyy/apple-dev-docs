# vvpowsf(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates, element-wise, x**y for a vector x and a scalar y.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vvpowsf(_: UnsafeMutablePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Int32>)
```

```c
void vvpowsf(float *, const float *, const float *, const int *);
```

### Parameters

- **z**: (output) Output vector of size `*n`. `z[i]` is set to `pow(x[i], y)`.
- **y**: (input)  Input scalar, exponent in calculation.
- **x**: (input)  Input vector of size `*n`, base in calculation.
- **n**: (input)  The number of elements in the vectors `x`, `y` and `z`

## See Also

### Exponential and Logarithmic Functions (from vfp.h)
- [func vexpf(vFloat) -> vFloat](./vexpf%28_%29.md)
  For each vector element, calculates the exponential of X.
- [func vexp2f(vFloat) -> vFloat](./vexp2f%28_%29.md)
- [func vexpm1f(vFloat) -> vFloat](./vexpm1f%28_%29.md)
  For each vector element, calculates ExpM1(x) = Exp(x) - 1.  But, for small enough arguments, ExpM1(x) is expected to be more accurate than Exp(x) - 1.
- [func vlogf(vFloat) -> vFloat](./vlogf%28_%29.md)
  For each vector element, calculates the natural logarithm of `X`.
- [func vlog1pf(vFloat) -> vFloat](./vlog1pf%28_%29.md)
  For each vector element, calculates Log1P = Log(1 + x). But, for small enough arguments, Log1P is expected to be more accurate than Log(1 + x).
- [func vlog10f(vFloat) -> vFloat](./vlog10f%28_%29.md)
  Computes the base-10 logarithm of values in a vector.
- [func vlogbf(vFloat) -> vFloat](./vlogbf%28_%29.md)
  For each vector element, extracts the exponent of `X`, as a signed integral value. A subnormal argument is treated as though it were first normalized. Thus:   1  <=  x * 2^(-logb(x))  <  2.
- [func vlog2f(vFloat) -> vFloat](./vlog2f%28_%29.md)
- [func vvpows(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](./vvpows%28_,_,_,_%29.md)
  Calculates the cube root for each element of a vector.
- [func vscalbf(vFloat, vSInt32) -> vFloat](./vscalbf%28_,_%29.md)
  For each vector element, calculates x * 2^n efficiently.  This is not normally done by computing 2^n explicitly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvpowsf(_:_:_:_:))*