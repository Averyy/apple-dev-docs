# twoPoleTwoZeroFilter(_:coefficients:)

**Framework**: Accelerate  
**Kind**: method

Returns the result of single-precision, two-pole, two-zero recursive filtering.

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
static func twoPoleTwoZeroFilter<U>(_ source: U, coefficients: (Float, Float, Float, Float, Float)) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## See Also

- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Double, Double, Double, Double, Double)) -> [Double]](vdsp/twopoletwozerofilter(_:coefficients:)-8oaux.md)
  Returns the result of double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Double, Double, Double, Double, Double), result: inout V)](vdsp/twopoletwozerofilter(_:coefficients:result:)-fe5l.md)
  Performs double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Float, Float, Float, Float, Float), result: inout V)](vdsp/twopoletwozerofilter(_:coefficients:result:)-gq5l.md)
  Performs single-precision, two-pole, two-zero recursive filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/twopoletwozerofilter(_:coefficients:)-3jbcg)*