# vvcosh(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Calculates the hyperbolic cosine of each element in an array of double-precision values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vvcosh(_: UnsafeMutablePointer<Double>, _: UnsafePointer<Double>, _: UnsafePointer<Int32>)
```

#### Discussion

##### Parameters

If `x` is `+/-0`, the result preserves the signed zero.

If `x` is `+/-inf`, the result is `+inf`.

## See Also

- [static func acosh<U>(U) -> [Double]](vforce/acosh(_:)-1j3qt.md)
  Returns the inverse hyperbolic cosine of each element in a vector of double-precision values.
- [static func acosh<U>(U) -> [Float]](vforce/acosh(_:)-8zjay.md)
  Returns the inverse hyperbolic cosine of each element in a vector of single-precision values.
- [static func acosh<U, V>(U, result: inout V)](vforce/acosh(_:result:)-4cip0.md)
  Calculates the inverse hyperbolic cosine of each element in a vector of double-precision values.
- [static func acosh<U, V>(U, result: inout V)](vforce/acosh(_:result:)-2r23w.md)
  Calculates the inverse hyperbolic cosine of each element in a vector of single-precision values.
- [static func asinh<U>(U) -> [Double]](vforce/asinh(_:)-ue6b.md)
  Returns the inverse hyperbolic sine of each element in a vector of double-precision values.
- [static func asinh<U>(U) -> [Float]](vforce/asinh(_:)-284n7.md)
  Returns the inverse hyperbolic sine of each element in a vector of single-precision values.
- [static func asinh<U, V>(U, result: inout V)](vforce/asinh(_:result:)-7wn57.md)
  Calculates the inverse hyperbolic sine of each element in a vector of double-precision values.
- [static func asinh<U, V>(U, result: inout V)](vforce/asinh(_:result:)-17vv4.md)
  Calculates the inverse hyperbolic sine of each element in a vector of single-precision values.
- [static func atanh<U>(U) -> [Double]](vforce/atanh(_:)-922d.md)
  Returns the inverse hyperbolic tangent of each element in a vector of double-precision values.
- [static func atanh<U>(U) -> [Float]](vforce/atanh(_:)-2t372.md)
  Returns the inverse hyperbolic tangent of each element in a vector of single-precision values.
- [static func atanh<U, V>(U, result: inout V)](vforce/atanh(_:result:)-6waj3.md)
  Calculates the inverse hyperbolic tangent of each element in a vector of double-precision values.
- [static func atanh<U, V>(U, result: inout V)](vforce/atanh(_:result:)-596wg.md)
  Calculates the inverse hyperbolic tangent of each element in a vector of single-precision values.
- [static func cosh<U>(U) -> [Double]](vforce/cosh(_:)-4dmhm.md)
  Returns the hyperbolic cosine of each element in a vector of double-precision values.
- [static func cosh<U>(U) -> [Float]](vforce/cosh(_:)-5ax3f.md)
  Returns the hyperbolic cosine of each element in a vector of single-precision values.
- [static func cosh<U, V>(U, result: inout V)](vforce/cosh(_:result:)-4f7in.md)
  Calculates the hyperbolic cosine of each element in a vector of double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvcosh(_:_:_:))*