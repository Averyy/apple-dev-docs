# vDSP.ThresholdRule

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that specify vector threshold rules.

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
enum ThresholdRule<T> where T : BinaryFloatingPoint
```

## Topics

### Threshold rules
- [vDSP.ThresholdRule.clampToThreshold](./thresholdrule/clamptothreshold.md)
  Returns the threshold if the input value is less than threshold; otherwise returns the input value.
- [vDSP.ThresholdRule.signedConstant(_:)](./thresholdrule/signedconstant%28_%29.md)
  Returns the negated constant if the input value is less than the threshold; otherwise returns the constant.
- [vDSP.ThresholdRule.zeroFill](./thresholdrule/zerofill.md)
  Returns `0` if the input value is less than the threshold; otherwise returns the input value.

## See Also

### Threshold Operations
- [static func threshold<U>(U, to: Double, with: vDSP.ThresholdRule<Double>) -> [Double]](./threshold%28_,to,with%29-77g7l.md)
  Returns the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U>(U, to: Float, with: vDSP.ThresholdRule<Float>) -> [Float]](./threshold%28_,to,with%29-534ob.md)
  Returns the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Double, with: vDSP.ThresholdRule<Double>, result: inout V)](./threshold%28_,to,with,result%29-45b58.md)
  Calculates the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Float, with: vDSP.ThresholdRule<Float>, result: inout V)](./threshold%28_,to,with,result%29-8137c.md)
  Calculates the elements of the supplied single-precision vector after applying a specified thresholding rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/thresholdrule)*