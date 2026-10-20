# Clipping, limit, and threshold operations

**Framework**: Accelerate  
**Role**: API Collection

Apply clipping, limit, or threshold rules to the elements in a vector.

## Topics

### Clipping Operations
- [static func clip<U>(U, to: ClosedRange<Double>) -> [Double]](./vdsp/clip%28_,to%29-8jsic.md)
  Returns the elements of a double-precision vector clipped to the specified range.
- [static func clip<U>(U, to: ClosedRange<Float>) -> [Float]](./vdsp/clip%28_,to%29-20gz4.md)
  Returns the elements of a single-precision vector clipped to the specified range.
- [static func clip<U, V>(U, to: ClosedRange<Double>, result: inout V)](./vdsp/clip%28_,to,result%29-3lbii.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [static func clip<U, V>(U, to: ClosedRange<Float>, result: inout V)](./vdsp/clip%28_,to,result%29-84zw9.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [static func invertedClip<U>(U, to: ClosedRange<Double>) -> [Double]](./vdsp/invertedclip%28_,to%29-8yqtl.md)
  Returns a double-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U>(U, to: ClosedRange<Float>) -> [Float]](./vdsp/invertedclip%28_,to%29-4pkxw.md)
  Returns a single-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U, V>(U, to: ClosedRange<Double>, result: inout V)](./vdsp/invertedclip%28_,to,result%29-5ioal.md)
  Calculates a double-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U, V>(U, to: ClosedRange<Float>, result: inout V)](./vdsp/invertedclip%28_,to,result%29-3q12m.md)
  Calculates a single-precision vector that’s inverted-clipped to the specified range.
### Limit Operations
- [static func limit<U>(U, limit: Double, withOutputConstant: Double) -> [Double]](./vdsp/limit%28_,limit,withoutputconstant%29-2d9u6.md)
  Returns the double-precision vector test limit.
- [static func limit<U>(U, limit: Float, withOutputConstant: Float) -> [Float]](./vdsp/limit%28_,limit,withoutputconstant%29-8bj65.md)
  Returns the single-precision vector test limit.
- [static func limit<U, V>(U, limit: Double, withOutputConstant: Double, result: inout V)](./vdsp/limit%28_,limit,withoutputconstant,result%29-6apdv.md)
  Calculates the double-precision vector test limit.
- [static func limit<U, V>(U, limit: Float, withOutputConstant: Float, result: inout V)](./vdsp/limit%28_,limit,withoutputconstant,result%29-9v33v.md)
  Calculates the single-precision vector test limit.
### Threshold Operations
- [static func threshold<U>(U, to: Double, with: vDSP.ThresholdRule<Double>) -> [Double]](./vdsp/threshold%28_,to,with%29-77g7l.md)
  Returns the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U>(U, to: Float, with: vDSP.ThresholdRule<Float>) -> [Float]](./vdsp/threshold%28_,to,with%29-534ob.md)
  Returns the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Double, with: vDSP.ThresholdRule<Double>, result: inout V)](./vdsp/threshold%28_,to,with,result%29-45b58.md)
  Calculates the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Float, with: vDSP.ThresholdRule<Float>, result: inout V)](./vdsp/threshold%28_,to,with,result%29-8137c.md)
  Calculates the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [vDSP.ThresholdRule](./vdsp/thresholdrule.md)
  Constants that specify vector threshold rules.

## See Also

### Single-vector arithmetic functions
- [Absolute and negation functions](./absolute-and-negation-functions.md)
  Compute the absolute or negated value of each element in a vector.
- [Integration functions](./integration-functions.md)
  Compute the running sum, Simpson, or trapezoidal integration of a vector.
- [Normalization functions](./normalization-functions.md)
  Compute the mean and standard deviation of a vector and calculate new elements to have a zero mean and a unit standard deviation.
- [Phase computation functions](./phase-computation-functions.md)
  Calculate the element-wise phase values, in radians, of a complex vector.
- [Complex conjugation functions](./complex-conjugation-functions.md)
  Calculate the complex conjugate of the elements in a vector.
- [Vector squaring functions](./vector-squaring-functions.md)
  Compute the square, signed square, or squared magnitude of the elements in a vector.
- [Fractional part extraction](./fractional-part-extraction.md)
  Truncate the elements of a vector to a fraction.
- [Zero crossing search](./zero-crossing-search.md)
  Count and find the zero crossings in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/clipping-limit-and-threshold-operations)*