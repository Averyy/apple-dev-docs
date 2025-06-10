# vvpowsf(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Calculates, elementwise, x**y for a vector x and a scalar y.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vvpowsf(_: UnsafeMutablePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Int32>)
```

##### Parameters

## See Also

- [func vexpf(vFloat) -> vFloat](vexpf(_:).md)
  For each vector element, calculates the exponential of X.
- [func vexp2f(vFloat) -> vFloat](vexp2f(_:).md)
- [func vexpm1f(vFloat) -> vFloat](vexpm1f(_:).md)
  For each vector element, calculates ExpM1(x) = Exp(x) - 1.  But, for small enough arguments, ExpM1(x) is expected to be more accurate than Exp(x) - 1.
- [func vlogf(vFloat) -> vFloat](vlogf(_:).md)
  For each vector element, calculates the natural logarithm of `X`.
- [func vlog1pf(vFloat) -> vFloat](vlog1pf(_:).md)
  For each vector element, calculates Log1P = Log(1 + x). But, for small enough arguments, Log1P is expected to be more accurate than Log(1 + x).
- [func vlog10f(vFloat) -> vFloat](vlog10f(_:).md)
  Computes the base-10 logarithm of values in a vector.
- [func vlogbf(vFloat) -> vFloat](vlogbf(_:).md)
  For each vector element, extracts the exponent of `X`, as a signed integral value. A subnormal argument is treated as though it were first normalized. Thus:   1  <=  x * 2^(-logb(x))  <  2.
- [func vlog2f(vFloat) -> vFloat](vlog2f(_:).md)
- [func vvpows(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvpows(_:_:_:_:).md)
  Calculates the cube root for each element of a vector.
- [func vscalbf(vFloat, vSInt32) -> vFloat](vscalbf(_:_:).md)
  For each vector element, calculates x * 2^n efficiently.  This is not normally done by computing 2^n explicitly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvpowsf(_:_:_:_:))*