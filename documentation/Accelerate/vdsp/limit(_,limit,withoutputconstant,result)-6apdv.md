# limit(_:limit:withOutputConstant:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Calculates the double-precision vector test limit.

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
static func limit<U, V>(_ vector: U, limit: Double, withOutputConstant outputConstant: Double, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

## See Also

### Limit Operations
- [static func limit<U>(U, limit: Double, withOutputConstant: Double) -> [Double]](./limit%28_,limit,withoutputconstant%29-2d9u6.md)
  Returns the double-precision vector test limit.
- [static func limit<U>(U, limit: Float, withOutputConstant: Float) -> [Float]](./limit%28_,limit,withoutputconstant%29-8bj65.md)
  Returns the single-precision vector test limit.
- [static func limit<U, V>(U, limit: Float, withOutputConstant: Float, result: inout V)](./limit%28_,limit,withoutputconstant,result%29-9v33v.md)
  Calculates the single-precision vector test limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/limit(_:limit:withoutputconstant:result:)-6apdv)*