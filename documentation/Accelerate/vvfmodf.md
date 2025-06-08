# vvfmodf(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Calculates the modulus after dividing each element in an array by the corresponding element in a second array of single-precision values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vvfmodf(_: UnsafeMutablePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Int32>)
```

#### Discussion

##### Parameters

The following code shows an example of using [`vvfmodf(_:_:_:_:)`](vvfmodf(_:_:_:_:).md):

## See Also

- [static func ceil<U>(U) -> [Double]](vforce/ceil(_:)-9dsdt.md)
  Returns the ceiling of each element in a vector of double-precision values.
- [static func ceil<U>(U) -> [Float]](vforce/ceil(_:)-57grr.md)
  Returns the ceiling of each element in a vector of single-precision values.
- [static func ceil<U, V>(U, result: inout V)](vforce/ceil(_:result:)-4wev4.md)
  Calculates the ceiling of each element in a vector of double-precision values.
- [static func ceil<U, V>(U, result: inout V)](vforce/ceil(_:result:)-6zm3u.md)
  Calculates the ceiling of each element in a vector of single-precision values.
- [static func copysign<U, V>(magnitudes: U, signs: V) -> [Double]](vforce/copysign(magnitudes:signs:)-s0r3.md)
  Returns each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<U, V>(magnitudes: U, signs: V) -> [Float]](vforce/copysign(magnitudes:signs:)-3jhf0.md)
  Returns each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<T, U, V>(magnitudes: T, signs: U, result: inout V)](vforce/copysign(magnitudes:signs:result:)-3zoya.md)
  Calculates each double-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<T, U, V>(magnitudes: T, signs: U, result: inout V)](vforce/copysign(magnitudes:signs:result:)-5umya.md)
  Calculates each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func floor<U>(U) -> [Double]](vforce/floor(_:)-64hyu.md)
  Returns the floor of each element in a vector of double-precision values.
- [static func floor<U>(U) -> [Float]](vforce/floor(_:)-5awna.md)
  Returns the floor of each element in a vector of single-precision values.
- [static func floor<U, V>(U, result: inout V)](vforce/floor(_:result:)-61veb.md)
  Calculates the floor of each element in a vector of double-precision values.
- [static func floor<U, V>(U, result: inout V)](vforce/floor(_:result:)-4mf4q.md)
  Calculates the floor of each element in a vector of single-precision values.
- [static func nearestInteger<U>(U) -> [Double]](vforce/nearestinteger(_:)-5mppu.md)
  Returns the nearest integer to each element in a vector of double-precision values.
- [static func nearestInteger<U>(U) -> [Float]](vforce/nearestinteger(_:)-386dx.md)
  Returns the nearest integer to each element in a vector of single-precision values.
- [static func nearestInteger<U, V>(U, result: inout V)](vforce/nearestinteger(_:result:)-bbtt.md)
  Calculates the nearest integer to each element in a vector of double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvfmodf(_:_:_:_:))*