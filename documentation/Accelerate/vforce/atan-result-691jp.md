# atan(_:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the arctangent of each element in a vector of double-precision values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func atan<U, V>(_ vector: U, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

## See Also

- [static func acos<U>(U) -> [Double]](vforce/acos(_:)-8srk.md)
  Returns the arccosine of each element in a vector of double-precision values.
- [static func acos<U>(U) -> [Float]](vforce/acos(_:)-3hl5t.md)
  Returns the arccosine of each element in a vector of single-precision values.
- [static func acos<U, V>(U, result: inout V)](vforce/acos(_:result:)-3c9qz.md)
  Calculates the arccosine of each element in a vector of double-precision values.
- [static func acos<U, V>(U, result: inout V)](vforce/acos(_:result:)-6rc2f.md)
  Calculates the arccosine of each element in a vector of single-precision values.
- [static func asin<U>(U) -> [Double]](vforce/asin(_:)-454ds.md)
  Returns the arcsine of each element in a vector of double-precision values.
- [static func asin<U>(U) -> [Float]](vforce/asin(_:)-8vvt1.md)
  Returns the arcsine of each element in a vector of single-precision values.
- [static func asin<U, V>(U, result: inout V)](vforce/asin(_:result:)-94jmy.md)
  Calculates the arcsine of each element in a vector of double-precision values.
- [static func asin<U, V>(U, result: inout V)](vforce/asin(_:result:)-ooti.md)
  Calculates the arcsine of each element in a vector of single-precision values.
- [static func atan<U>(U) -> [Double]](vforce/atan(_:)-1ghr3.md)
  Returns the arctangent of each element in a vector of double-precision values.
- [static func atan<U>(U) -> [Float]](vforce/atan(_:)-5ejvk.md)
  Returns the arctangent of each element in a vector of single-precision values.
- [static func atan<U, V>(U, result: inout V)](vforce/atan(_:result:)-6bb8n.md)
  Calculates the arctangent of each element in a vector of single-precision values.
- [static func atan2<U, V>(x: U, y: V) -> [Double]](vforce/atan2(x:y:)-h54u.md)
  Returns the arctangent of each pair of elements in two vectors of double-precision values.
- [static func atan2<U, V>(x: U, y: V) -> [Float]](vforce/atan2(x:y:)-3lku3.md)
  Returns the arctangent of each pair of elements in two vectors of single-precision values.
- [static func atan2<T, U, V>(x: T, y: U, result: inout V)](vforce/atan2(x:y:result:)-184b6.md)
  Calculates the arctangent of each pair of elements in two vectors of double-precision values.
- [static func atan2<T, U, V>(x: T, y: U, result: inout V)](vforce/atan2(x:y:result:)-6j6xb.md)
  Calculates the arctangent of each pair of elements in two vectors of single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vforce/atan(_:result:)-691jp)*