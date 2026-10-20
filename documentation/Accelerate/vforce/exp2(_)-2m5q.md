# exp2(_:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns the 2, raised to the power of each element in a vector of double-precision values.

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
static func exp2<U>(_ vector: U) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

## See Also

### Array-Oriented Exponential and Logarithmic Functions
- [static func exp<U>(U) -> [Double]](./exp%28_%29-76nrd.md)
  Returns the *e*, raised to the power of each element in a vector of double-precision values.
- [static func exp<U>(U) -> [Float]](./exp%28_%29-5iaun.md)
  Returns the *e*, raised to the power of each element in a vector of single-precision values.
- [static func exp<U, V>(U, result: inout V)](./exp%28_,result%29-34nxw.md)
  Calculates the *e*, raised to the power of each element in a vector of double-precision values.
- [static func exp<U, V>(U, result: inout V)](./exp%28_,result%29-4k85n.md)
  Calculates the *e*, raised to the power of each element in a vector of single-precision values.
- [static func exp2<U>(U) -> [Float]](./exp2%28_%29-4mm9y.md)
  Returns the 2, raised to the power of each element in a vector of single-precision values.
- [static func exp2<U, V>(U, result: inout V)](./exp2%28_,result%29-6ru6m.md)
  Calculates the 2, raised to the power of each element in a vector of double-precision values.
- [static func exp2<U, V>(U, result: inout V)](./exp2%28_,result%29-8m564.md)
  Calculates the 2, raised to the power of each element in a vector of single-precision values.
- [static func expm1<U>(U) -> [Double]](./expm1%28_%29-xkzx.md)
  Returns the *eˣ-1* for each element in a vector of double-precision values.
- [static func expm1<U>(U) -> [Float]](./expm1%28_%29-mfq5.md)
  Returns the *eˣ-1* for each element in a vector of single-precision values.
- [static func expm1<U, V>(U, result: inout V)](./expm1%28_,result%29-4dpl4.md)
  Calculates the *eˣ-1* for each element in a vector of double-precision values.
- [static func expm1<U, V>(U, result: inout V)](./expm1%28_,result%29-2yhs3.md)
  Calculates the *eˣ-1* for each element in a vector of single-precision values.
- [static func log10<U>(U) -> [Double]](./log10%28_%29-9wr68.md)
  Returns the base 10 logarithm of each element in a vector of double-precision values.
- [static func log<U>(U) -> [Double]](./log%28_%29-2gh9a.md)
  Returns the natural logarithm for each element in a vector of double-precision values.
- [static func log<U>(U) -> [Float]](./log%28_%29-5ffby.md)
  Returns the natural logarithm for each element in a vector of single-precision values.
- [static func log<U, V>(U, result: inout V)](./log%28_,result%29-84hv7.md)
  Calculates the natural logarithm for each element in a vector of double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vforce/exp2(_:)-2m5q)*