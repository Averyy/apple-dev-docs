# Absolute and negation functions

**Framework**: Accelerate  
**Role**: API Collection

Compute the absolute or negated value of each element in a vector.

## Topics

### Vector absolute functions
- [static func absolute<U>(U) -> [Float]](./vdsp/absolute%28_%29-5ehc1.md)
  Returns the absolute value of each element in the supplied single-precision vector.
- [static func absolute<U>(U) -> [Double]](./vdsp/absolute%28_%29-9c3ge.md)
  Returns the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U, V>(U, result: inout V)](./vdsp/absolute%28_,result%29-4pigo.md)
  Calculates the absolute value of each element in the supplied single-precision vector.
- [static func absolute<U, V>(U, result: inout V)](./vdsp/absolute%28_,result%29-657bd.md)
  Calculates the absolute value of each element in the supplied double-precision vector.
- [vDSP_vabsi](./vdsp_vabsi.md)
  Calculates the absolute value of each element in the supplied integer vector using the specified stride.
- [vDSP_vabs](./vdsp_vabs.md)
  Calculates the absolute value of each element in the supplied single-precision vector using the specified stride.
- [vDSP_vabsD](./vdsp_vabsd.md)
  Calculates the absolute value of each element in the supplied double-precision vector using the specified stride.
### Complex vector absolute functions
- [static func absolute<V>(DSPSplitComplex, result: inout V)](./vdsp/absolute%28_,result%29-9x5jn.md)
  Calculates the absolute value of each element in the supplied single-precision complex vector.
- [static func absolute<V>(DSPDoubleSplitComplex, result: inout V)](./vdsp/absolute%28_,result%29-1wu9x.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector.
- [vDSP_zvabs](./vdsp_zvabs.md)
  Calculates the absolute value of each element in the supplied single-precision complex vector using the specified stride.
- [vDSP_zvabsD](./vdsp_zvabsd.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector using the specified stride.
### Vector negative absolute functions
- [static func negativeAbsolute<U>(U) -> [Float]](./vdsp/negativeabsolute%28_%29-66a7a.md)
  Returns the negative absolute value of each element in the supplied single-precision vector.
- [static func negativeAbsolute<U>(U) -> [Double]](./vdsp/negativeabsolute%28_%29-1b5m6.md)
  Returns the negative absolute value of each element in the supplied double-precision vector.
- [static func negativeAbsolute<U, V>(U, result: inout V)](./vdsp/negativeabsolute%28_,result%29-85gj0.md)
  Calculates the negative absolute value of each element in the supplied single-precision vector.
- [static func negativeAbsolute<U, V>(U, result: inout V)](./vdsp/negativeabsolute%28_,result%29-1gpcy.md)
  Calculates the negative absolute value of each element in the supplied double-precision vector.
- [vDSP_vnabs](./vdsp_vnabs.md)
  Calculates the negative absolute value of each element in the supplied single-precision vector using the specified stride.
- [vDSP_vnabsD](./vdsp_vnabsd.md)
  Calculates the negative absolute value of each element in the supplied double-precision vector using the specified stride.
### Vector negation functions
- [static func negative<U>(U) -> [Float]](./vdsp/negative%28_%29-8mo1p.md)
  Returns the negative value of each element in the supplied single-precision vector.
- [static func negative<U>(U) -> [Double]](./vdsp/negative%28_%29-24oe4.md)
  Returns the negative value of each element in the supplied double-precision vector.
- [static func negative<U, V>(U, result: inout V)](./vdsp/negative%28_,result%29-92caw.md)
  Calculates the negative value of each element in the supplied single-precision vector.
- [static func negative<U, V>(U, result: inout V)](./vdsp/negative%28_,result%29-5bwqv.md)
  Calculates the negative value of each element in the supplied double-precision vector.
- [vDSP_vneg](./vdsp_vneg.md)
  Calculates the negative value of each element in the supplied single-precision vector using the specified stride.
- [vDSP_vnegD](./vdsp_vnegd.md)
  Calculates the negative value of each element in the supplied double-precision vector using specified stride.
### Complex vector negation functions
- [vDSP_zvneg](./vdsp_zvneg.md)
  Calculates the negative value of each element in the supplied complex single-precision vector.
- [vDSP_zvnegD](./vdsp_zvnegd.md)
  Calculates the negative value of each element in the supplied complex double-precision vector.

## See Also

### Single-vector arithmetic functions
- [Integration functions](./integration-functions.md)
  Compute the running sum, Simpson, or trapezoidal integration of a vector.
- [Clipping, limit, and threshold operations](./clipping-limit-and-threshold-operations.md)
  Apply clipping, limit, or threshold rules to the elements in a vector.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/absolute-and-negation-functions)*