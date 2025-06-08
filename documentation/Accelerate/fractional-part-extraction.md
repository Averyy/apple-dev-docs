# Fractional part extraction

**Framework**: Accelerate

Truncate the elements of a vector to a fraction.

## Topics

### Single-Vector Fractional Part Extraction
- [static func trunc<U>(U) -> [Double]](vdsp/trunc(_:)-80rfo.md)
  Returns a double-precision array containing each element in the supplied vector truncated to a fraction.
- [static func trunc<U>(U) -> [Float]](vdsp/trunc(_:)-1npgt.md)
  Returns a single-precision array containing each element in the supplied vector truncated to a fraction.
- [static func trunc<U, V>(U, result: inout V)](vdsp/trunc(_:result:)-4t63c.md)
  Calculates each element in the supplied double-precision vector truncated to a fraction.
- [static func trunc<U, V>(U, result: inout V)](vdsp/trunc(_:result:)-fabn.md)
  Calculates each element in the supplied single-precision vector truncated to a fraction.
- [vDSP_vfrac](vdsp_vfrac.md)
  Truncates the elements of a single-precision vector to fractions.
- [vDSP_vfracD](vdsp_vfracd.md)
  Truncates the elements of a double-precision vector to fractions.

## See Also

- [Absolute and negation functions](absolute-and-negation-functions.md)
  Compute the absolute or negated value of each element in a vector.
- [Integration functions](integration-functions.md)
  Compute the running sum, Simpson, or trapezoidal integration of a vector.
- [Clipping, limit, and threshold operations](clipping-limit-and-threshold-operations.md)
  Apply clipping, limit, or threshold rules to the elements in a vector.
- [Normalization functions](normalization-functions.md)
  Compute the mean and standard deviation of a vector and calculate new elements to have a zero mean and a unit standard deviation.
- [Phase computation functions](phase-computation-functions.md)
  Calculate the element-wise phase values, in radians, of a complex vector.
- [Complex conjugation functions](complex-conjugation-functions.md)
  Calculate the complex conjugate of the elements in a vector.
- [Vector squaring functions](vector-squaring-functions.md)
  Compute the square, signed square, or squared magnitude of the elements in a vector.
- [Zero crossing search](zero-crossing-search.md)
  Count and find the zero crossings in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/fractional-part-extraction)*