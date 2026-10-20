# Arithmetic operations

**Framework**: Accelerate  
**Role**: API Collection

Perform operations on large vectors.

## Topics

### Addition
- [static func add<U>(Double, U) -> [Double]](./vdsp/add%28_,_%29-9mv1a.md)
  Returns the double-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Double]](./vdsp/add%28_,_%29-2ftxc.md)
  Returns the double-precision element-wise sum of two vectors.
- [static func add<U>(Float, U) -> [Float]](./vdsp/add%28_,_%29-53nh9.md)
  Returns the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Float]](./vdsp/add%28_,_%29-7swvf.md)
  Returns the single-precision element-wise sum of two vectors.
- [static func add<U, V>(Double, U, result: inout V)](./vdsp/add%28_,_,result%29-2531u.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<U, V>(Float, U, result: inout V)](./vdsp/add%28_,_,result%29-2w0o9.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U, V>(T, U, result: inout V)](./vdsp/add%28_,_,result%29-338hl.md)
  Calculates the double-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](./vdsp/add%28_,_,result%29-3vzwi.md)
  Calculates the single-precision element-wise sum of two vectors.
- [static func add(DSPSplitComplex, to: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./vdsp/add%28_,to,count,result%29-g1dk.md)
  Calculates the single-precision element-wise sum of the supplied complex vectors.
- [static func add(DSPDoubleSplitComplex, to: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](./vdsp/add%28_,to,count,result%29-75np9.md)
  Calculates the double-precision element-wise sum of the supplied complex vectors.
- [static func add<U>(multiplication: (a: U, b: Double), Double) -> [Double]](./vdsp/add%28multiplication,_%29-4e3tj.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Double), U) -> [Double]](./vdsp/add%28multiplication,_%29-1bsuq.md)
  Returns the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: U), Double) -> [Double]](./vdsp/add%28multiplication,_%29-9dxlr.md)
  Returns the double-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Double]](./vdsp/add%28multiplication,_%29-4667v.md)
  Returns the double-precision element-wise sum of a vector and the product of two vectors.
- [static func add<U>(multiplication: (a: U, b: Float), Float) -> [Float]](./vdsp/add%28multiplication,_%29-3tw93.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Float), U) -> [Float]](./vdsp/add%28multiplication,_%29-7aut1.md)
  Returns the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U>(multiplication: (a: T, b: U), Float) -> [Float]](./vdsp/add%28multiplication,_%29-36vhq.md)
  Returns the single-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<S, T, U>(multiplication: (a: S, b: T), U) -> [Float]](./vdsp/add%28multiplication,_%29-9bgb2.md)
  Returns the single-precision element-wise sum of a vector and the product of two vectors.
- [static func add<U, V>(multiplication: (a: U, b: Double), Double, result: inout V)](./vdsp/add%28multiplication,_,result%29-8ixx9.md)
  Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a scalar.
- [static func add<T, U, V>(multiplication: (a: T, b: Double), U, result: inout V)](./vdsp/add%28multiplication,_,result%29-2i5om.md)
  Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<U, V>(multiplication: (a: U, b: Float), Float, result: inout V)](./vdsp/add%28multiplication,_,result%29-1rob9.md)
  Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a scalar.
- [static func add<T, U, V>(multiplication: (a: T, b: Float), U, result: inout V)](./vdsp/add%28multiplication,_,result%29-6n4jf.md)
  Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a vector.
- [static func add<T, U, V>(multiplication: (a: T, b: U), Double, result: inout V)](./vdsp/add%28multiplication,_,result%29-2wpvw.md)
  Calculates the double-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<T, U, V>(multiplication: (a: T, b: U), Float, result: inout V)](./vdsp/add%28multiplication,_,result%29-8dau.md)
  Calculates the single-precision element-wise sum of the product of two vectors, and a scalar value.
- [static func add<S, T, U, V>(multiplication: (a: S, b: T), U, result: inout V)](./vdsp/add%28multiplication,_,result%29-48vyq.md)
  Calculates the double-precision element-wise sum of a vector and the product of two vectors.
- [static func add<S, T, U, V>(multiplication: (a: S, b: T), U, result: inout V)](./vdsp/add%28multiplication,_,result%29-1srn8.md)
  Calculates the single-precision element-wise sum of a vector and the product of two vectors.
- [static func add<T, U>(multiplication: (a: T, b: Double), multiplication: (c: U, d: Double)) -> [Double]](./vdsp/add%28multiplication,multiplication%29-563ub.md)
  Returns the double-precision element-wise addition of two vector-scalar products.
- [static func add<R, S, T, U>(multiplication: (a: R, b: S), multiplication: (c: T, d: U)) -> [Double]](./vdsp/add%28multiplication,multiplication%29-boma.md)
  Returns the double-precision element-wise product of a vector and a vector, added to a second product of a vector and a vector.
- [static func add<T, U>(multiplication: (a: T, b: Float), multiplication: (c: U, d: Float)) -> [Float]](./vdsp/add%28multiplication,multiplication%29-8rjh8.md)
  Returns the single-precision element-wise addition of two vector-scalar products.
- [static func add<R, S, T, U>(multiplication: (a: R, b: S), multiplication: (c: T, d: U)) -> [Float]](./vdsp/add%28multiplication,multiplication%29-xxxa.md)
  Returns the single-precision element-wise product of a vector and a vector, added to a second product of a vector and a vector.
- [static func add<T, U, V>(multiplication: (a: T, b: Double), multiplication: (c: U, d: Double), result: inout V)](./vdsp/add%28multiplication,multiplication,result%29-9xe8k.md)
  Calculates the double-precision element-wise addition of two vector-scalar products.
- [static func add<T, U, V>(multiplication: (a: T, b: Float), multiplication: (c: U, d: Float), result: inout V)](./vdsp/add%28multiplication,multiplication,result%29-663mk.md)
  Calculates the single-precision element-wise addition of two vector-scalar products.
- [static func add<R, S, T, U, V>(multiplication: (a: R, b: S), multiplication: (c: T, d: U), result: inout V)](./vdsp/add%28multiplication,multiplication,result%29-5s7xu.md)
  Calculates the double-precision element-wise product of a vector and a vector, added to a second product of a vector and a vector.
- [static func add<R, S, T, U, V>(multiplication: (a: R, b: S), multiplication: (c: T, d: U), result: inout V)](./vdsp/add%28multiplication,multiplication,result%29-4g1u3.md)
  Calculates the single-precision element-wise product of a vector and a vector, added to a second product of a vector and a vector.
### Subtraction
- [static func subtract<T, U>(U, T) -> [Double]](./vdsp/subtract%28_,_%29-8o5ai.md)
  Returns the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U>(U, T) -> [Float]](./vdsp/subtract%28_,_%29-9xmo8.md)
  Returns the single-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](./vdsp/subtract%28_,_,result%29-1ianx.md)
  Calculates the double-precision element-wise subtraction of two vectors.
- [static func subtract<T, U, V>(U, T, result: inout V)](./vdsp/subtract%28_,_,result%29-2p3fa.md)
  Calculates the single-precision element-wise subtraction of two vectors.
- [static func subtract(DSPSplitComplex, from: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./vdsp/subtract%28_,from,count,result%29-4p5xd.md)
  Calculates the single-precision element-wise subtraction of a complex vector from a complex vector.
- [static func subtract(DSPDoubleSplitComplex, from: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](./vdsp/subtract%28_,from,count,result%29-80zi9.md)
  Calculates the double-precision element-wise subtraction of a complex vector from a complex vector.
- [static func subtract<T, U>(multiplication: (a: U, b: Double), T) -> [Double]](./vdsp/subtract%28multiplication,_%29-2hhme.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Double]](./vdsp/subtract%28multiplication,_%29-9gphg.md)
  Returns the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U>(multiplication: (a: U, b: Float), T) -> [Float]](./vdsp/subtract%28multiplication,_%29-3zm6l.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U>(multiplication: (a: T, b: U), S) -> [Float]](./vdsp/subtract%28multiplication,_%29-6u3sp.md)
  Returns the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Double), T, result: inout V)](./vdsp/subtract%28multiplication,_,result%29-9p12h.md)
  Calculates the double-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<T, U, V>(multiplication: (a: U, b: Float), T, result: inout V)](./vdsp/subtract%28multiplication,_,result%29-86gx3.md)
  Calculates the single-precision element-wise difference of the product of a vector and a scalar value, and a vector.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](./vdsp/subtract%28multiplication,_,result%29-3f2bw.md)
  Calculates the double-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<S, T, U, V>(multiplication: (a: T, b: U), S, result: inout V)](./vdsp/subtract%28multiplication,_,result%29-6b91s.md)
  Calculates the single-precision element-wise difference of a vector and the product of two vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Double]](./vdsp/subtract%28multiplication,multiplication%29-22a4b.md)
  Returns the double-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U>(multiplication: (a: T, b: U), multiplication: (c: R, d: S)) -> [Float]](./vdsp/subtract%28multiplication,multiplication%29-1ghyu.md)
  Returns the single-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U, V>(multiplication: (a: T, b: U), multiplication: (c: R, d: S), result: inout V)](./vdsp/subtract%28multiplication,multiplication,result%29-48y6i.md)
  Calculates the double-precision element-wise difference of the products of two pairs of vectors.
- [static func subtract<R, S, T, U, V>(multiplication: (a: T, b: U), multiplication: (c: R, d: S), result: inout V)](./vdsp/subtract%28multiplication,multiplication,result%29-8ofjj.md)
  Calculates the single-precision element-wise difference of the products of two pairs of vectors.
### Addition and Subtraction
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](./vdsp/addsubtract%28_,_,addresult,subtractresult%29-avzd.md)
  Calculates the double-precision element-wise sum and subtraction of two vectors.
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](./vdsp/addsubtract%28_,_,addresult,subtractresult%29-6qxwa.md)
  Calculates the single-precision element-wise sum and subtraction of two vectors.
### Multiplication
- [static func multiply<U>(Double, U) -> [Double]](./vdsp/multiply%28_,_%29-9dxnc.md)
  Returns the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Double]](./vdsp/multiply%28_,_%29-1ckqt.md)
  Returns the double-precision element-wise product of two vectors.
- [static func multiply<U>(Float, U) -> [Float]](./vdsp/multiply%28_,_%29-993yp.md)
  Returns the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Float]](./vdsp/multiply%28_,_%29-9zgw.md)
  Returns the single-precision element-wise product of two vectors.
- [static func multiply<U, V>(Double, U, result: inout V)](./vdsp/multiply%28_,_,result%29-4xorc.md)
  Calculates the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<U, V>(Float, U, result: inout V)](./vdsp/multiply%28_,_,result%29-358cn.md)
  Calculates the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U, V>(T, U, result: inout V)](./vdsp/multiply%28_,_,result%29-3ptjl.md)
  Calculates the double-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](./vdsp/multiply%28_,_,result%29-155f3.md)
  Calculates the single-precision element-wise product of two vectors.
- [static func multiply(DSPSplitComplex, by: DSPSplitComplex, count: Int, useConjugate: Bool, result: inout DSPSplitComplex)](./vdsp/multiply%28_,by,count,useconjugate,result%29-4idx8.md)
  Calculates the product of two complex single-precision vectors, optionally conjugating one of them.
- [static func multiply(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, useConjugate: Bool, result: inout DSPDoubleSplitComplex)](./vdsp/multiply%28_,by,count,useconjugate,result%29-79r8u.md)
  Calculates the element-wise product of two complex double-precision vectors, optionally conjugating one of them.
- [static func multiply<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](./vdsp/multiply%28_,by,result%29-8b9eq.md)
  Calculates the double-precision element-wise product of a complex vector and a real vector.
- [static func multiply<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](./vdsp/multiply%28_,by,result%29-8jyhd.md)
  Calculates the single-precision element-wise product of a complex vector and a real vector.
- [static func multiply<T, U>(addition: (a: T, b: U), Double) -> [Double]](./vdsp/multiply%28addition,_%29-4c9in.md)
  Returns the double-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Double]](./vdsp/multiply%28addition,_%29-1wt61.md)
  Returns the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<T, U>(addition: (a: T, b: U), Float) -> [Float]](./vdsp/multiply%28addition,_%29-4fnbx.md)
  Returns the single-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Float]](./vdsp/multiply%28addition,_%29-7t59.md)
  Returns the single-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<T, U, V>(addition: (a: T, b: U), Double, result: inout V)](./vdsp/multiply%28addition,_,result%29-7dujy.md)
  Calculates the double-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<T, U, V>(addition: (a: T, b: U), Float, result: inout V)](./vdsp/multiply%28addition,_,result%29-6x7xq.md)
  Calculates the single-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), U, result: inout V)](./vdsp/multiply%28addition,_,result%29-5sqwo.md)
  Calculates the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), U, result: inout V)](./vdsp/multiply%28addition,_,result%29-3jqts.md)
  Calculates the single-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<S, T, U>(addition: (a: S, b: T), addition: (c: U, d: U)) -> [Double]](./vdsp/multiply%28addition,addition%29-7rs.md)
  Returns the double-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U>(addition: (a: S, b: T), addition: (c: U, d: U)) -> [Float]](./vdsp/multiply%28addition,addition%29-1voy8.md)
  Returns the single-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), addition: (c: U, d: U), result: inout V)](./vdsp/multiply%28addition,addition,result%29-89hgk.md)
  Calculates the double-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<S, T, U, V>(addition: (a: S, b: T), addition: (c: U, d: U), result: inout V)](./vdsp/multiply%28addition,addition,result%29-7p21q.md)
  Calculates the single-precision element-wise product of the sums of two pairs of vectors.
- [static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double]](./vdsp/multiply%28addition,subtraction%29-7qfik.md)
  Returns the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U>(addition: (a: R, b: S), subtraction: (c: T, d: U)) -> [Float]](./vdsp/multiply%28addition,subtraction%29-6h89l.md)
  Returns the single-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U, V>(addition: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](./vdsp/multiply%28addition,subtraction,result%29-2rldl.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<R, S, T, U, V>(addition: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](./vdsp/multiply%28addition,subtraction,result%29-j688.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors.
- [static func multiply<T, U>(subtraction: (a: T, b: U), Double) -> [Double]](./vdsp/multiply%28subtraction,_%29-3gxn3.md)
  Returns the double-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<S, T, U>(subtraction: (a: S, b: T), U) -> [Double]](./vdsp/multiply%28subtraction,_%29-8a8sr.md)
  Returns the double-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<T, U>(subtraction: (a: T, b: U), Float) -> [Float]](./vdsp/multiply%28subtraction,_%29-106pt.md)
  Returns the single-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<S, T, U>(subtraction: (a: S, b: T), U) -> [Float]](./vdsp/multiply%28subtraction,_%29-6y7g6.md)
  Returns the single-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<T, U, V>(subtraction: (a: T, b: U), Double, result: inout V)](./vdsp/multiply%28subtraction,_,result%29-lhn7.md)
  Calculates the double-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<T, U, V>(subtraction: (a: T, b: U), Float, result: inout V)](./vdsp/multiply%28subtraction,_,result%29-5l106.md)
  Calculates the single-precision element-wise product of the difference of two vectors and a scalar value.
- [static func multiply<S, T, U, V>(subtraction: (a: S, b: T), U, result: inout V)](./vdsp/multiply%28subtraction,_,result%29-ziw4.md)
  Calculates the double-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<S, T, U, V>(subtraction: (a: S, b: T), U, result: inout V)](./vdsp/multiply%28subtraction,_,result%29-36flg.md)
  Calculates the single-precision element-wise product of a vector and the differences of two vectors.
- [static func multiply<R, S, T, U>(subtraction: (a: R, b: S), subtraction: (c: T, d: U)) -> [Double]](./vdsp/multiply%28subtraction,subtraction%29-5pv8p.md)
  Returns the double-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U>(subtraction: (a: R, b: S), subtraction: (c: T, d: U)) -> [Float]](./vdsp/multiply%28subtraction,subtraction%29-1rnom.md)
  Returns the single-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U, V>(subtraction: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](./vdsp/multiply%28subtraction,subtraction,result%29-4jjy5.md)
  Calculates the double-precision element-wise product of the differences of two pairs of vectors.
- [static func multiply<R, S, T, U, V>(subtraction: (a: R, b: S), subtraction: (c: T, d: U), result: inout V)](./vdsp/multiply%28subtraction,subtraction,result%29-rubk.md)
  Calculates the single-precision element-wise product of the differences of two pairs of vectors.
### Division
- [static func divide<U>(Double, U) -> [Double]](./vdsp/divide%28_,_%29-73m8v.md)
  Returns the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Double) -> [Double]](./vdsp/divide%28_,_%29-9nb4j.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U>(T, U) -> [Double]](./vdsp/divide%28_,_%29-8swnm.md)
  Returns the double-precision element-wise division of two vectors.
- [static func divide<U>(Float, U) -> [Float]](./vdsp/divide%28_,_%29-70npt.md)
  Returns the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U>(U, Float) -> [Float]](./vdsp/divide%28_,_%29-1uqmz.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U>(T, U) -> [Float]](./vdsp/divide%28_,_%29-6nfsi.md)
  Returns the single-precision element-wise division of two vectors.
- [static func divide<U, V>(Double, U, result: inout V)](./vdsp/divide%28_,_,result%29-18qa3.md)
  Calculates the double-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(Float, U, result: inout V)](./vdsp/divide%28_,_,result%29-3emlk.md)
  Calculates the single-precision element-wise division of a scalar value and a vector.
- [static func divide<U, V>(U, Double, result: inout V)](./vdsp/divide%28_,_,result%29-44mff.md)
  Calculates the double-precision element-wise division of a vector and a scalar value.
- [static func divide<U, V>(U, Float, result: inout V)](./vdsp/divide%28_,_,result%29-5hwb2.md)
  Calculates the single-precision element-wise division of a vector and a scalar value.
- [static func divide<T, U, V>(T, U, result: inout V)](./vdsp/divide%28_,_,result%29-6gtmm.md)
  Calculates the double-precision element-wise division of two vectors.
- [static func divide<T, U, V>(T, U, result: inout V)](./vdsp/divide%28_,_,result%29-7ejy9.md)
  Calculates the single-precision element-wise division of two vectors.
- [static func divide(DSPSplitComplex, by: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./vdsp/divide%28_,by,count,result%29-9chz5.md)
  Calculates the single-precision element-wise division of a complex vector by a complex vector.
- [static func divide(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](./vdsp/divide%28_,by,count,result%29-57jlj.md)
  Calculates the double-precision element-wise division of a complex vector by a complex vector.
- [static func divide<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](./vdsp/divide%28_,by,result%29-66qch.md)
  Calculates the single-precision element-wise division of a complex vector by a real vector.
- [static func divide<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](./vdsp/divide%28_,by,result%29-402v9.md)
  Calculates the double-precision element-wise division of a complex vector by a complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/arithmetic-operations)*