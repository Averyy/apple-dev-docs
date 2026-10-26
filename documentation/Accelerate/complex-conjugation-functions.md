# Complex conjugation functions

**Framework**: Accelerate  
**Role**: API Collection

Calculate the complex conjugate of the elements in a vector.

## Topics

### Single-Vector Complex Conjugation
- [static func conjugate(DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./vdsp/conjugate%28_,count,result%29-v5m9.md)
  Calculates the complex conjugate of the values in a single-precision vector.
- [static func conjugate(DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](./vdsp/conjugate%28_,count,result%29-89mrk.md)
  Calculates the complex conjugate of the values in a double-precision vector.
- [vDSP_zvconj](./vdsp_zvconj.md)
  Calculates the complex conjugate of the values in a single-precision vector using the specified stride.
- [vDSP_zvconjD](./vdsp_zvconjd.md)
  Calculates the complex conjugate of the values in a double-precision vector using the specified stride.

## See Also

### Single-vector arithmetic functions
- [Absolute and negation functions](./absolute-and-negation-functions.md)
  Compute the absolute or negated value of each element in a vector.
- [Integration functions](./integration-functions.md)
  Compute the running sum, Simpson, or trapezoidal integration of a vector.
- [Clipping, limit, and threshold operations](./clipping-limit-and-threshold-operations.md)
  Apply clipping, limit, or threshold rules to the elements in a vector.
- [Normalization functions](./normalization-functions.md)
  Compute the mean and standard deviation of a vector and calculate new elements to have a zero mean and a unit standard deviation.
- [Phase computation functions](./phase-computation-functions.md)
  Calculate the element-wise phase values, in radians, of a complex vector.
- [Vector squaring functions](./vector-squaring-functions.md)
  Compute the square, signed square, or squared magnitude of the elements in a vector.
- [Fractional part extraction](./fractional-part-extraction.md)
  Truncate the elements of a vector to a fraction.
- [Zero crossing search](./zero-crossing-search.md)
  Count and find the zero crossings in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/complex-conjugation-functions)*