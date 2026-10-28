# vvcbrt(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the cube root for each element of a vector.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vvcbrt(_: UnsafeMutablePointer<Double>, _: UnsafePointer<Double>, _: UnsafePointer<Int32>)
```

```c
void vvcbrt(double *, const double *, const int *);
```

### Parameters

- **y**: (output) Output vector of size `*n`. `y[i]` is set to `cbrt(x[i])`.
- **x**: (input) Input vector of size `*n`.
- **n**: (input) The number of elements in the vectors `x` and `y`.

## See Also

### Trigonometric Functions (from vfp.h)
- [func vsinf(vFloat) -> vFloat](./vsinf%28_%29.md)
  For each vector element, calculates the sine.
- [func vcosf(vFloat) -> vFloat](./vcosf%28_%29.md)
  For each vector element, calculates the cosine.
- [func vsincosf(vFloat, UnsafeMutablePointer<vFloat>) -> vFloat](./vsincosf%28_,_%29.md)
  Simultaneously computes sine and cosine of values in a vector.
- [func vtanf(vFloat) -> vFloat](./vtanf%28_%29.md)
  For each vector element, calculates the tangent.
- [func vasinf(vFloat) -> vFloat](./vasinf%28_%29.md)
  For each vector element, calculates the arcsine.  Results are in the interval [-pi/2, pi/2].
- [func vacosf(vFloat) -> vFloat](./vacosf%28_%29.md)
  For each vector element, calculates the arccosine.  Results are in the interval [0, pi].
- [func vatanf(vFloat) -> vFloat](./vatanf%28_%29.md)
  For each vector element, calculates the arctangent.  Results are in the interval [-pi/2, pi/2].
- [func vatan2f(vFloat, vFloat) -> vFloat](./vatan2f%28_,_%29.md)
  For each vector element, calculates the arctangent of `arg2`/`arg1` in the interval [-pi,pi] using the sign of both arguments to determine the quadrant of the computed value.
- [func vvcbrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](./vvcbrtf%28_,_,_%29.md)
  Calculates the cube root for each element of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvcbrt(_:_:_:))*