# log2(_:)

**Framework**: Accelerate  
**Kind**: method

Returns the base 2 logarithm of each element in a vector of single-precision values.

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
static func log2<U>(_ vector: U) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## See Also

- [static func exp<U>(U) -> [Double]](vforce/exp(_:)-76nrd.md)
  Returns the , raised to the power of each element in a vector of double-precision values.
- [static func exp<U>(U) -> [Float]](vforce/exp(_:)-5iaun.md)
  Returns the , raised to the power of each element in a vector of single-precision values.
- [static func exp<U, V>(U, result: inout V)](vforce/exp(_:result:)-34nxw.md)
  Calculates the , raised to the power of each element in a vector of double-precision values.
- [static func exp<U, V>(U, result: inout V)](vforce/exp(_:result:)-4k85n.md)
  Calculates the , raised to the power of each element in a vector of single-precision values.
- [static func exp2<U>(U) -> [Double]](vforce/exp2(_:)-2m5q.md)
  Returns the 2, raised to the power of each element in a vector of double-precision values.
- [static func exp2<U>(U) -> [Float]](vforce/exp2(_:)-4mm9y.md)
  Returns the 2, raised to the power of each element in a vector of single-precision values.
- [static func exp2<U, V>(U, result: inout V)](vforce/exp2(_:result:)-6ru6m.md)
  Calculates the 2, raised to the power of each element in a vector of double-precision values.
- [static func exp2<U, V>(U, result: inout V)](vforce/exp2(_:result:)-8m564.md)
  Calculates the 2, raised to the power of each element in a vector of single-precision values.
- [static func expm1<U>(U) -> [Double]](vforce/expm1(_:)-xkzx.md)
  Returns the  for each element in a vector of double-precision values.
- [static func expm1<U>(U) -> [Float]](vforce/expm1(_:)-mfq5.md)
  Returns the  for each element in a vector of single-precision values.
- [static func expm1<U, V>(U, result: inout V)](vforce/expm1(_:result:)-4dpl4.md)
  Calculates the  for each element in a vector of double-precision values.
- [static func expm1<U, V>(U, result: inout V)](vforce/expm1(_:result:)-2yhs3.md)
  Calculates the  for each element in a vector of single-precision values.
- [static func log10<U>(U) -> [Double]](vforce/log10(_:)-9wr68.md)
  Returns the base 10 logarithm of each element in a vector of double-precision values.
- [static func log<U>(U) -> [Double]](vforce/log(_:)-2gh9a.md)
  Returns the natural logarithm for each element in a vector of double-precision values.
- [static func log<U>(U) -> [Float]](vforce/log(_:)-5ffby.md)
  Returns the natural logarithm for each element in a vector of single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vforce/log2(_:)-9b3yo)*