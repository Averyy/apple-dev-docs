# vacosf(_:)

**Framework**: Accelerate  
**Kind**: func

For each vector element, calculates the arccosine.  Results are in the interval [0, pi].

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vacosf(_: vFloat) -> vFloat
```

## See Also

- [func vsinf(vFloat) -> vFloat](vsinf(_:).md)
  For each vector element, calculates the sine.
- [func vcosf(vFloat) -> vFloat](vcosf(_:).md)
  For each vector element, calculates the cosine.
- [func vsincosf(vFloat, UnsafeMutablePointer<vFloat>) -> vFloat](vsincosf(_:_:).md)
  Simultaneously computes sine and cosine of values in a vector.
- [func vtanf(vFloat) -> vFloat](vtanf(_:).md)
  For each vector element, calculates the tangent.
- [func vasinf(vFloat) -> vFloat](vasinf(_:).md)
  For each vector element, calculates the arcsine.  Results are in the interval [-pi/2, pi/2].
- [func vatanf(vFloat) -> vFloat](vatanf(_:).md)
  For each vector element, calculates the arctangent.  Results are in the interval [-pi/2, pi/2].
- [func vatan2f(vFloat, vFloat) -> vFloat](vatan2f(_:_:).md)
  For each vector element, calculates the arctangent of `arg2`/`arg1` in the interval [-pi,pi] using the sign of both arguments to determine the quadrant of the computed value.
- [func vvcbrt(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvcbrt(_:_:_:).md)
  Calculates the cube root for each element of a vector.
- [func vvcbrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvcbrtf(_:_:_:).md)
  Calculates the cube root for each element of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vacosf(_:))*