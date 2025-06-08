# Vector-vector real arithmetic functions

**Framework**: Accelerate

Perform element-wise operations on vectors of real values.

#### Overview

The vDSP library provides a suite of general-purpose, high-performance arithmetic functions that are alternatives to `for` loops and `map` when you apply operations on collections of floating-point values.

See [`Using vDSP for vector-based arithmetic`](using-vdsp-for-vector-based-arithmetic.md) for a summary of available operations.

## Topics

### Binary addition operations
- [static func add<T, U>(T, U) -> [Float]](vdsp/add(_:_:)-7swvf.md)
  Returns the single-precision element-wise sum of two vectors.
- [static func add<T, U>(T, U) -> [Double]](vdsp/add(_:_:)-2ftxc.md)
  Returns the double-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-3vzwi.md)
  Calculates the single-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-338hl.md)
  Calculates the double-precision element-wise sum of two vectors.
- [vDSP_vadd](vdsp_vadd.md)
  Calculates the single-precision element-wise sum of two vectors, using the specified stride.
- [vDSP_vaddD](vdsp_vaddd.md)
  Calculates the double-precision element-wise sum of two vectors, using the specified stride.
### Binary subtraction operations
- [static func subtract<T, U>(U, T) -> [Float]](vdsp/subtract(_:_:)-9xmo8.md)
  Returns the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U>(U, T) -> [Double]](vdsp/subtract(_:_:)-8o5ai.md)
  Returns the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](vdsp/subtract(_:_:result:)-2p3fa.md)
  Calculates the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](vdsp/subtract(_:_:result:)-1ianx.md)
  Calculates the double-precision element-wise subtraction of two vectors.
- [vDSP_vsub](vdsp_vsub.md)
  Calculates the single-precision element-wise subtraction of two vectors, using the specified stride.
- [vDSP_vsubD](vdsp_vsubd.md)
  Calculates the double-precision element-wise subtraction of two vectors, using the specified stride.
### Binary multiplication operations
- [static func multiply<T, U>(T, U) -> [Float]](vdsp/multiply(_:_:)-9zgw.md)
  Returns the single-precision element-wise product of two vectors.
- [static func multiply<T, U>(T, U) -> [Double]](vdsp/multiply(_:_:)-1ckqt.md)
  Returns the double-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](vdsp/multiply(_:_:result:)-155f3.md)
  Calculates the single-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](vdsp/multiply(_:_:result:)-3ptjl.md)
  Calculates the double-precision element-wise product of two vectors.
- [vDSP_vmul](vdsp_vmul.md)
  Calculates the single-precision element-wise product of two vectors, using the specified stride.
- [vDSP_vmulD](vdsp_vmuld.md)
  Calculates the double-precision element-wise product of two vectors, using the specified stride.
### Binary division operations
- [static func divide<T, U>(T, U) -> [Float]](vdsp/divide(_:_:)-6nfsi.md)
  Returns the single-precision element-wise division of two vectors.
- [static func divide<T, U>(T, U) -> [Double]](vdsp/divide(_:_:)-8swnm.md)
  Returns the double-precision element-wise division of two vectors.
- [static func divide<T, U, V>(T, U, result: inout V)](vdsp/divide(_:_:result:)-7ejy9.md)
  Calculates the single-precision element-wise division of two vectors.
- [static func divide<T, U, V>(T, U, result: inout V)](vdsp/divide(_:_:result:)-6gtmm.md)
  Calculates the double-precision element-wise division of two vectors.
- [vDSP_vdiv](vdsp_vdiv.md)
  Calculates the single-precision element-wise division of two vectors, using the specified stride.
- [vDSP_vdivD](vdsp_vdivd.md)
  Calculates the double-precision element-wise division of two vectors, using the specified stride.
### Binary addition and subtraction operations
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](vdsp/addsubtract(_:_:addresult:subtractresult:)-6qxwa.md)
  Calculates the single-precision element-wise sum and subtraction of two vectors.
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](vdsp/addsubtract(_:_:addresult:subtractresult:)-avzd.md)
  Calculates the double-precision element-wise sum and subtraction of two vectors.
- [vDSP_vaddsub](vdsp_vaddsub.md)
  Calculates the single-precision element-wise sum and subtraction of two vectors, using the specified stride.
- [vDSP_vaddsubD](vdsp_vaddsubd.md)
  Calculates the double-precision element-wise sum and subtraction of two vectors, using the specified stride.
### Ternary add-multiply operations
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Float]](vdsp/multiply(addition:_:)-7t59.md)
  Returns the single-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Double]](vdsp/multiply(addition:_:)-1wt61.md)
  Returns the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), U, result: inout V)](vdsp/multiply(addition:_:result:)-3jqts.md)
  Calculates the single-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), U, result: inout V)](vdsp/multiply(addition:_:result:)-5sqwo.md)
  Calculates the double-precision element-wise product of a vector and the sum of two vectors.
- [vDSP_vam](vdsp_vam.md)
  Calculates the single-precision element-wise product of a vector and the sum of two vectors, using the specified stride.
- [vDSP_vamD](vdsp_vamd.md)
  Calculates the double-precision element-wise product of a vector and the sum of two vectors, using the specified stride.
### Ternary multiply-add operations
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Float]](vdsp/add(multiplication:_:)-9bgb2.md)
  Returns the single-precision element-wise sum of a vector and the product of two vectors.
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Double]](vdsp/add(multiplication:_:)-4667v.md)
  Returns the double-precision element-wise sum of a vector and the product of two vectors.
- [static func add<S, T, U, V>(multiplication: (a: S, b: T), U, result: inout V)](vdsp/add(multiplication:_:result:)-1srn8.md)
  Calculates the single-precision element-wise sum of a vector and the product of two vectors.
- [static func add<S, T, U, V>(multiplication: (a: S, b: T), U, result: inout V)](vdsp/add(multiplication:_:result:)-48vyq.md)
  Calculates the double-precision element-wise sum of a vector and the product of two vectors.
- [vDSP_vma](vdsp_vma.md)
  Calculates the single-precision element-wise sum of a vector and the product of two vectors, using the specified stride.
- [vDSP_vmaD](vdsp_vmad.md)
  Calculates the double-precision element-wise sum of a vector and the product of two vectors, using the specified stride.
### Ternary multiply-subtract operations
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Float]](vdsp/subtract(multiplication:_:)-6u3sp.md)
  Returns the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Double]](vdsp/subtract(multiplication:_:)-9gphg.md)
  Returns the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](vdsp/subtract(multiplication:_:result:)-6b91s.md)
  Calculates the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](vdsp/subtract(multiplication:_:result:)-3f2bw.md)
  Calculates the double-precision element-wise difference of a vector and the product of two vectors.
- [vDSP_vmsb](vdsp_vmsb.md)
  Calculates the single-precision element-wise difference of a vector and the product of two vectors, using the specified stride.
- [vDSP_vmsbD](vdsp_vmsbd.md)
  Calculates the double-precision element-wise difference of a vector and the product of two vectors, using the specified stride.
### Ternary subtract-multiply operations
- [static func multiply<S, T, U>(subtraction: (a: S, b: T), U) -> [Float]](vdsp/multiply(subtraction:_:)-6y7g6.md)
  Returns the single-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<S, T, U>(subtraction: (a: S, b: T), U) -> [Double]](vdsp/multiply(subtraction:_:)-8a8sr.md)
  Returns the double-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<S, T, U, V>(subtraction: (a: S, b: T), U, result: inout V)](vdsp/multiply(subtraction:_:result:)-36flg.md)
  Calculates the single-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<S, T, U, V>(subtraction: (a: S, b: T), U, result: inout V)](vdsp/multiply(subtraction:_:result:)-ziw4.md)
  Calculates the double-precision element-wise product of a vector and the differences of two vectors.
- [vDSP_vsbm](vdsp_vsbm.md)
  Calculates the single-precision element-wise product of a vector and the differences of two vectors, using the specified stride.
- [vDSP_vsbmD](vdsp_vsbmd.md)
  Calculates the double-precision element-wise product of a vector and the differences of two vectors, using the specified stride.
### Quaternary multiply-multiply-add operations
- [vDSP_vmma](vdsp_vmma.md)
  Calculates the single-precision element-wise sum of the products of two pairs of vectors, using the specified stride.
- [vDSP_vmmaD](vdsp_vmmad.md)
  Calculates the double-precision element-wise sum of the products of two pairs of vectors, using the specified stride.
### Quaternary multiply-multiply-subtract operations
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Float]](vdsp/subtract(multiplication:multiplication:)-1ghyu.md)
  Returns the single-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Double]](vdsp/subtract(multiplication:multiplication:)-22a4b.md)
  Returns the double-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U, V>(multiplication: (a: T, b: U), multiplication: (c: R, d: S), result: inout V)](vdsp/subtract(multiplication:multiplication:result:)-8ofjj.md)
  Calculates the single-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U, V>(multiplication: (a: T, b: U), multiplication: (c: R, d: S), result: inout V)](vdsp/subtract(multiplication:multiplication:result:)-48y6i.md)
  Calculates the double-precision element-wise difference of the products of two pairs of vectors.
- [vDSP_vmmsb](vdsp_vmmsb.md)
  Calculates the single-precision element-wise difference of the products of two pairs of vectors, using the specified stride.
- [vDSP_vmmsbD](vdsp_vmmsbd.md)
  Calculates the double-precision element-wise difference of the products of two pairs of vectors, using the specified stride.
### Quaternary add-add-multiply operations
- [static func multiply<S, T, U>(addition: (a: S, b: T), addition: (c: U, d: U)) -> [Float]](vdsp/multiply(addition:addition:)-1voy8.md)
  Returns the single-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U>(addition: (a: S, b: T), addition: (c: U, d: U)) -> [Double]](vdsp/multiply(addition:addition:)-7rs.md)
  Returns the double-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), addition: (c: U, d: U), result: inout V)](vdsp/multiply(addition:addition:result:)-7p21q.md)
  Calculates the single-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), addition: (c: U, d: U), result: inout V)](vdsp/multiply(addition:addition:result:)-89hgk.md)
  Calculates the double-precision element-wise product of the sums of two pairs of vectors.
- [vDSP_vaam](vdsp_vaam.md)
  Calculates the single-precision element-wise product of the sums of two pairs of vectors, using the specified stride.
- [vDSP_vaamD](vdsp_vaamd.md)
  Calculates the double-precision element-wise product of the sums of two pairs of vectors, using the specified stride.
### Quaternary subtract-subtract-multiply operations
- [static func multiply<R, S, T, U>(subtraction: (a: R, b: S), subtraction: (c: T, d: U)) -> [Float]](vdsp/multiply(subtraction:subtraction:)-1rnom.md)
  Returns the single-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U>(subtraction: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double]](vdsp/multiply(subtraction:subtraction:)-5pv8p.md)
  Returns the double-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U, V>(subtraction: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](vdsp/multiply(subtraction:subtraction:result:)-rubk.md)
  Calculates the single-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U, V>(subtraction: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](vdsp/multiply(subtraction:subtraction:result:)-4jjy5.md)
  Calculates the double-precision element-wise product of the differences of two pairs of vectors.
- [vDSP_vsbsbm](vdsp_vsbsbm.md)
  Calculates the single-precision element-wise product of the differences of two pairs of vectors, using the specified stride.
- [vDSP_vsbsbmD](vdsp_vsbsbmd.md)
  Calculates the double-precision element-wise product of the differences of two pairs of vectors, using the specified stride.
### Quaternary add-subtract-multiply operations
- [static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Float]](vdsp/multiply(addition:subtraction:)-6h89l.md)
  Returns the single-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double]](vdsp/multiply(addition:subtraction:)-7qfik.md)
  Returns the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U, V>(addition: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](vdsp/multiply(addition:subtraction:result:)-j688.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U, V>(addition: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](vdsp/multiply(addition:subtraction:result:)-2rldl.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [vDSP_vasbm](vdsp_vasbm.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors, using the specified stride.
- [vDSP_vasbmD](vdsp_vasbmd.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors, using the specified stride.

## See Also

- [Complex basic arithmetic](complex-basic-arithmetic.md)
  Perform elementwise operations on vectors of complex values.
- [Integer arithmetic](integer-arithmetic.md)
  Perform elementwise operations on vectors of integer values.
- [Linear averaging functions](linear-averaging-functions.md)
  Calculate the element-wise linear average of two vectors.
- [Polynomial evaluation](polynomial-evaluation.md)
  Evaluate polynomials using coefficients and independent variables that you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vector-vector-real-arithmetic-functions)*