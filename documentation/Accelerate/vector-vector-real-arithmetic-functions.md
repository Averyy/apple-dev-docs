# Vector-vector real arithmetic functions

**Framework**: Accelerate  
**Role**: API Collection

Perform element-wise operations on vectors of real values.

#### Overview

The vDSP library provides a suite of general-purpose, high-performance arithmetic functions that are alternatives to `for` loops and `map` when you apply operations on collections of floating-point values.

See [Using vDSP for vector-based arithmetic](./using-vdsp-for-vector-based-arithmetic.md) for a summary of available operations.

## Topics

### Binary addition operations
- [static func add<T, U>(T, U) -> [Float]](./vdsp/add%28_,_%29-7swvf.md)
  Returns the single-precision element-wise sum of two vectors.
- [static func add<T, U>(T, U) -> [Double]](./vdsp/add%28_,_%29-2ftxc.md)
  Returns the double-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](./vdsp/add%28_,_,result%29-3vzwi.md)
  Calculates the single-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](./vdsp/add%28_,_,result%29-338hl.md)
  Calculates the double-precision element-wise sum of two vectors.
### Binary subtraction operations
- [static func subtract<T, U>(U, T) -> [Float]](./vdsp/subtract%28_,_%29-9xmo8.md)
  Returns the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U>(U, T) -> [Double]](./vdsp/subtract%28_,_%29-8o5ai.md)
  Returns the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](./vdsp/subtract%28_,_,result%29-2p3fa.md)
  Calculates the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](./vdsp/subtract%28_,_,result%29-1ianx.md)
  Calculates the double-precision element-wise subtraction of two vectors.
### Binary multiplication operations
- [static func multiply<T, U>(T, U) -> [Float]](./vdsp/multiply%28_,_%29-9zgw.md)
  Returns the single-precision element-wise product of two vectors.
- [static func multiply<T, U>(T, U) -> [Double]](./vdsp/multiply%28_,_%29-1ckqt.md)
  Returns the double-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](./vdsp/multiply%28_,_,result%29-155f3.md)
  Calculates the single-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](./vdsp/multiply%28_,_,result%29-3ptjl.md)
  Calculates the double-precision element-wise product of two vectors.
### Binary division operations
- [static func divide<T, U>(T, U) -> [Float]](./vdsp/divide%28_,_%29-6nfsi.md)
  Returns the single-precision element-wise division of two vectors.
- [static func divide<T, U>(T, U) -> [Double]](./vdsp/divide%28_,_%29-8swnm.md)
  Returns the double-precision element-wise division of two vectors.
- [static func divide<T, U, V>(T, U, result: inout V)](./vdsp/divide%28_,_,result%29-7ejy9.md)
  Calculates the single-precision element-wise division of two vectors.
- [static func divide<T, U, V>(T, U, result: inout V)](./vdsp/divide%28_,_,result%29-6gtmm.md)
  Calculates the double-precision element-wise division of two vectors.
### Binary addition and subtraction operations
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](./vdsp/addsubtract%28_,_,addresult,subtractresult%29-6qxwa.md)
  Calculates the single-precision element-wise sum and subtraction of two vectors.
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](./vdsp/addsubtract%28_,_,addresult,subtractresult%29-avzd.md)
  Calculates the double-precision element-wise sum and subtraction of two vectors.
### Ternary add-multiply operations
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Float]](./vdsp/multiply%28addition,_%29-7t59.md)
  Returns the single-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Double]](./vdsp/multiply%28addition,_%29-1wt61.md)
  Returns the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), U, result: inout V)](./vdsp/multiply%28addition,_,result%29-3jqts.md)
  Calculates the single-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), U, result: inout V)](./vdsp/multiply%28addition,_,result%29-5sqwo.md)
  Calculates the double-precision element-wise product of a vector and the sum of two vectors.
### Ternary multiply-add operations
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Float]](./vdsp/add%28multiplication,_%29-9bgb2.md)
  Returns the single-precision element-wise sum of a vector and the product of two vectors.
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Double]](./vdsp/add%28multiplication,_%29-4667v.md)
  Returns the double-precision element-wise sum of a vector and the product of two vectors.
- [static func add<S, T, U, V>(multiplication: (a: S, b: T), U, result: inout V)](./vdsp/add%28multiplication,_,result%29-1srn8.md)
  Calculates the single-precision element-wise sum of a vector and the product of two vectors.
- [static func add<S, T, U, V>(multiplication: (a: S, b: T), U, result: inout V)](./vdsp/add%28multiplication,_,result%29-48vyq.md)
  Calculates the double-precision element-wise sum of a vector and the product of two vectors.
### Ternary multiply-subtract operations
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Float]](./vdsp/subtract%28multiplication,_%29-6u3sp.md)
  Returns the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Double]](./vdsp/subtract%28multiplication,_%29-9gphg.md)
  Returns the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](./vdsp/subtract%28multiplication,_,result%29-6b91s.md)
  Calculates the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](./vdsp/subtract%28multiplication,_,result%29-3f2bw.md)
  Calculates the double-precision element-wise difference of a vector and the product of two vectors.
### Ternary subtract-multiply operations
- [static func multiply<S, T, U>(subtraction: (a: S, b: T), U) -> [Float]](./vdsp/multiply%28subtraction,_%29-6y7g6.md)
  Returns the single-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<S, T, U>(subtraction: (a: S, b: T), U) -> [Double]](./vdsp/multiply%28subtraction,_%29-8a8sr.md)
  Returns the double-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<S, T, U, V>(subtraction: (a: S, b: T), U, result: inout V)](./vdsp/multiply%28subtraction,_,result%29-36flg.md)
  Calculates the single-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<S, T, U, V>(subtraction: (a: S, b: T), U, result: inout V)](./vdsp/multiply%28subtraction,_,result%29-ziw4.md)
  Calculates the double-precision element-wise product of a vector and the differences of two vectors.
### Quaternary multiply-multiply-subtract operations
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Float]](./vdsp/subtract%28multiplication,multiplication%29-1ghyu.md)
  Returns the single-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Double]](./vdsp/subtract%28multiplication,multiplication%29-22a4b.md)
  Returns the double-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U, V>(multiplication: (a: T, b: U), multiplication: (c: R, d: S), result: inout V)](./vdsp/subtract%28multiplication,multiplication,result%29-8ofjj.md)
  Calculates the single-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U, V>(multiplication: (a: T, b: U), multiplication: (c: R, d: S), result: inout V)](./vdsp/subtract%28multiplication,multiplication,result%29-48y6i.md)
  Calculates the double-precision element-wise difference of the products of two pairs of vectors.
### Quaternary add-add-multiply operations
- [static func multiply<S, T, U>(addition: (a: S, b: T), addition: (c: U, d: U)) -> [Float]](./vdsp/multiply%28addition,addition%29-1voy8.md)
  Returns the single-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U>(addition: (a: S, b: T), addition: (c: U, d: U)) -> [Double]](./vdsp/multiply%28addition,addition%29-7rs.md)
  Returns the double-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), addition: (c: U, d: U), result: inout V)](./vdsp/multiply%28addition,addition,result%29-7p21q.md)
  Calculates the single-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), addition: (c: U, d: U), result: inout V)](./vdsp/multiply%28addition,addition,result%29-89hgk.md)
  Calculates the double-precision element-wise product of the sums of two pairs of vectors.
### Quaternary subtract-subtract-multiply operations
- [static func multiply<R, S, T, U>(subtraction: (a: R, b: S), subtraction: (c: T, d: U)) -> [Float]](./vdsp/multiply%28subtraction,subtraction%29-1rnom.md)
  Returns the single-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U>(subtraction: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double]](./vdsp/multiply%28subtraction,subtraction%29-5pv8p.md)
  Returns the double-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U, V>(subtraction: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](./vdsp/multiply%28subtraction,subtraction,result%29-rubk.md)
  Calculates the single-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U, V>(subtraction: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](./vdsp/multiply%28subtraction,subtraction,result%29-4jjy5.md)
  Calculates the double-precision element-wise product of the differences of two pairs of vectors.
### Quaternary add-subtract-multiply operations
- [static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Float]](./vdsp/multiply%28addition,subtraction%29-6h89l.md)
  Returns the single-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double]](./vdsp/multiply%28addition,subtraction%29-7qfik.md)
  Returns the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U, V>(addition: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](./vdsp/multiply%28addition,subtraction,result%29-j688.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U, V>(addition: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](./vdsp/multiply%28addition,subtraction,result%29-2rldl.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors.

## See Also

### Vector-vector arithmetic
- [Complex basic arithmetic](./complex-basic-arithmetic.md)
  Perform element-wise operations on vectors of complex values.
- [Integer arithmetic](./integer-arithmetic.md)
  Perform element-wise operations on vectors of integer values.
- [Linear averaging functions](./linear-averaging-functions.md)
  Calculate the element-wise linear average of two vectors.
- [Polynomial evaluation](./polynomial-evaluation.md)
  Evaluate polynomials using coefficients and independent variables that you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vector-vector-real-arithmetic-functions)*