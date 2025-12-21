# Vector-scalar real arithmetic functions

**Framework**: Accelerate

Perform element-wise operations on combinations of vectors of real values and scalar values.

#### Overview

The vDSP library provides a suite of general-purpose, high-performance arithmetic functions that are alternatives to `for` loops and `map` when you apply operations on collections of floating-point values.

See [`Using vDSP for vector-based arithmetic`](using-vdsp-for-vector-based-arithmetic.md) for a summary of available operations.

## Topics

### Vector-scalar addition operations
- [static func add<U>(Float, U) -> [Float]](vdsp/add(_:_:)-53nh9.md)
  Returns the single-precision element-wise sum of a vector and a scalar value.
- [static func add<U>(Double, U) -> [Double]](vdsp/add(_:_:)-9mv1a.md)
  Returns the double-precision element-wise sum of a vector and a scalar value.
- [static func add<U, V>(Float, U, result: inout V)](vdsp/add(_:_:result:)-2w0o9.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<U, V>(Double, U, result: inout V)](vdsp/add(_:_:result:)-2531u.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
### Vector-scalar multiplication operations
- [static func multiply<U>(Float, U) -> [Float]](vdsp/multiply(_:_:)-993yp.md)
  Returns the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<U>(Double, U) -> [Double]](vdsp/multiply(_:_:)-9dxnc.md)
  Returns the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<U, V>(Float, U, result: inout V)](vdsp/multiply(_:_:result:)-358cn.md)
  Calculates the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<U, V>(Double, U, result: inout V)](vdsp/multiply(_:_:result:)-4xorc.md)
  Calculates the double-precision element-wise product of a vector and a scalar value.
### Vector-scalar division operations
- [static func divide<U>(U, Float) -> [Float]](vdsp/divide(_:_:)-1uqmz.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<U>(U, Double) -> [Double]](vdsp/divide(_:_:)-9nb4j.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<U, V>(U, Float, result: inout V)](vdsp/divide(_:_:result:)-5hwb2.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<U, V>(U, Double, result: inout V)](vdsp/divide(_:_:result:)-44mff.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
### Scalar-vector division operations
- [static func divide<U>(Float, U) -> [Float]](vdsp/divide(_:_:)-70npt.md)
  Returns the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(Double, U) -> [Double]](vdsp/divide(_:_:)-73m8v.md)
  Returns the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(Float, U, result: inout V)](vdsp/divide(_:_:result:)-3emlk.md)
  Calculates the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(Double, U, result: inout V)](vdsp/divide(_:_:result:)-18qa3.md)
  Calculates the double-precision element-wise division of a scalar value and a vector.
### Vector-vector-scalar add-multiply operations
- [static func multiply<T, U>(addition: (a: T, b: U), Float) -> [Float]](vdsp/multiply(addition:_:)-4fnbx.md)
  Returns the single-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<T, U>(addition: (a: T, b: U), Double) -> [Double]](vdsp/multiply(addition:_:)-4c9in.md)
  Returns the double-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<T, U, V>(addition: (a: T, b: U), Float, result: inout V)](vdsp/multiply(addition:_:result:)-6x7xq.md)
  Calculates the single-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<T, U, V>(addition: (a: T, b: U), Double, result: inout V)](vdsp/multiply(addition:_:result:)-7dujy.md)
  Calculates the double-precision element-wise product of the sum of two vectors and a scalar value.
### Vector-vector-scalar subtract-multiply operations
- [static func multiply<T, U>(subtraction: (a: T, b: U), Float) -> [Float]](vdsp/multiply(subtraction:_:)-106pt.md)
  Returns the single-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<T, U>(subtraction: (a: T, b: U), Double) -> [Double]](vdsp/multiply(subtraction:_:)-3gxn3.md)
  Returns the double-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<T, U, V>(subtraction: (a: T, b: U), Float, result: inout V)](vdsp/multiply(subtraction:_:result:)-5l106.md)
  Calculates the single-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<T, U, V>(subtraction: (a: T, b: U), Double, result: inout V)](vdsp/multiply(subtraction:_:result:)-lhn7.md)
  Calculates the double-precision element-wise product of the difference of two vectors and a scalar value.
### Vector-scalar-vector multiply-subtract operations
- [static func subtract<T, U>(multiplication: (a: U, b: Float), T) -> [Float]](vdsp/subtract(multiplication:_:)-3zm6l.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<T, U>(multiplication: (a: U, b: Double), T) -> [Double]](vdsp/subtract(multiplication:_:)-2hhme.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Float), T, result: inout V)](vdsp/subtract(multiplication:_:result:)-86gx3.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Double), T, result: inout V)](vdsp/subtract(multiplication:_:result:)-9p12h.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
### Vector-vector-scalar multiply-add operations
- [static func add<T, U>(multiplication: (a: T, b: U), Float) -> [Float]](vdsp/add(multiplication:_:)-36vhq.md)
  Returns the single-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<T, U>(multiplication: (a: T, b: U), Double) -> [Double]](vdsp/add(multiplication:_:)-9dxlr.md)
  Returns the double-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<T, U, V>(multiplication: (a: T, b: U), Float, result: inout V)](vdsp/add(multiplication:_:result:)-8dau.md)
  Calculates the single-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<T, U, V>(multiplication: (a: T, b: U), Double, result: inout V)](vdsp/add(multiplication:_:result:)-2wpvw.md)
  Calculates the double-precision element-wise sum of the product of two vectors, and a scalar value.
### Vector-scalar-vector multiply-add operations
- [static func add<T, U>(multiplication: (a: T, b: Float), U) -> [Float]](vdsp/add(multiplication:_:)-7aut1.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Double), U) -> [Double]](vdsp/add(multiplication:_:)-1bsuq.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U, V>(multiplication: (a: T, b: Float), U, result: inout V)](vdsp/add(multiplication:_:result:)-6n4jf.md)
  Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U, V>(multiplication: (a: T, b: Double), U, result: inout V)](vdsp/add(multiplication:_:result:)-2i5om.md)
  Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
### Vector-scalar-scalar multiply-add operations
- [static func add<U>(multiplication: (a: U, b: Float), Float) -> [Float]](vdsp/add(multiplication:_:)-3tw93.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<U>(multiplication: (a: U, b: Double), Double) -> [Double]](vdsp/add(multiplication:_:)-4e3tj.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<U, V>(multiplication: (a: U, b: Float), Float, result: inout V)](vdsp/add(multiplication:_:result:)-1rob9.md)
  Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a scalar.
- [static func add<U, V>(multiplication: (a: U, b: Double), Double, result: inout V)](vdsp/add(multiplication:_:result:)-8ixx9.md)
  Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a scalar.
### Vector-scalar-vector-scalar multiply-multiply-add operations
- [static func add<T, U>(multiplication: (a: T, b: Float), multiplication: (c: U, d: Float)) -> [Float]](vdsp/add(multiplication:multiplication:)-8rjh8.md)
  Returns the single-precision element-wise addition of two vector-scalar products.
- [static func add<T, U>(multiplication: (a: T, b: Double), multiplication: (c: U, d: Double)) -> [Double]](vdsp/add(multiplication:multiplication:)-563ub.md)
  Returns the double-precision element-wise addition of two vector-scalar products.
- [static func add<T, U, V>(multiplication: (a: T, b: Float), multiplication: (c: U, d: Float), result: inout V)](vdsp/add(multiplication:multiplication:result:)-663mk.md)
  Calculates the single-precision element-wise addition of two vector-scalar products.
- [static func add<T, U, V>(multiplication: (a: T, b: Double), multiplication: (c: U, d: Double), result: inout V)](vdsp/add(multiplication:multiplication:result:)-9xe8k.md)
  Calculates the double-precision element-wise addition of two vector-scalar products.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vector-scalar-real-arithmetic-functions)*