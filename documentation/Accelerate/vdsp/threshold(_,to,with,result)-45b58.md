# threshold(_:to:with:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Calculates the elements of the supplied double-precision vector after applying a specified thresholding rule.

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
static func threshold<U, V>(_ vector: U, to lowerBound: Double, with rule: vDSP.ThresholdRule<Double>, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

## See Also

### Threshold Operations
- [static func threshold<U>(U, to: Double, with: vDSP.ThresholdRule<Double>) -> [Double]](./threshold%28_,to,with%29-77g7l.md)
  Returns the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U>(U, to: Float, with: vDSP.ThresholdRule<Float>) -> [Float]](./threshold%28_,to,with%29-534ob.md)
  Returns the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Float, with: vDSP.ThresholdRule<Float>, result: inout V)](./threshold%28_,to,with,result%29-8137c.md)
  Calculates the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [vDSP.ThresholdRule](./thresholdrule.md)
  Constants that specify vector threshold rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/threshold(_:to:with:result:)-45b58)*