# vsincosf(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Simultaneously computes sine and cosine of values in a vector.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vsincosf(_: vFloat, _: UnsafeMutablePointer<vFloat>) -> vFloat
```

```c
extern vFloat vsincosf(vFloat , vFloat *);
```

## Return Value

Returns a vector that contains the result of `cos(x)` for each value (`x`) in the source vector.

### Parameters:

- **parameter 1**: the source vector.
- **parameter 2**: the output vector.

## See Also

### Trigonometric Functions (from vfp.h)
- [func vsinf(vFloat) -> vFloat](./vsinf%28_%29.md)
  For each vector element, calculates the sine.
- [func vcosf(vFloat) -> vFloat](./vcosf%28_%29.md)
  For each vector element, calculates the cosine.
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
- [func vvcbrt(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](./vvcbrt%28_,_,_%29.md)
  Calculates the cube root for each element of a vector.
- [func vvcbrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](./vvcbrtf%28_,_,_%29.md)
  Calculates the cube root for each element of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsincosf(_:_:))*