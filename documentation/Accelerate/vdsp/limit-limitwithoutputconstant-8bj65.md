# limit(_:limit:withOutputConstant:)

**Framework**: Accelerate  
**Kind**: method

Returns the single-precision vector test limit.

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
static func limit<U>(_ vector: U, limit: Float, withOutputConstant outputConstant: Float) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## See Also

- [static func limit<U>(U, limit: Double, withOutputConstant: Double) -> [Double]](vdsp/limit(_:limit:withoutputconstant:)-2d9u6.md)
  Returns the double-precision vector test limit.
- [static func limit<U, V>(U, limit: Double, withOutputConstant: Double, result: inout V)](vdsp/limit(_:limit:withoutputconstant:result:)-6apdv.md)
  Calculates the double-precision vector test limit.
- [static func limit<U, V>(U, limit: Float, withOutputConstant: Float, result: inout V)](vdsp/limit(_:limit:withoutputconstant:result:)-9v33v.md)
  Calculates the single-precision vector test limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/limit(_:limit:withoutputconstant:)-8bj65)*