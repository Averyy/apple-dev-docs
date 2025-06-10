# threshold(_:to:with:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the elements of the supplied single-precision vector after applying a specified thresholding rule.

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
static func threshold<U, V>(_ vector: U, to lowerBound: Float, with rule: vDSP.ThresholdRule<Float>, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```

## See Also

- [static func threshold<U>(U, to: Double, with: vDSP.ThresholdRule<Double>) -> [Double]](vdsp/threshold(_:to:with:)-77g7l.md)
  Returns the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U>(U, to: Float, with: vDSP.ThresholdRule<Float>) -> [Float]](vdsp/threshold(_:to:with:)-534ob.md)
  Returns the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Double, with: vDSP.ThresholdRule<Double>, result: inout V)](vdsp/threshold(_:to:with:result:)-45b58.md)
  Calculates the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [vDSP.ThresholdRule](vdsp/thresholdrule.md)
  Constants that specify vector threshold rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/threshold(_:to:with:result:)-8137c)*