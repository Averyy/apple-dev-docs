# Vector squaring functions

**Framework**: Accelerate

Compute the square, signed square, or squared magnitude of the elements in a vector.

## Topics

### Single-Vector Squaring
- [static func square<U>(U) -> [Double]](vdsp/square(_:)-1dz7.md)
  Returns a double-precision array containing the square of each element in the supplied vector.
- [static func square<U>(U) -> [Float]](vdsp/square(_:)-30jok.md)
  Returns a single-precision array containing the square of each element in the supplied vector.
- [static func square<U, V>(U, result: inout V)](vdsp/square(_:result:)-9e5hu.md)
  Calculates the square of each element in the supplied double-precision vector.
- [static func square<U, V>(U, result: inout V)](vdsp/square(_:result:)-3kja7.md)
  Calculates the square of each element in the supplied single-precision vector.
- [static func signedSquare<U>(U) -> [Double]](vdsp/signedsquare(_:)-8y09t.md)
  Returns a double-precision array containing the signed square of each element in the supplied vector.
- [static func signedSquare<U>(U) -> [Float]](vdsp/signedsquare(_:)-9v7ec.md)
  Returns a single-precision array containing the signed square of each element in the supplied vector.
- [static func signedSquare<U, V>(U, result: inout V)](vdsp/signedsquare(_:result:)-56omf.md)
  Calculates the signed square of each element in the supplied double-precision vector.
- [static func signedSquare<U, V>(U, result: inout V)](vdsp/signedsquare(_:result:)-2771f.md)
  Calculates the signed square of each element in the supplied single-precision vector.
- [static func squareMagnitudes<V>(DSPSplitComplex, result: inout V)](vdsp/squaremagnitudes(_:result:)-22k5h.md)
  Calculates the square magnitude of each element in the supplied single-precision complex vector.
- [static func squareMagnitudes<V>(DSPDoubleSplitComplex, result: inout V)](vdsp/squaremagnitudes(_:result:)-14oiw.md)
  Calculates the square magnitude of each element in the supplied double-precision complex vector.
- [vDSP_vsq](vdsp_vsq.md)
  Computes the squared value of each element in the supplied single-precision vector.
- [vDSP_vsqD](vdsp_vsqd.md)
  Computes the squared value of each element in the supplied double-precision vector.
- [vDSP_vssq](vdsp_vssq.md)
  Computes the signed squared value of each element in the supplied single-precision vector.
- [vDSP_vssqD](vdsp_vssqd.md)
  Computes the signed squared value of each element in the supplied double-precision vector.
- [vDSP_zvmags](vdsp_zvmags.md)
  Computes the squared magnitude value of each element in the supplied complex single-precision vector.
- [vDSP_zvmagsD](vdsp_zvmagsd.md)
  Computes the squared magnitude value of each element in the supplied complex double-precision vector.
- [vDSP_zvmgsa](vdsp_zvmgsa.md)
  Complex vector magnitudes square and add; single precision.
- [vDSP_zvmgsaD](vdsp_zvmgsad.md)
  Complex vector magnitudes square and add; double precision.

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
- [Fractional part extraction](fractional-part-extraction.md)
  Truncate the elements of a vector to a fraction.
- [Zero crossing search](zero-crossing-search.md)
  Count and find the zero crossings in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vector-squaring-functions)*