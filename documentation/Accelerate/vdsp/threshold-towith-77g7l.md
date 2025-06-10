# threshold(_:to:with:)

**Framework**: Accelerate  
**Kind**: method

Returns the elements of the supplied double-precision vector after applying a specified thresholding rule.

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
static func threshold<U>(_ vector: U, to lowerBound: Double, with rule: vDSP.ThresholdRule<Double>) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

## See Also

- [static func threshold<U>(U, to: Float, with: vDSP.ThresholdRule<Float>) -> [Float]](vdsp/threshold(_:to:with:)-534ob.md)
  Returns the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Double, with: vDSP.ThresholdRule<Double>, result: inout V)](vdsp/threshold(_:to:with:result:)-45b58.md)
  Calculates the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Float, with: vDSP.ThresholdRule<Float>, result: inout V)](vdsp/threshold(_:to:with:result:)-8137c.md)
  Calculates the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [vDSP.ThresholdRule](vdsp/thresholdrule.md)
  Constants that specify vector threshold rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/threshold(_:to:with:)-77g7l)*