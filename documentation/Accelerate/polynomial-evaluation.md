# Polynomial evaluation

**Framework**: Accelerate

Evaluate polynomials using coefficients and independent variables that you supply.

## Topics

### Single-precision polynomial evaluation
- [static func evaluatePolynomial<U>(usingCoefficients: [Float], withVariables: U) -> [Float]](vdsp/evaluatepolynomial(usingcoefficients:withvariables:)-7mznu.md)
  Returns a single-precision evaluated polynomial using specified coefficients and variables.
- [static func evaluatePolynomial<U, V>(usingCoefficients: [Float], withVariables: U, result: inout V)](vdsp/evaluatepolynomial(usingcoefficients:withvariables:result:)-6eaoc.md)
  Evaluates a single-precision polynomial using specified coefficients and variables.
- [vDSP_vpoly](vdsp_vpoly.md)
  Evaluates a single-precision polynomial using specified coefficients, variables, and strides.
### Double-precision polynomial evaluation
- [static func evaluatePolynomial<U>(usingCoefficients: [Double], withVariables: U) -> [Double]](vdsp/evaluatepolynomial(usingcoefficients:withvariables:)-31vi2.md)
  Returns a double-precision evaluated polynomial using specified coefficients and variables.
- [static func evaluatePolynomial<U, V>(usingCoefficients: [Double], withVariables: U, result: inout V)](vdsp/evaluatepolynomial(usingcoefficients:withvariables:result:)-2ncdh.md)
  Evaluates a double-precision polynomial using specified coefficients and variables.
- [vDSP_vpolyD](vdsp_vpolyd.md)
  Evaluates a double-precision polynomial using specified coefficients, variables, and strides.

## See Also

- [Vector-vector real arithmetic functions](vector-vector-real-arithmetic-functions.md)
  Perform element-wise operations on vectors of real values.
- [Complex basic arithmetic](complex-basic-arithmetic.md)
  Perform elementwise operations on vectors of complex values.
- [Integer arithmetic](integer-arithmetic.md)
  Perform elementwise operations on vectors of integer values.
- [Linear averaging functions](linear-averaging-functions.md)
  Calculate the element-wise linear average of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/polynomial-evaluation)*