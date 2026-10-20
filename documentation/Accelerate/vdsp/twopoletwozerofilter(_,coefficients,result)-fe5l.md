# twoPoleTwoZeroFilter(_:coefficients:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Performs double-precision, two-pole, two-zero recursive filtering.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
static func twoPoleTwoZeroFilter<U, V>(_ source: U, coefficients: (Double, Double, Double, Double, Double), result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

## See Also

### Vector-to-Vector Recursive Filtering on Real Vectors
- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Double, Double, Double, Double, Double)) -> [Double]](./twopoletwozerofilter%28_,coefficients%29-8oaux.md)
  Returns the result of double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Float, Float, Float, Float, Float)) -> [Float]](./twopoletwozerofilter%28_,coefficients%29-3jbcg.md)
  Returns the result of single-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Float, Float, Float, Float, Float), result: inout V)](./twopoletwozerofilter%28_,coefficients,result%29-gq5l.md)
  Performs single-precision, two-pole, two-zero recursive filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/twopoletwozerofilter(_:coefficients:result:)-fe5l)*