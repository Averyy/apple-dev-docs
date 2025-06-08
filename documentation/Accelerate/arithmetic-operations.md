# Arithmetic operations

**Framework**: Accelerate

Perform operations on large vectors.

## Topics

### Addition
- [static func add<U>(Double, U) -> [Double]](vdsp/add(_:_:)-9mv1a.md)
  Returns the double-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Double]](vdsp/add(_:_:)-2ftxc.md)
  Returns the double-precision element-wise sum of two vectors.
- [static func add<U>(Float, U) -> [Float]](vdsp/add(_:_:)-53nh9.md)
  Returns the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Float]](vdsp/add(_:_:)-7swvf.md)
  Returns the single-precision element-wise sum of two vectors.
- [static func add<U, V>(Double, U, result: inout V)](vdsp/add(_:_:result:)-2531u.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<U, V>(Float, U, result: inout V)](vdsp/add(_:_:result:)-2w0o9.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-338hl.md)
  Calculates the double-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-3vzwi.md)
  Calculates the single-precision element-wise sum of two vectors.
- [static func add(DSPSplitComplex, to: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/add(_:to:count:result:)-g1dk.md)
  Calculates the single-precision elementwise sum of the supplied complex vectors.
- [static func add(DSPDoubleSplitComplex, to: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](vdsp/add(_:to:count:result:)-75np9.md)
  Calculates the double-precision elementwise sum of the supplied complex vectors.
- [static func add<U>(multiplication: (a: U, b: Double), Double) -> [Double]](vdsp/add(multiplication:_:)-4e3tj.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Double), U) -> [Double]](vdsp/add(multiplication:_:)-1bsuq.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: U), Double) -> [Double]](vdsp/add(multiplication:_:)-9dxlr.md)
  Returns the double-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Double]](vdsp/add(multiplication:_:)-4667v.md)
  Returns the double-precision element-wise sum of a vector and the product of two vectors.
- [static func add<U>(multiplication: (a: U, b: Float), Float) -> [Float]](vdsp/add(multiplication:_:)-3tw93.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Float), U) -> [Float]](vdsp/add(multiplication:_:)-7aut1.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: U), Float) -> [Float]](vdsp/add(multiplication:_:)-36vhq.md)
  Returns the single-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Float]](vdsp/add(multiplication:_:)-9bgb2.md)
  Returns the single-precision element-wise sum of a vector and the product of two vectors.
- [static func add<U, V>(multiplication: (a: U, b: Double), Double, result: inout V)](vdsp/add(multiplication:_:result:)-8ixx9.md)
  Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U, V>(multiplication: (a: T, b: Double), U, result: inout V)](vdsp/add(multiplication:_:result:)-2i5om.md)
  Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<U, V>(multiplication: (a: U, b: Float), Float, result: inout V)](vdsp/add(multiplication:_:result:)-1rob9.md)
  Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U, V>(multiplication: (a: T, b: Float), U, result: inout V)](vdsp/add(multiplication:_:result:)-6n4jf.md)
  Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U, V>(multiplication: (a: T, b: U), Double, result: inout V)](vdsp/add(multiplication:_:result:)-2wpvw.md)
  Calculates the double-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<T, U, V>(multiplication: (a: T, b: U), Float, result: inout V)](vdsp/add(multiplication:_:result:)-8dau.md)
  Calculates the single-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<S, T, U, V>(multiplication: (a: S, b: T), U, result: inout V)](vdsp/add(multiplication:_:result:)-48vyq.md)
  Calculates the double-precision element-wise sum of a vector and the product of two vectors.
- [static func add<S, T, U, V>(multiplication: (a: S, b: T), U, result: inout V)](vdsp/add(multiplication:_:result:)-1srn8.md)
  Calculates the single-precision element-wise sum of a vector and the product of two vectors.
- [static func add<T, U>(multiplication: (a: T, b: Double), multiplication: (c: U, d: Double)) -> [Double]](vdsp/add(multiplication:multiplication:)-563ub.md)
  Returns the double-precision element-wise addition of two vector-scalar products.
- [static func add<R, S, T, U>(multiplication: (a: R, b: S), multiplication: (c: T, d: U)) -> [Double]](vdsp/add(multiplication:multiplication:)-boma.md)
  Returns the double-precision elementwise product of a vector and a vector, added to a second product of a vector and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Float), multiplication: (c: U, d: Float)) -> [Float]](vdsp/add(multiplication:multiplication:)-8rjh8.md)
  Returns the single-precision element-wise addition of two vector-scalar products.
- [static func add<R, S, T, U>(multiplication: (a: R, b: S), multiplication: (c: T, d: U)) -> [Float]](vdsp/add(multiplication:multiplication:)-xxxa.md)
  Returns the single-precision elementwise product of a vector and a vector, added to a second product of a vector and a vector.
- [static func add<T, U, V>(multiplication: (a: T, b: Double), multiplication: (c: U, d: Double), result: inout V)](vdsp/add(multiplication:multiplication:result:)-9xe8k.md)
  Calculates the double-precision element-wise addition of two vector-scalar products.
- [static func add<T, U, V>(multiplication: (a: T, b: Float), multiplication: (c: U, d: Float), result: inout V)](vdsp/add(multiplication:multiplication:result:)-663mk.md)
  Calculates the single-precision element-wise addition of two vector-scalar products.
- [static func add<R, S, T, U, V>(multiplication: (a: R, b: S), multiplication: (c: T, d: U), result: inout V)](vdsp/add(multiplication:multiplication:result:)-5s7xu.md)
  Calculates the double-precision elementwise product of a vector and a vector, added to a second product of a vector and a vector.
- [static func add<R, S, T, U, V>(multiplication: (a: R, b: S), multiplication: (c: T, d: U), result: inout V)](vdsp/add(multiplication:multiplication:result:)-4g1u3.md)
  Calculates the single-precision elementwise product of a vector and a vector, added to a second product of a vector and a vector.
### Subtraction
- [static func subtract<T, U>(U, T) -> [Double]](vdsp/subtract(_:_:)-8o5ai.md)
  Returns the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U>(U, T) -> [Float]](vdsp/subtract(_:_:)-9xmo8.md)
  Returns the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](vdsp/subtract(_:_:result:)-1ianx.md)
  Calculates the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](vdsp/subtract(_:_:result:)-2p3fa.md)
  Calculates the single-precision element-wise subtraction of two vectors.
- [static func subtract(DSPSplitComplex, from: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/subtract(_:from:count:result:)-4p5xd.md)
  Calculates the single-precision elementwise subtraction of a complex vector from a complex vector.
- [static func subtract(DSPDoubleSplitComplex, from: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](vdsp/subtract(_:from:count:result:)-80zi9.md)
  Calculates the double-precision elementwise subtraction of a complex vector from a complex vector.
- [static func subtract<T, U>(multiplication: (a: U, b: Double), T) -> [Double]](vdsp/subtract(multiplication:_:)-2hhme.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Double]](vdsp/subtract(multiplication:_:)-9gphg.md)
  Returns the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U>(multiplication: (a: U, b: Float), T) -> [Float]](vdsp/subtract(multiplication:_:)-3zm6l.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Float]](vdsp/subtract(multiplication:_:)-6u3sp.md)
  Returns the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Double), T, result: inout V)](vdsp/subtract(multiplication:_:result:)-9p12h.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Float), T, result: inout V)](vdsp/subtract(multiplication:_:result:)-86gx3.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](vdsp/subtract(multiplication:_:result:)-3f2bw.md)
  Calculates the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](vdsp/subtract(multiplication:_:result:)-6b91s.md)
  Calculates the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Double]](vdsp/subtract(multiplication:multiplication:)-22a4b.md)
  Returns the double-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Float]](vdsp/subtract(multiplication:multiplication:)-1ghyu.md)
  Returns the single-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U, V>(multiplication: (a: T, b: U), multiplication: (c: R, d: S), result: inout V)](vdsp/subtract(multiplication:multiplication:result:)-48y6i.md)
  Calculates the double-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U, V>(multiplication: (a: T, b: U), multiplication: (c: R, d: S), result: inout V)](vdsp/subtract(multiplication:multiplication:result:)-8ofjj.md)
  Calculates the single-precision element-wise difference of the products of two pairs of vectors.
### Addition and Subtraction
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](vdsp/addsubtract(_:_:addresult:subtractresult:)-avzd.md)
  Calculates the double-precision element-wise sum and subtraction of two vectors.
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](vdsp/addsubtract(_:_:addresult:subtractresult:)-6qxwa.md)
  Calculates the single-precision element-wise sum and subtraction of two vectors.
### Multiplication
- [static func multiply<U>(Double, U) -> [Double]](vdsp/multiply(_:_:)-9dxnc.md)
  Returns the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Double]](vdsp/multiply(_:_:)-1ckqt.md)
  Returns the double-precision element-wise product of two vectors.
- [static func multiply<U>(Float, U) -> [Float]](vdsp/multiply(_:_:)-993yp.md)
  Returns the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Float]](vdsp/multiply(_:_:)-9zgw.md)
  Returns the single-precision element-wise product of two vectors.
- [static func multiply<U, V>(Double, U, result: inout V)](vdsp/multiply(_:_:result:)-4xorc.md)
  Calculates the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<U, V>(Float, U, result: inout V)](vdsp/multiply(_:_:result:)-358cn.md)
  Calculates the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U, V>(T, U, result: inout V)](vdsp/multiply(_:_:result:)-3ptjl.md)
  Calculates the double-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](vdsp/multiply(_:_:result:)-155f3.md)
  Calculates the single-precision element-wise product of two vectors.
- [static func multiply(DSPSplitComplex, by: DSPSplitComplex, count: Int, useConjugate: Bool, result: inout DSPSplitComplex)](vdsp/multiply(_:by:count:useconjugate:result:)-4idx8.md)
  Calculates the product of two complex single-precision vectors, optionally conjugating one of them.
- [static func multiply(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, useConjugate: Bool, result: inout DSPDoubleSplitComplex)](vdsp/multiply(_:by:count:useconjugate:result:)-79r8u.md)
  Calculates the elementwise product of two complex double-precision vectors, optionally conjugating one of them.
- [static func multiply<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](vdsp/multiply(_:by:result:)-8b9eq.md)
  Calculates the double-precision elementwise product of a complex vector and a real vector.
- [static func multiply<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](vdsp/multiply(_:by:result:)-8jyhd.md)
  Calculates the single-precision elementwise product of a complex vector and a real vector.
- [static func multiply<T, U>(addition: (a: T, b: U), Double) -> [Double]](vdsp/multiply(addition:_:)-4c9in.md)
  Returns the double-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Double]](vdsp/multiply(addition:_:)-1wt61.md)
  Returns the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<T, U>(addition: (a: T, b: U), Float) -> [Float]](vdsp/multiply(addition:_:)-4fnbx.md)
  Returns the single-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Float]](vdsp/multiply(addition:_:)-7t59.md)
  Returns the single-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<T, U, V>(addition: (a: T, b: U), Double, result: inout V)](vdsp/multiply(addition:_:result:)-7dujy.md)
  Calculates the double-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<T, U, V>(addition: (a: T, b: U), Float, result: inout V)](vdsp/multiply(addition:_:result:)-6x7xq.md)
  Calculates the single-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), U, result: inout V)](vdsp/multiply(addition:_:result:)-5sqwo.md)
  Calculates the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), U, result: inout V)](vdsp/multiply(addition:_:result:)-3jqts.md)
  Calculates the single-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U>(addition: (a: S, b: T), addition: (c: U, d: U)) -> [Double]](vdsp/multiply(addition:addition:)-7rs.md)
  Returns the double-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U>(addition: (a: S, b: T), addition: (c: U, d: U)) -> [Float]](vdsp/multiply(addition:addition:)-1voy8.md)
  Returns the single-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), addition: (c: U, d: U), result: inout V)](vdsp/multiply(addition:addition:result:)-89hgk.md)
  Calculates the double-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), addition: (c: U, d: U), result: inout V)](vdsp/multiply(addition:addition:result:)-7p21q.md)
  Calculates the single-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double]](vdsp/multiply(addition:subtraction:)-7qfik.md)
  Returns the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Float]](vdsp/multiply(addition:subtraction:)-6h89l.md)
  Returns the single-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U, V>(addition: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](vdsp/multiply(addition:subtraction:result:)-2rldl.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U, V>(addition: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](vdsp/multiply(addition:subtraction:result:)-j688.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<T, U>(subtraction: (a: T, b: U), Double) -> [Double]](vdsp/multiply(subtraction:_:)-3gxn3.md)
  Returns the double-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<S, T, U>(subtraction: (a: S, b: T), U) -> [Double]](vdsp/multiply(subtraction:_:)-8a8sr.md)
  Returns the double-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<T, U>(subtraction: (a: T, b: U), Float) -> [Float]](vdsp/multiply(subtraction:_:)-106pt.md)
  Returns the single-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<S, T, U>(subtraction: (a: S, b: T), U) -> [Float]](vdsp/multiply(subtraction:_:)-6y7g6.md)
  Returns the single-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<T, U, V>(subtraction: (a: T, b: U), Double, result: inout V)](vdsp/multiply(subtraction:_:result:)-lhn7.md)
  Calculates the double-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<T, U, V>(subtraction: (a: T, b: U), Float, result: inout V)](vdsp/multiply(subtraction:_:result:)-5l106.md)
  Calculates the single-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<S, T, U, V>(subtraction: (a: S, b: T), U, result: inout V)](vdsp/multiply(subtraction:_:result:)-ziw4.md)
  Calculates the double-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<S, T, U, V>(subtraction: (a: S, b: T), U, result: inout V)](vdsp/multiply(subtraction:_:result:)-36flg.md)
  Calculates the single-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<R, S, T, U>(subtraction: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double]](vdsp/multiply(subtraction:subtraction:)-5pv8p.md)
  Returns the double-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U>(subtraction: (a: R, b: S), subtraction: (c: T, d: U)) -> [Float]](vdsp/multiply(subtraction:subtraction:)-1rnom.md)
  Returns the single-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U, V>(subtraction: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](vdsp/multiply(subtraction:subtraction:result:)-4jjy5.md)
  Calculates the double-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U, V>(subtraction: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](vdsp/multiply(subtraction:subtraction:result:)-rubk.md)
  Calculates the single-precision element-wise product of the differences of two pairs of vectors.
### Division
- [static func divide<U>(Double, U) -> [Double]](vdsp/divide(_:_:)-73m8v.md)
  Returns the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Double) -> [Double]](vdsp/divide(_:_:)-9nb4j.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U>(T, U) -> [Double]](vdsp/divide(_:_:)-8swnm.md)
  Returns the double-precision element-wise division of two vectors.
- [static func divide<U>(Float, U) -> [Float]](vdsp/divide(_:_:)-70npt.md)
  Returns the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Float) -> [Float]](vdsp/divide(_:_:)-1uqmz.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U>(T, U) -> [Float]](vdsp/divide(_:_:)-6nfsi.md)
  Returns the single-precision element-wise division of two vectors.
- [static func divide<U, V>(Double, U, result: inout V)](vdsp/divide(_:_:result:)-18qa3.md)
  Calculates the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(Float, U, result: inout V)](vdsp/divide(_:_:result:)-3emlk.md)
  Calculates the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(U, Double, result: inout V)](vdsp/divide(_:_:result:)-44mff.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<U, V>(U, Float, result: inout V)](vdsp/divide(_:_:result:)-5hwb2.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U, V>(T, U, result: inout V)](vdsp/divide(_:_:result:)-6gtmm.md)
  Calculates the double-precision element-wise division of two vectors.
- [static func divide<T, U, V>(T, U, result: inout V)](vdsp/divide(_:_:result:)-7ejy9.md)
  Calculates the single-precision element-wise division of two vectors.
- [static func divide(DSPSplitComplex, by: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/divide(_:by:count:result:)-9chz5.md)
  Calculates the single-precision elementwise division of a complex vector by a complex vector.
- [static func divide(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](vdsp/divide(_:by:count:result:)-57jlj.md)
  Calculates the double-precision elementwise division of a complex vector by a complex vector.
- [static func divide<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](vdsp/divide(_:by:result:)-66qch.md)
  Calculates the single-precision elementwise division of a complex vector by a real vector.
- [static func divide<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](vdsp/divide(_:by:result:)-402v9.md)
  Calculates the double-precision elementwise division of a complex vector by a complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/arithmetic-operations)*