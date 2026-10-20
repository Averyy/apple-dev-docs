# vacosf(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

For each vector element, calculates the arccosine.  Results are in the interval [0, pi].

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vacosf(_: vFloat) -> vFloat
```

```c
extern vFloat vacosf(vFloat );
```

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
- [func vatanf(vFloat) -> vFloat](./vatanf%28_%29.md)
  For each vector element, calculates the arctangent.  Results are in the interval [-pi/2, pi/2].
- [func vatan2f(vFloat, vFloat) -> vFloat](./vatan2f%28_,_%29.md)
  For each vector element, calculates the arctangent of `arg2`/`arg1` in the interval [-pi,pi] using the sign of both arguments to determine the quadrant of the computed value.
- [func vvcbrt(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](./vvcbrt%28_,_,_%29.md)
  Calculates the cube root for each element of a vector.
- [func vvcbrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](./vvcbrtf%28_,_,_%29.md)
  Calculates the cube root for each element of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vacosf(_:))*