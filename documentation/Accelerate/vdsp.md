# vDSP

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

An enumeration that acts as a namespace for Swift overlays to vDSP.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
enum vDSP
```

## Mentions

- [Performing Fourier transforms on interleaved-complex data](./performing-fourier-transforms-on-interleaved-complex-data.md)

## Topics

### Type Methods
- [static func absolute<U>(U) -> [Double]](./vdsp/absolute%28_%29-9c3ge.md)
  Returns the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U>(U) -> [Float]](./vdsp/absolute%28_%29-5ehc1.md)
  Returns the absolute value of each element in the supplied single-precision vector.
- [static func absolute<V>(DSPSplitComplex, result: inout V)](./vdsp/absolute%28_,result%29-9x5jn.md)
  Calculates the absolute value of each element in the supplied single-precision complex vector.
- [static func absolute<V>(DSPDoubleSplitComplex, result: inout V)](./vdsp/absolute%28_,result%29-1wu9x.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector.
- [static func absolute<U, V>(U, result: inout V)](./vdsp/absolute%28_,result%29-657bd.md)
  Calculates the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U, V>(U, result: inout V)](./vdsp/absolute%28_,result%29-4pigo.md)
  Calculates the absolute value of each element in the supplied single-precision vector.
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
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](./vdsp/addsubtract%28_,_,addresult,subtractresult%29-avzd.md)
  Calculates the double-precision element-wise sum and subtraction of two vectors.
- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](./vdsp/addsubtract%28_,_,addresult,subtractresult%29-6qxwa.md)
  Calculates the single-precision element-wise sum and subtraction of two vectors.
- [static func amplitudeToDecibels<U>(U, zeroReference: Double) -> [Double]](./vdsp/amplitudetodecibels%28_,zeroreference%29-2cgik.md)
  Returns double-precision amplitude values converted to decibel values.
- [static func amplitudeToDecibels<U>(U, zeroReference: Float) -> [Float]](./vdsp/amplitudetodecibels%28_,zeroreference%29-88bpy.md)
  Returns single-precision amplitude values converted to decibels.
- [static func clear<V>(inout V)](./vdsp/clear%28_%29-1t76j.md)
  Populates a double-precision vector with zeros.
- [static func clear<V>(inout V)](./vdsp/clear%28_%29-5f0gr.md)
  Populates a single-precision vector with zeros.
- [static func clip<U>(U, to: ClosedRange<Double>) -> [Double]](./vdsp/clip%28_,to%29-8jsic.md)
  Returns the elements of a double-precision vector clipped to the specified range.
- [static func clip<U>(U, to: ClosedRange<Float>) -> [Float]](./vdsp/clip%28_,to%29-20gz4.md)
  Returns the elements of a single-precision vector clipped to the specified range.
- [static func clip<U, V>(U, to: ClosedRange<Double>, result: inout V)](./vdsp/clip%28_,to,result%29-3lbii.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [static func clip<U, V>(U, to: ClosedRange<Float>, result: inout V)](./vdsp/clip%28_,to,result%29-84zw9.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [static func conjugate(DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](./vdsp/conjugate%28_,count,result%29-v5m9.md)
  Calculates the complex conjugate of the values in a single-precision vector.
- [static func conjugate(DSPDoubleSplitComplex, count: Int, result: inout DSPDoubleSplitComplex)](./vdsp/conjugate%28_,count,result%29-89mrk.md)
  Calculates the complex conjugate of the values in a double-precision vector.
- [static func convert<U, V>(amplitude: U, toDecibels: inout V, zeroReference: Double)](./vdsp/convert%28amplitude,todecibels,zeroreference%29-4io4p.md)
  Converts double-precision amplitude values to decibel values.
- [static func convert<U, V>(amplitude: U, toDecibels: inout V, zeroReference: Float)](./vdsp/convert%28amplitude,todecibels,zeroreference%29-83uy1.md)
  Converts single-precision amplitude values to decibel values.
- [static func convert(interleavedComplexVector: [DSPDoubleComplex], toSplitComplexVector: inout DSPDoubleSplitComplex)](./vdsp/convert%28interleavedcomplexvector,tosplitcomplexvector%29-8cqd4.md)
  Converts the contents of an interleaved double-precision complex vector to a split complex vector.
- [static func convert(interleavedComplexVector: [DSPComplex], toSplitComplexVector: inout DSPSplitComplex)](./vdsp/convert%28interleavedcomplexvector,tosplitcomplexvector%29-4lnrf.md)
  Converts the contents of an interleaved single-precision complex vector to a split complex vector.
- [static func convert<U, V>(polarCoordinates: U, toRectangularCoordinates: inout V)](./vdsp/convert%28polarcoordinates,torectangularcoordinates%29-22zz0.md)
  Converts double-precision polar coordinates to rectangular coordinates.
- [static func convert<U, V>(polarCoordinates: U, toRectangularCoordinates: inout V)](./vdsp/convert%28polarcoordinates,torectangularcoordinates%29-3vpjf.md)
  Converts single-precision polar coordinates to rectangular coordinates.
- [static func convert<U, V>(power: U, toDecibels: inout V, zeroReference: Double)](./vdsp/convert%28power,todecibels,zeroreference%29-3aiv4.md)
  Converts double-precision power values to decibel values.
- [static func convert<U, V>(power: U, toDecibels: inout V, zeroReference: Float)](./vdsp/convert%28power,todecibels,zeroreference%29-5u3vs.md)
  Converts single-precision power values to decibel values.
- [static func convert<U, V>(rectangularCoordinates: U, toPolarCoordinates: inout V)](./vdsp/convert%28rectangularcoordinates,topolarcoordinates%29-84131.md)
  Converts double-precision rectangular coordinates to polar coordinates.
- [static func convert<U, V>(rectangularCoordinates: U, toPolarCoordinates: inout V)](./vdsp/convert%28rectangularcoordinates,topolarcoordinates%29-1zi4t.md)
  Converts single-precision rectangular coordinates to polar coordinates.
- [static func convert(splitComplexVector: DSPDoubleSplitComplex, toInterleavedComplexVector: inout [DSPDoubleComplex])](./vdsp/convert%28splitcomplexvector,tointerleavedcomplexvector%29-9v193.md)
  Converts the contents of a split double-precision complex vector to an interleaved vector.
- [static func convert(splitComplexVector: DSPSplitComplex, toInterleavedComplexVector: inout [DSPComplex])](./vdsp/convert%28splitcomplexvector,tointerleavedcomplexvector%29-65gyx.md)
  Converts the contents of a split single-precision complex vector to an interleaved vector.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-698ye.md)
  Converts double-precision values to single-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-2ejgr.md)
  Converts single-precision values to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-3jcmt.md)
  Converts 8-bit signed integers to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-3bomv.md)
  Converts 8-bit signed integers to single-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-3j3tb.md)
  Converts 16-bit signed integers to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-93xn9.md)
  Converts 16-bit signed integers to single-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-7itb5.md)
  Converts 32-bit signed integers to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-7pknu.md)
  Converts 32-bit signed integers to single-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-1jwgk.md)
  Converts 8-bit unsigned integers to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-7jdvz.md)
  Converts 8-bit unsigned integers to single-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-4sj10.md)
  Converts 16-bit unsigned integers to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-1ajdy.md)
  Converts 16-bit unsigned integers to single-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-4es14.md)
  Converts 32-bit unsigned integers to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-9orm4.md)
  Converts 32-bit unsigned integers to single-precision values.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-2ig4y.md)
  Converts double-precision values to 8-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-4xlg5.md)
  Converts double-precision values to 16-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-3sxak.md)
  Converts double-precision values to 32-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-3sgv7.md)
  Converts double-precision values to 8-bit unsigned integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-2oiwm.md)
  Converts double-precision values to 16-bit unsigned integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-3t71v.md)
  Converts double-precision values to 32-bit unsigned integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-48635.md)
  Converts single-precision values to 8-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-3tofv.md)
  Converts single-precision values to 16-bit unsigned integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-2dsry.md)
  Converts single-precision values to 32-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-9qu7f.md)
  Converts single-precision values to 8-bit unsigned integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-slaa.md)
  Converts single-precision values to 16-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](./vdsp/convertelements%28of,to,rounding%29-14dc1.md)
  Converts single-precision values to 32-bit unsigned integers.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U) -> [Double]](./vdsp/convolve%28_,rowcount,columncount,with3x3kernel%29-1r5oa.md)
  Returns the 2D convolution of a double-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U) -> [Float]](./vdsp/convolve%28_,rowcount,columncount,with3x3kernel%29-7qjgw.md)
  Returns the 2D convolution of a single-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U, result: inout V)](./vdsp/convolve%28_,rowcount,columncount,with3x3kernel,result%29-34k76.md)
  Calculates the 2D convolution of a double-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U, result: inout V)](./vdsp/convolve%28_,rowcount,columncount,with3x3kernel,result%29-2worq.md)
  Calculates the 2D convolution of a single-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U) -> [Double]](./vdsp/convolve%28_,rowcount,columncount,with5x5kernel%29-7cvh9.md)
  Returns the 2D convolution of a double-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U) -> [Float]](./vdsp/convolve%28_,rowcount,columncount,with5x5kernel%29-101d6.md)
  Returns the 2D convolution of a single-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U, result: inout V)](./vdsp/convolve%28_,rowcount,columncount,with5x5kernel,result%29-g68r.md)
  Calculates the 2D convolution of a double-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U, result: inout V)](./vdsp/convolve%28_,rowcount,columncount,with5x5kernel,result%29-76h85.md)
  Calculates the 2D convolution of a single-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int) -> [Double]](./vdsp/convolve%28_,rowcount,columncount,withkernel,kernelrowcount,kernelcolumncount%29-1sswe.md)
  Returns the 2D convolution of a double-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int) -> [Float]](./vdsp/convolve%28_,rowcount,columncount,withkernel,kernelrowcount,kernelcolumncount%29-267yl.md)
  Returns the 2D convolution of a single-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int, result: inout V)](./vdsp/convolve%28_,rowcount,columncount,withkernel,kernelrowcount,kernelcolumncount,result%29-4211m.md)
  Calculates the 2D convolution of a double-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int, result: inout V)](./vdsp/convolve%28_,rowcount,columncount,withkernel,kernelrowcount,kernelcolumncount,result%29-5hiro.md)
  Calculates the 2D convolution of a single-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U>(T, withKernel: U) -> [Double]](./vdsp/convolve%28_,withkernel%29-1nv65.md)
  Returns the 1D convolution of a double-precision vector.
- [static func convolve<T, U>(T, withKernel: U) -> [Float]](./vdsp/convolve%28_,withkernel%29-4p0rt.md)
  Returns the 1D convolution of a single-precision vector.
- [static func convolve<T, U, V>(T, withKernel: U, result: inout V)](./vdsp/convolve%28_,withkernel,result%29-8j76l.md)
  Calculates the 1D convolution of a double-precision vector.
- [static func convolve<T, U, V>(T, withKernel: U, result: inout V)](./vdsp/convolve%28_,withkernel,result%29-2z66w.md)
  Calculates the 1D convolution of a single-precision vector.
- [static func copy(DSPSplitComplex, to: inout DSPSplitComplex, count: Int)](./vdsp/copy%28_,to,count%29-96jr5.md)
  Copies a complex single-precision vector.
- [static func copy(DSPDoubleSplitComplex, to: inout DSPDoubleSplitComplex, count: Int)](./vdsp/copy%28_,to,count%29-7zpro.md)
  Copies a complex double-precision vector.
- [static func correlate<T, U>(T, withKernel: U) -> [Double]](./vdsp/correlate%28_,withkernel%29-7f6o0.md)
  Returns the correlation of a double-precision signal vector and a filter vector.
- [static func correlate<T, U>(T, withKernel: U) -> [Float]](./vdsp/correlate%28_,withkernel%29-9sol8.md)
  Returns the correlation of a single-precision signal vector and a filter vector.
- [static func correlate<T, U, V>(T, withKernel: U, result: inout V)](./vdsp/correlate%28_,withkernel,result%29-1lb82.md)
  Calculates the correlation of a double-precision signal vector and a filter vector.
- [static func correlate<T, U, V>(T, withKernel: U, result: inout V)](./vdsp/correlate%28_,withkernel,result%29-377zj.md)
  Calculates the correlation of a single-precision signal vector and a filter vector.
- [static func countZeroCrossings<U>(U) -> UInt](./vdsp/countzerocrossings%28_%29-3vfmd.md)
  Returns the number of zero crossings in a double-precision vector.
- [static func countZeroCrossings<U>(U) -> UInt](./vdsp/countzerocrossings%28_%29-3btsl.md)
  Returns the number of zero crossings in a single-precision vector.
- [static func distanceSquared<U, V>(U, V) -> Double](./vdsp/distancesquared%28_,_%29-3oub3.md)
  Returns the double-precision distance squared between two points in n-dimensional space.
- [static func distanceSquared<U, V>(U, V) -> Float](./vdsp/distancesquared%28_,_%29-2dvb6.md)
  Returns the single-precision distance squared between two points in n-dimensional space.
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
- [static func doubleToFloat<U>(U) -> [Float]](./vdsp/doubletofloat%28_%29.md)
  Returns single-precision values converted from a double-precision source.
- [static func downsample<T, U>(U, decimationFactor: Int, filter: T) -> [Double]](./vdsp/downsample%28_,decimationfactor,filter%29-1o8it.md)
  Returns the downsampled double-precision vector.
- [static func downsample<T, U>(U, decimationFactor: Int, filter: T) -> [Float]](./vdsp/downsample%28_,decimationfactor,filter%29-40d8o.md)
  Returns the downsampled single-precision vector.
- [static func downsample<T, U, V>(U, decimationFactor: Int, filter: T, result: inout V)](./vdsp/downsample%28_,decimationfactor,filter,result%29-2y1iv.md)
  Calculates the downsampled double-precision vector.
- [static func downsample<T, U, V>(U, decimationFactor: Int, filter: T, result: inout V)](./vdsp/downsample%28_,decimationfactor,filter,result%29-1g4a.md)
  Calculates the downsampled single-precision vector.
- [static func evaluatePolynomial<U>(usingCoefficients: [Double], withVariables: U) -> [Double]](./vdsp/evaluatepolynomial%28usingcoefficients,withvariables%29-31vi2.md)
  Returns a double-precision evaluated polynomial using specified coefficients and variables.
- [static func evaluatePolynomial<U>(usingCoefficients: [Float], withVariables: U) -> [Float]](./vdsp/evaluatepolynomial%28usingcoefficients,withvariables%29-7mznu.md)
  Returns a single-precision evaluated polynomial using specified coefficients and variables.
- [static func evaluatePolynomial<U, V>(usingCoefficients: [Double], withVariables: U, result: inout V)](./vdsp/evaluatepolynomial%28usingcoefficients,withvariables,result%29-2ncdh.md)
  Evaluates a double-precision polynomial using specified coefficients and variables.
- [static func evaluatePolynomial<U, V>(usingCoefficients: [Float], withVariables: U, result: inout V)](./vdsp/evaluatepolynomial%28usingcoefficients,withvariables,result%29-6eaoc.md)
  Evaluates a single-precision polynomial using specified coefficients and variables.
- [static func fill<V>(inout V, with: Double)](./vdsp/fill%28_,with%29-91ud3.md)
  Populates a double-precision vector with a specified scalar value.
- [static func fill<V>(inout V, with: Float)](./vdsp/fill%28_,with%29-7gfq3.md)
  Populates a single-precision vector with a specified scalar value.
- [static func floatToDouble<U>(U) -> [Double]](./vdsp/floattodouble%28_%29.md)
  Returns double-precision values converted from a single-precision source.
- [static func floatingPointToInteger<T, U>(T, integerType: U.Type, rounding: vDSP.RoundingMode) -> [U]](./vdsp/floatingpointtointeger%28_,integertype,rounding%29-33dtm.md)
  Returns double-precision values converted to integer values.
- [static func floatingPointToInteger<T, U>(T, integerType: U.Type, rounding: vDSP.RoundingMode) -> [U]](./vdsp/floatingpointtointeger%28_,integertype,rounding%29-9z84u.md)
  Returns single-precision values converted to integer values.
- [static func formRamp<V>(in: ClosedRange<Double>, result: inout V)](./vdsp/formramp%28in,result%29-6ef26.md)
  Populates a single-precision vector with monotonically incrementing or decrementing values within a range.
- [static func formRamp<V>(in: ClosedRange<Float>, result: inout V)](./vdsp/formramp%28in,result%29-8lsid.md)
  Populates a double-precision vector with monotonically incrementing or decrementing values within a range.
- [static func formRamp<V>(withInitialValue: Double, increment: Double, result: inout V)](./vdsp/formramp%28withinitialvalue,increment,result%29-4ibjw.md)
  Populates a double-precision vector with monotonically incrementing or decrementing values using an initial value and increment.
- [static func formRamp<V>(withInitialValue: Float, increment: Float, result: inout V)](./vdsp/formramp%28withinitialvalue,increment,result%29-40zxg.md)
  Populates a single-precision vector with monotonically incrementing or decrementing values using an initial value and increment.
- [static func formRamp<U, V>(withInitialValue: inout Double, multiplyingBy: U, increment: Double, result: inout V)](./vdsp/formramp%28withinitialvalue,multiplyingby,increment,result%29-p7s4.md)
  Populates a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func formRamp<U, V>(withInitialValue: inout Float, multiplyingBy: U, increment: Float, result: inout V)](./vdsp/formramp%28withinitialvalue,multiplyingby,increment,result%29-4r0kz.md)
  Populates a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func formStereoRamp<U, V>(withInitialValue: inout Double, multiplyingBy: U, U, increment: Double, results: inout V, inout V)](./vdsp/formstereoramp%28withinitialvalue,multiplyingby,_,increment,results,_%29-99lyb.md)
  Populates two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func formStereoRamp<U, V>(withInitialValue: inout Float, multiplyingBy: U, U, increment: Float, results: inout V, inout V)](./vdsp/formstereoramp%28withinitialvalue,multiplyingby,_,increment,results,_%29-9be28.md)
  Populates two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func formWindow<V>(usingSequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool)](./vdsp/formwindow%28usingsequence,result,ishalfwindow%29-6cmve.md)
  Populates a double-precision vector with a specified window.
- [static func formWindow<V>(usingSequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool)](./vdsp/formwindow%28usingsequence,result,ishalfwindow%29-9dls5.md)
  Populates a single-precision vector with a specified window.
- [static func hypot<U, V>(U, V) -> [Double]](./vdsp/hypot%28_,_%29-7ku7m.md)
  Returns the double-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of the two input vectors.
- [static func hypot<U, V>(U, V) -> [Float]](./vdsp/hypot%28_,_%29-5grex.md)
  Returns the single-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of the two input vectors.
- [static func hypot<T, U, V>(T, U, result: inout V)](./vdsp/hypot%28_,_,result%29-1z10j.md)
  Calculates the double-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of the two input vectors.
- [static func hypot<T, U, V>(T, U, result: inout V)](./vdsp/hypot%28_,_,result%29-5d8pw.md)
  Calculates the single-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of the two input vectors.
- [static func hypot<R, S, T, U>(x0: R, x1: S, y0: T, y1: U) -> [Double]](./vdsp/hypot%28x0,x1,y0,y1%29-12d4r.md)
  Returns the double-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
- [static func hypot<R, S, T, U>(x0: R, x1: S, y0: T, y1: U) -> [Float]](./vdsp/hypot%28x0,x1,y0,y1%29-15wy5.md)
  Returns the single-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
- [static func hypot<R, S, T, U, V>(x0: R, x1: S, y0: T, y1: U, result: inout V)](./vdsp/hypot%28x0,x1,y0,y1,result%29-4pizr.md)
  Calculates the double-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
- [static func hypot<R, S, T, U, V>(x0: R, x1: S, y0: T, y1: U, result: inout V)](./vdsp/hypot%28x0,x1,y0,y1,result%29-7ksm.md)
  Calculates the single-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
- [static func indexOfMaximum<U>(U) -> (UInt, Double)](./vdsp/indexofmaximum%28_%29-8h0hm.md)
  Returns the maximum value and corresponding index in a double-precision vector.
- [static func indexOfMaximum<U>(U) -> (UInt, Float)](./vdsp/indexofmaximum%28_%29-5qdtm.md)
  Returns the maximum value and corresponding index in a single-precision vector.
- [static func indexOfMaximumMagnitude<U>(U) -> (UInt, Double)](./vdsp/indexofmaximummagnitude%28_%29-6847f.md)
  Returns the maximum magnitude and corresponding index in a double-precision vector.
- [static func indexOfMaximumMagnitude<U>(U) -> (UInt, Float)](./vdsp/indexofmaximummagnitude%28_%29-f14b.md)
  Returns the maximum magnitude and corresponding index in a single-precision vector.
- [static func indexOfMinimum<U>(U) -> (UInt, Double)](./vdsp/indexofminimum%28_%29-56tf7.md)
  Returns the maximum value and corresponding index in a double-precision vector.
- [static func indexOfMinimum<U>(U) -> (UInt, Float)](./vdsp/indexofminimum%28_%29-989q3.md)
  Returns the maximum value and corresponding index in a single-precision vector.
- [static func integerToFloatingPoint<T, U>(T, floatingPointType: U.Type) -> [U]](./vdsp/integertofloatingpoint%28_,floatingpointtype%29-7479i.md)
  Returns a vector of floating-point values converted from signed 8-bit integer values.
- [static func integerToFloatingPoint<T, U>(T, floatingPointType: U.Type) -> [U]](./vdsp/integertofloatingpoint%28_,floatingpointtype%29-5os5n.md)
  Returns a vector of floating-point values converted from signed 16-bit integer values.
- [static func integerToFloatingPoint<T, U>(T, floatingPointType: U.Type) -> [U]](./vdsp/integertofloatingpoint%28_,floatingpointtype%29-8b7ni.md)
  Returns a vector of floating-point values converted from signed 32-bit integer values.
- [static func integerToFloatingPoint<T, U>(T, floatingPointType: U.Type) -> [U]](./vdsp/integertofloatingpoint%28_,floatingpointtype%29-8jgqh.md)
  Returns a vector of floating-point values converted from unsigned 8-bit integer values.
- [static func integerToFloatingPoint<T, U>(T, floatingPointType: U.Type) -> [U]](./vdsp/integertofloatingpoint%28_,floatingpointtype%29-2xoiz.md)
  Returns a vector of floating-point values converted from unsigned 16-bit integer values.
- [static func integerToFloatingPoint<T, U>(T, floatingPointType: U.Type) -> [U]](./vdsp/integertofloatingpoint%28_,floatingpointtype%29-23d97.md)
  Returns a vector of floating-point values converted from unsigned 32-bit integer values.
- [static func integrate<U>(U, using: vDSP.IntegrationRule, stepSize: Double) -> [Double]](./vdsp/integrate%28_,using,stepsize%29-1bw3x.md)
  Returns the integration of a double-precision vector using the specified rule.
- [static func integrate<U>(U, using: vDSP.IntegrationRule, stepSize: Float) -> [Float]](./vdsp/integrate%28_,using,stepsize%29-7wei4.md)
  Returns the integration of a single-precision vector using the specified rule.
- [static func integrate<U, V>(U, using: vDSP.IntegrationRule, stepSize: Double, result: inout V)](./vdsp/integrate%28_,using,stepsize,result%29-75jvf.md)
  Performs the integration of a double-precision using the specified rule.
- [static func integrate<U, V>(U, using: vDSP.IntegrationRule, stepSize: Float, result: inout V)](./vdsp/integrate%28_,using,stepsize,result%29-44lew.md)
  Performs the integration of a single-precision using the specified rule.
- [static func invertedClip<U>(U, to: ClosedRange<Double>) -> [Double]](./vdsp/invertedclip%28_,to%29-8yqtl.md)
  Returns a double-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U>(U, to: ClosedRange<Float>) -> [Float]](./vdsp/invertedclip%28_,to%29-4pkxw.md)
  Returns a single-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U, V>(U, to: ClosedRange<Double>, result: inout V)](./vdsp/invertedclip%28_,to,result%29-5ioal.md)
  Calculates a double-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U, V>(U, to: ClosedRange<Float>, result: inout V)](./vdsp/invertedclip%28_,to,result%29-3q12m.md)
  Calculates a single-precision vector that’s inverted-clipped to the specified range.
- [static func limit<U>(U, limit: Double, withOutputConstant: Double) -> [Double]](./vdsp/limit%28_,limit,withoutputconstant%29-2d9u6.md)
  Returns the double-precision vector test limit.
- [static func limit<U>(U, limit: Float, withOutputConstant: Float) -> [Float]](./vdsp/limit%28_,limit,withoutputconstant%29-8bj65.md)
  Returns the single-precision vector test limit.
- [static func limit<U, V>(U, limit: Double, withOutputConstant: Double, result: inout V)](./vdsp/limit%28_,limit,withoutputconstant,result%29-6apdv.md)
  Calculates the double-precision vector test limit.
- [static func limit<U, V>(U, limit: Float, withOutputConstant: Float, result: inout V)](./vdsp/limit%28_,limit,withoutputconstant,result%29-9v33v.md)
  Calculates the single-precision vector test limit.
- [static func linearInterpolate<T, U>(T, U, using: Double) -> [Double]](./vdsp/linearinterpolate%28_,_,using%29-3j5d2.md)
  Returns the linear interpolation between the supplied double-precision vectors.
- [static func linearInterpolate<T, U>(T, U, using: Float) -> [Float]](./vdsp/linearinterpolate%28_,_,using%29-71as1.md)
  Returns the linear interpolation between the supplied single-precision vectors.
- [static func linearInterpolate<T, U, V>(T, U, using: Double, result: inout V)](./vdsp/linearinterpolate%28_,_,using,result%29-6o7a9.md)
  Calculates the linear interpolation between the supplied double-precision vectors.
- [static func linearInterpolate<T, U, V>(T, U, using: Float, result: inout V)](./vdsp/linearinterpolate%28_,_,using,result%29-55avl.md)
  Calculates the linear interpolation between the supplied single-precision vectors.
- [static func linearInterpolate<T, U>(elementsOf: T, using: U) -> [Double]](./vdsp/linearinterpolate%28elementsof,using%29-5i3jc.md)
  Returns the interpolation between the neighboring elements of a double-precision vector.
- [static func linearInterpolate<T, U>(elementsOf: T, using: U) -> [Float]](./vdsp/linearinterpolate%28elementsof,using%29-49r3c.md)
  Returns the interpolation between the neighboring elements of a single-precision vector.
- [static func linearInterpolate<T, U, V>(elementsOf: T, using: U, result: inout V)](./vdsp/linearinterpolate%28elementsof,using,result%29-4n3lr.md)
  Calculates the interpolation between the neighboring elements of a double-precision vector.
- [static func linearInterpolate<T, U, V>(elementsOf: T, using: U, result: inout V)](./vdsp/linearinterpolate%28elementsof,using,result%29-9y61c.md)
  Calculates the interpolation between the neighboring elements of a single-precision vector.
- [static func maximum<U>(U) -> Double](./vdsp/maximum%28_%29-6lwgw.md)
  Returns the double-precision maximum value of a vector.
- [static func maximum<U>(U) -> Float](./vdsp/maximum%28_%29-220y6.md)
  Returns the single-precision maximum value of a vector.
- [static func maximum<U>(U, U) -> [Double]](./vdsp/maximum%28_,_%29-4sao3.md)
  Returns a double-precision array containing the maximum of the corresponding values of two vectors.
- [static func maximum<U>(U, U) -> [Float]](./vdsp/maximum%28_,_%29-6306m.md)
  Returns a single-precision array containing the maximum of the corresponding values of two vectors.
- [static func maximum<U, V>(U, U, result: inout V)](./vdsp/maximum%28_,_,result%29-1rxz4.md)
  Calculates the maximum of the corresponding double-precision values of two vectors.
- [static func maximum<U, V>(U, U, result: inout V)](./vdsp/maximum%28_,_,result%29-4021u.md)
  Calculates the maximum of the corresponding single-precision values of two vectors.
- [static func maximumMagnitude<U>(U) -> Double](./vdsp/maximummagnitude%28_%29-557r4.md)
  Returns the double-precision maximum magnitude of a vector.
- [static func maximumMagnitude<U>(U) -> Float](./vdsp/maximummagnitude%28_%29-19jre.md)
  Returns the single-precision maximum magnitude of a vector.
- [static func mean<U>(U) -> Double](./vdsp/mean%28_%29-60g3p.md)
  Returns the mean value of a double-precision vector.
- [static func mean<U>(U) -> Float](./vdsp/mean%28_%29-1lwak.md)
  Returns the mean value of a single-precision vector.
- [static func meanMagnitude<U>(U) -> Double](./vdsp/meanmagnitude%28_%29-664b7.md)
  Returns the mean of magnitudes of a double-precision vector.
- [static func meanMagnitude<U>(U) -> Float](./vdsp/meanmagnitude%28_%29-3fica.md)
  Returns the mean of magnitudes of a single-precision vector.
- [static func meanSquare<U>(U) -> Double](./vdsp/meansquare%28_%29-1gh6k.md)
  Returns the mean of squares of a double-precision vector.
- [static func meanSquare<U>(U) -> Float](./vdsp/meansquare%28_%29-751e5.md)
  Returns the mean of squares of a single-precision vector.
- [static func minimum<U>(U) -> Double](./vdsp/minimum%28_%29-4w8y3.md)
  Returns the double-precision minimum value of a vector.
- [static func minimum<U>(U) -> Float](./vdsp/minimum%28_%29-9b5zc.md)
  Returns the single-precision minimum value of a vector.
- [static func minimum<U>(U, U) -> [Double]](./vdsp/minimum%28_,_%29-9t6e4.md)
  Returns a double-precision array containing the minimum of the corresponding values of two vectors.
- [static func minimum<U>(U, U) -> [Float]](./vdsp/minimum%28_,_%29-1rpb2.md)
  Returns a single-precision array containing the minimum of the corresponding values of two vectors.
- [static func minimum<U, V>(U, U, result: inout V)](./vdsp/minimum%28_,_,result%29-1bdzw.md)
  Calculates the double-precision minimum of the corresponding values of two vectors.
- [static func minimum<U, V>(U, U, result: inout V)](./vdsp/minimum%28_,_,result%29-3eh5g.md)
  Calculates the single-precision minimum of the corresponding values of two vectors.
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
- [static func negative<U>(U) -> [Double]](./vdsp/negative%28_%29-24oe4.md)
  Returns the negative value of each element in the supplied double-precision vector.
- [static func negative<U>(U) -> [Float]](./vdsp/negative%28_%29-8mo1p.md)
  Returns the negative value of each element in the supplied single-precision vector.
- [static func negative<U, V>(U, result: inout V)](./vdsp/negative%28_,result%29-5bwqv.md)
  Calculates the negative value of each element in the supplied double-precision vector.
- [static func negative<U, V>(U, result: inout V)](./vdsp/negative%28_,result%29-92caw.md)
  Calculates the negative value of each element in the supplied single-precision vector.
- [static func negativeAbsolute<U>(U) -> [Double]](./vdsp/negativeabsolute%28_%29-1b5m6.md)
  Returns the negative absolute value of each element in the supplied double-precision vector.
- [static func negativeAbsolute<U>(U) -> [Float]](./vdsp/negativeabsolute%28_%29-66a7a.md)
  Returns the negative absolute value of each element in the supplied single-precision vector.
- [static func negativeAbsolute<U, V>(U, result: inout V)](./vdsp/negativeabsolute%28_,result%29-1gpcy.md)
  Calculates the negative absolute value of each element in the supplied double-precision vector.
- [static func negativeAbsolute<U, V>(U, result: inout V)](./vdsp/negativeabsolute%28_,result%29-85gj0.md)
  Calculates the negative absolute value of each element in the supplied single-precision vector.
- [static func phase<V>(DSPSplitComplex, result: inout V)](./vdsp/phase%28_,result%29-1ve4y.md)
  Calculates the single-precision element-wise phase values, in radians, of the supplied complex vector.
- [static func phase<V>(DSPDoubleSplitComplex, result: inout V)](./vdsp/phase%28_,result%29-56qb1.md)
  Calculates the double-precision element-wise phase values, in radians, of the supplied complex vector.
- [static func polarToRectangular<U>(U) -> [Double]](./vdsp/polartorectangular%28_%29-jgv8.md)
  Returns double-precision rectangular coordinates converted from polar coordinates.
- [static func polarToRectangular<U>(U) -> [Float]](./vdsp/polartorectangular%28_%29-8upqj.md)
  Returns single-precision rectangular coordinates converted from polar coordinates.
- [static func powerToDecibels<U>(U, zeroReference: Double) -> [Double]](./vdsp/powertodecibels%28_,zeroreference%29-4b0qz.md)
  Returns double-precision power values converted to decibel values.
- [static func powerToDecibels<U>(U, zeroReference: Float) -> [Float]](./vdsp/powertodecibels%28_,zeroreference%29-861j5.md)
  Returns single-precision power values converted to decibel values.
- [static func ramp(in: ClosedRange<Double>, count: Int) -> [Double]](./vdsp/ramp%28in,count%29-744b4.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values within a range.
- [static func ramp(in: ClosedRange<Float>, count: Int) -> [Float]](./vdsp/ramp%28in,count%29-79aw7.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values within a range.
- [static func ramp(withInitialValue: Double, increment: Double, count: Int) -> [Double]](./vdsp/ramp%28withinitialvalue,increment,count%29-3cast.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values using an initial value and increment.
- [static func ramp(withInitialValue: Float, increment: Float, count: Int) -> [Float]](./vdsp/ramp%28withinitialvalue,increment,count%29-mjsa.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values using an initial value and increment.
- [static func ramp<U>(withInitialValue: inout Double, multiplyingBy: U, increment: Double) -> [Double]](./vdsp/ramp%28withinitialvalue,multiplyingby,increment%29-1s3c9.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func ramp<U>(withInitialValue: inout Float, multiplyingBy: U, increment: Float) -> [Float]](./vdsp/ramp%28withinitialvalue,multiplyingby,increment%29-6b5re.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func rectangularToPolar<U>(U) -> [Double]](./vdsp/rectangulartopolar%28_%29-3txg1.md)
  Returns double-precision polar coordinates converted from rectangular coordinates.
- [static func rectangularToPolar<U>(U) -> [Float]](./vdsp/rectangulartopolar%28_%29-5p4kg.md)
  Returns single-precision polar coordinates converted from rectangular coordinates.
- [static func reverse<V>(inout V)](./vdsp/reverse%28_%29-3aq38.md)
  Reverses a vector of double-precision values in-place.
- [static func reverse<V>(inout V)](./vdsp/reverse%28_%29-38ptd.md)
  Reverses a vector of single-precision values in-place.
- [static func rootMeanSquare<U>(U) -> Double](./vdsp/rootmeansquare%28_%29-4mwg7.md)
  Returns the root mean square of a double-precision vector.
- [static func rootMeanSquare<U>(U) -> Float](./vdsp/rootmeansquare%28_%29-9xkkk.md)
  Returns the root mean square of a single-precision vector.
- [static func signedSquare<U>(U) -> [Double]](./vdsp/signedsquare%28_%29-8y09t.md)
  Returns a double-precision array containing the signed square of each element in the supplied vector.
- [static func signedSquare<U>(U) -> [Float]](./vdsp/signedsquare%28_%29-9v7ec.md)
  Returns a single-precision array containing the signed square of each element in the supplied vector.
- [static func signedSquare<U, V>(U, result: inout V)](./vdsp/signedsquare%28_,result%29-56omf.md)
  Calculates the signed square of each element in the supplied double-precision vector.
- [static func signedSquare<U, V>(U, result: inout V)](./vdsp/signedsquare%28_,result%29-2771f.md)
  Calculates the signed square of each element in the supplied single-precision vector.
- [static func slidingWindowSum<U>(U, usingWindowLength: Int) -> [Double]](./vdsp/slidingwindowsum%28_,usingwindowlength%29-2t1dc.md)
  Returns the double-precision sliding window sum of a vector.
- [static func slidingWindowSum<U>(U, usingWindowLength: Int) -> [Float]](./vdsp/slidingwindowsum%28_,usingwindowlength%29-reb8.md)
  Returns the single-precision sliding window sum of a vector.
- [static func slidingWindowSum<U, V>(U, usingWindowLength: Int, result: inout V)](./vdsp/slidingwindowsum%28_,usingwindowlength,result%29-i972.md)
  Calculates the double-precision sliding window sum of a vector.
- [static func slidingWindowSum<U, V>(U, usingWindowLength: Int, result: inout V)](./vdsp/slidingwindowsum%28_,usingwindowlength,result%29-5tg0h.md)
  Calculates the single-precision sliding window sum of a vector.
- [static func sort<V>(inout V, sortOrder: vDSP.SortOrder)](./vdsp/sort%28_,sortorder%29-418g0.md)
  Sorts a vector of double-precision values in-place.
- [static func sort<V>(inout V, sortOrder: vDSP.SortOrder)](./vdsp/sort%28_,sortorder%29-wx0w.md)
  Sorts a vector of single-precision values in-place.
- [static func square<U>(U) -> [Double]](./vdsp/square%28_%29-1dz7.md)
  Returns a double-precision array containing the square of each element in the supplied vector.
- [static func square<U>(U) -> [Float]](./vdsp/square%28_%29-30jok.md)
  Returns a single-precision array containing the square of each element in the supplied vector.
- [static func square<U, V>(U, result: inout V)](./vdsp/square%28_,result%29-9e5hu.md)
  Calculates the square of each element in the supplied double-precision vector.
- [static func square<U, V>(U, result: inout V)](./vdsp/square%28_,result%29-3kja7.md)
  Calculates the square of each element in the supplied single-precision vector.
- [static func squareMagnitudes<V>(DSPSplitComplex, result: inout V)](./vdsp/squaremagnitudes%28_,result%29-22k5h.md)
  Calculates the square magnitude of each element in the supplied single-precision complex vector.
- [static func squareMagnitudes<V>(DSPDoubleSplitComplex, result: inout V)](./vdsp/squaremagnitudes%28_,result%29-14oiw.md)
  Calculates the square magnitude of each element in the supplied double-precision complex vector.
- [static func stereoRamp<U>(withInitialValue: inout Double, multiplyingBy: U, U, increment: Double) -> (firstOutput: [Double], secondOutput: [Double])](./vdsp/stereoramp%28withinitialvalue,multiplyingby,_,increment%29-5utuo.md)
  Returns two double-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func stereoRamp<U>(withInitialValue: inout Float, multiplyingBy: U, U, increment: Float) -> (firstOutput: [Float], secondOutput: [Float])](./vdsp/stereoramp%28withinitialvalue,multiplyingby,_,increment%29-18f8z.md)
  Returns two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
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
- [static func sum<U>(U) -> Double](./vdsp/sum%28_%29-6jamg.md)
  Returns the double-precision vector sum.
- [static func sum<U>(U) -> Float](./vdsp/sum%28_%29-8hq9.md)
  Returns the single-precision vector sum.
- [static func sumAndSumOfSquares<U>(U) -> (elementsSum: Double, squaresSum: Double)](./vdsp/sumandsumofsquares%28_%29-9uec5.md)
  Returns the double-precision vector sum and sum of squares.
- [static func sumAndSumOfSquares<U>(U) -> (elementsSum: Float, squaresSum: Float)](./vdsp/sumandsumofsquares%28_%29-45el.md)
  Returns the single-precision vector sum and sum of squares.
- [static func sumOfMagnitudes<U>(U) -> Double](./vdsp/sumofmagnitudes%28_%29-77eli.md)
  Returns the double-precision vector sum of magnitudes.
- [static func sumOfMagnitudes<U>(U) -> Float](./vdsp/sumofmagnitudes%28_%29-3mdj2.md)
  Returns the single-precision vector sum of magnitudes.
- [static func sumOfSquares<U>(U) -> Double](./vdsp/sumofsquares%28_%29-9quys.md)
  Returns the double-precision vector sum of squares.
- [static func sumOfSquares<U>(U) -> Float](./vdsp/sumofsquares%28_%29-2sew6.md)
  Returns the single-precision vector sum of squares.
- [static func threshold<U>(U, to: Double, with: vDSP.ThresholdRule<Double>) -> [Double]](./vdsp/threshold%28_,to,with%29-77g7l.md)
  Returns the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U>(U, to: Float, with: vDSP.ThresholdRule<Float>) -> [Float]](./vdsp/threshold%28_,to,with%29-534ob.md)
  Returns the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Double, with: vDSP.ThresholdRule<Double>, result: inout V)](./vdsp/threshold%28_,to,with,result%29-45b58.md)
  Calculates the elements of the supplied double-precision vector after applying a specified thresholding rule.
- [static func threshold<U, V>(U, to: Float, with: vDSP.ThresholdRule<Float>, result: inout V)](./vdsp/threshold%28_,to,with,result%29-8137c.md)
  Calculates the elements of the supplied single-precision vector after applying a specified thresholding rule.
- [static func trunc<U>(U) -> [Double]](./vdsp/trunc%28_%29-80rfo.md)
  Returns a double-precision array containing each element in the supplied vector truncated to a fraction.
- [static func trunc<U>(U) -> [Float]](./vdsp/trunc%28_%29-1npgt.md)
  Returns a single-precision array containing each element in the supplied vector truncated to a fraction.
- [static func trunc<U, V>(U, result: inout V)](./vdsp/trunc%28_,result%29-4t63c.md)
  Calculates each element in the supplied double-precision vector truncated to a fraction.
- [static func trunc<U, V>(U, result: inout V)](./vdsp/trunc%28_,result%29-fabn.md)
  Calculates each element in the supplied single-precision vector truncated to a fraction.
- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Double, Double, Double, Double, Double)) -> [Double]](./vdsp/twopoletwozerofilter%28_,coefficients%29-8oaux.md)
  Returns the result of double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Float, Float, Float, Float, Float)) -> [Float]](./vdsp/twopoletwozerofilter%28_,coefficients%29-3jbcg.md)
  Returns the result of single-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Double, Double, Double, Double, Double), result: inout V)](./vdsp/twopoletwozerofilter%28_,coefficients,result%29-fe5l.md)
  Performs double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Float, Float, Float, Float, Float), result: inout V)](./vdsp/twopoletwozerofilter%28_,coefficients,result%29-gq5l.md)
  Performs single-precision, two-pole, two-zero recursive filtering.
- [static func window<T>(ofType: T.Type, usingSequence: vDSP.WindowSequence, count: Int, isHalfWindow: Bool) -> [T]](./vdsp/window%28oftype,usingsequence,count,ishalfwindow%29.md)
  Returns an array that contains the specified window.
- [static func compress<T, U>(T, gatingVector: U, nonZeroGatingCount: Int?) -> [Double]](./vdsp/compress%28_,gatingvector,nonzerogatingcount%29-93v23.md)
  Returns a compressed copy of the specified double-precision vector using the nonzero values in a gating vector.
- [static func compress<T, U>(T, gatingVector: U, nonZeroGatingCount: Int?) -> [Float]](./vdsp/compress%28_,gatingvector,nonzerogatingcount%29-3c7yk.md)
  Returns a compressed copy of the specified single-precision vector using the nonzero values in a gating vector.
- [static func compress<T, U, V>(T, gatingVector: U, result: inout V)](./vdsp/compress%28_,gatingvector,result%29-2yse4.md)
  Compresses the specified double-precision vector using the nonzero values in a gating vector.
- [static func compress<T, U, V>(T, gatingVector: U, result: inout V)](./vdsp/compress%28_,gatingvector,result%29-7fvy9.md)
  Compresses the specified single-precision vector using the nonzero values in a gating vector.
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-aiez.md)
- [static func convertElements<U, V>(of: U, to: inout V)](./vdsp/convertelements%28of,to%29-1maw9.md)
- [static func dot<T, U>(T, U) -> Double](./vdsp/dot%28_,_%29-9uigz.md)
- [static func dot<T, U>(T, U) -> Float](./vdsp/dot%28_,_%29-9pb8y.md)
- [static func float16ToFloat<U>(U) -> [Float]](./vdsp/float16tofloat%28_%29.md)
- [static func floatToFloat16<U>(U) -> [Float16]](./vdsp/floattofloat16%28_%29.md)
- [static func formRamp<V>(from: Double, through: Double, result: inout V)](./vdsp/formramp%28from,through,result%29-2sujw.md)
- [static func formRamp<V>(from: Float, through: Float, result: inout V)](./vdsp/formramp%28from,through,result%29-iyvh.md)
- [static func gather<T, U>(T, indices: U) -> [Double]](./vdsp/gather%28_,indices%29-4yt3o.md)
  Returns a gathered copy of the specified double-precision vector using a vector that defines the indices to keep.
- [static func gather<T, U>(T, indices: U) -> [Float]](./vdsp/gather%28_,indices%29-4jwvh.md)
  Returns a gathered copy of the specified single-precision vector using a vector that defines the indices to keep.
- [static func gather<T, U, V>(T, indices: U, result: inout V)](./vdsp/gather%28_,indices,result%29-34yzg.md)
  Gathers the specified double-precision vector using a vector that defines the indices to keep.
- [static func gather<T, U, V>(T, indices: U, result: inout V)](./vdsp/gather%28_,indices,result%29-7erii.md)
  Gathers the specified single-precision vector using a vector that defines the indices to keep.
- [static func linearInterpolate<T, U>(lookupTable: T, withOffsets: U, scale: Double, baseOffset: Double) -> [Double]](./vdsp/linearinterpolate%28lookuptable,withoffsets,scale,baseoffset%29-1ye2o.md)
  Returns the double-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U>(lookupTable: T, withOffsets: U, scale: Float, baseOffset: Float) -> [Float]](./vdsp/linearinterpolate%28lookuptable,withoffsets,scale,baseoffset%29-3nw6t.md)
  Returns the single-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U, V>(lookupTable: T, withOffsets: U, scale: Double, baseOffset: Double, result: inout V)](./vdsp/linearinterpolate%28lookuptable,withoffsets,scale,baseoffset,result%29-9l3uy.md)
  Computes the double-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U, V>(lookupTable: T, withOffsets: U, scale: Float, baseOffset: Float, result: inout V)](./vdsp/linearinterpolate%28lookuptable,withoffsets,scale,baseoffset,result%29-4ownc.md)
  Computes the single-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U>(values: T, atIndices: U) -> [Double]](./vdsp/linearinterpolate%28values,atindices%29-9rxb4.md)
  Returns the double-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U>(values: T, atIndices: U) -> [Float]](./vdsp/linearinterpolate%28values,atindices%29-5mbnu.md)
  Returns the single-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U, V>(values: T, atIndices: U, result: inout V)](./vdsp/linearinterpolate%28values,atindices,result%29-7nre0.md)
  Computes the double-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U, V>(values: T, atIndices: U, result: inout V)](./vdsp/linearinterpolate%28values,atindices,result%29-6i7sl.md)
  Computes the single-precision linearly interpolated values of a vector at the specified indices.
- [static func normalize(some AccelerateBuffer<Double>) -> [Double]](./vdsp/normalize%28_%29-9hp3n.md)
- [static func normalize(some AccelerateBuffer<Float>) -> [Float]](./vdsp/normalize%28_%29-6cmqg.md)
- [static func normalize(some AccelerateBuffer<Double>, result: inout some AccelerateMutableBuffer<Double>) -> (mean: Double, stdDev: Double)](./vdsp/normalize%28_,result%29-3cxh2.md)
- [static func normalize(some AccelerateBuffer<Float>, result: inout some AccelerateMutableBuffer<Float>) -> (mean: Float, stdDev: Float)](./vdsp/normalize%28_,result%29-1z58z.md)
- [static func ramp(from: Double, through: Double, count: Int) -> [Double]](./vdsp/ramp%28from,through,count%29-6r2fd.md)
- [static func ramp(from: Float, through: Float, count: Int) -> [Float]](./vdsp/ramp%28from,through,count%29-2q6al.md)
- [static func standardDeviation(some AccelerateMutableBuffer<Double>) -> Double](./vdsp/standarddeviation%28_%29-2e9i1.md)
- [static func standardDeviation(some AccelerateMutableBuffer<Float>) -> Float](./vdsp/standarddeviation%28_%29-9i3oh.md)
- [static func swapElements<T, U>(inout T, inout U)](./vdsp/swapelements%28_,_%29-62wvt.md)
  Swaps the elements of two double-precision vectors.
- [static func swapElements<T, U>(inout T, inout U)](./vdsp/swapelements%28_,_%29-96xn7.md)
  Swaps the elements of two single-precision vectors.
- [static func taperedMerge<T, U>(T, U) -> [Double]](./vdsp/taperedmerge%28_,_%29-9s9j5.md)
  Returns the result of a tapered merge between two double-precision vectors.
- [static func taperedMerge<T, U>(T, U) -> [Float]](./vdsp/taperedmerge%28_,_%29-5dhoj.md)
  Returns the result of a tapered merge between two single-precision vectors.
- [static func taperedMerge<T, U, V>(T, U, result: inout V)](./vdsp/taperedmerge%28_,_,result%29-9361o.md)
  Computes the result of a tapered merge between two double-precision vectors.
- [static func taperedMerge<T, U, V>(T, U, result: inout V)](./vdsp/taperedmerge%28_,_,result%29-74fuy.md)
  Computes the result of a tapered merge between two single-precision vectors.
### Classes
- [class DCT](./vdsp/dct.md)
  A single-precision discrete cosine transform.
- [class DFT](./vdsp/dft.md)
  A single- and double-precision discrete Fourier transform.
- [class FFT](./vdsp/fft.md)
  A 1D single- and double-precision fast Fourier transform.
- [class FFT2D](./vdsp/fft2d.md)
  A 2D single- and double-precision fast Fourier transform.
- [class DiscreteFourierTransform](./vdsp/discretefouriertransform.md)
  An object that provides forward and inverse discrete Fourier transforms on single- or double-precision collections of interleaved or split-complex data.
### Structures
- [struct Biquad](./vdsp/biquad.md)
  A single- or double-precision biquadratic filter.
- [struct VectorizableDouble](./vdsp/vectorizabledouble.md)
  A structure that represents a double-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct VectorizableFloat](./vdsp/vectorizablefloat.md)
  A structure that represents a single-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct DFTDoublePrecisionInterleavedFunctions](./vdsp/dftdoubleprecisioninterleavedfunctions.md)
- [struct DFTDoublePrecisionSplitComplexFunctions](./vdsp/dftdoubleprecisionsplitcomplexfunctions.md)
- [struct DFTSinglePrecisionInterleavedFunctions](./vdsp/dftsingleprecisioninterleavedfunctions.md)
- [struct DFTSinglePrecisionSplitComplexFunctions](./vdsp/dftsingleprecisionsplitcomplexfunctions.md)
- [struct vDSP_SplitComplexDouble](./vdsp_splitcomplexdouble.md)
- [struct vDSP_SplitComplexFloat](./vdsp_splitcomplexfloat.md)
### Enumerations
- [vDSP.DCTTransformType](./vdsp/dcttransformtype.md)
  An enumeration that describes the discrete cosine transform types.
- [vDSP.DFTTransformType](./vdsp/dfttransformtype.md)
  Discrete Fourier transform types.
- [vDSP.FourierTransformDirection](./vdsp/fouriertransformdirection.md)
  Fast Fourier transform directions.
- [vDSP.IntegrationRule](./vdsp/integrationrule.md)
  Integration rules.
- [vDSP.Radix](./vdsp/radix.md)
  Fast Fourier transform radices.
- [vDSP.RoundingMode](./vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
- [vDSP.SortOrder](./vdsp/sortorder.md)
  Constants that specify the sorting order.
- [vDSP.ThresholdRule](./vdsp/thresholdrule.md)
  Constants that specify vector threshold rules.
- [vDSP.WindowSequence](./vdsp/windowsequence.md)
  Constants that specify window sequence functions.
- [vDSP.DFTError](./vdsp/dfterror.md)

## See Also

### Swift overlay
- [vDSP Protocols](./vdsp-protocols.md)
  Protocols that support Swift implementations of vDSP operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp)*