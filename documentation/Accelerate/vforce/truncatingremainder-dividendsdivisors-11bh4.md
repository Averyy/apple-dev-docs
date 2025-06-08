# truncatingRemainder(dividends:divisors:)

**Framework**: Accelerate  
**Kind**: method

Returns the remainder of the double-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.

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
static func truncatingRemainder<U, V>(dividends: U, divisors: V) -> [Double] where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vforce/truncatingremainder(dividends:divisors:)-11bh4)*