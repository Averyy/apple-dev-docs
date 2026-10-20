# Vector generation

**Framework**: Accelerate  
**Role**: API Collection

Populate vectors with ramps, values from lookup tables, interpolated values, and window functions.

## Topics

### Vector generation with ramps using an initial value and increment
- [static func ramp(withInitialValue: Float, increment: Float, count: Int) -> [Float]](./vdsp/ramp%28withinitialvalue,increment,count%29-mjsa.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values using an initial value and increment.
- [static func ramp(withInitialValue: Double, increment: Double, count: Int) -> [Double]](./vdsp/ramp%28withinitialvalue,increment,count%29-3cast.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values using an initial value and increment.
- [static func formRamp<V>(withInitialValue: Float, increment: Float, result: inout V)](./vdsp/formramp%28withinitialvalue,increment,result%29-40zxg.md)
  Populates a single-precision vector with monotonically incrementing or decrementing values using an initial value and increment.
- [static func formRamp<V>(withInitialValue: Double, increment: Double, result: inout V)](./vdsp/formramp%28withinitialvalue,increment,result%29-4ibjw.md)
  Populates a double-precision vector with monotonically incrementing or decrementing values using an initial value and increment.
### Vector generation with ramps using a range
- [static func ramp(in: ClosedRange<Float>, count: Int) -> [Float]](./vdsp/ramp%28in,count%29-79aw7.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values within a range.
- [static func ramp(in: ClosedRange<Double>, count: Int) -> [Double]](./vdsp/ramp%28in,count%29-744b4.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values within a range.
- [static func formRamp<V>(in: ClosedRange<Float>, result: inout V)](./vdsp/formramp%28in,result%29-8lsid.md)
  Populates a double-precision vector with monotonically incrementing or decrementing values within a range.
- [static func formRamp<V>(in: ClosedRange<Double>, result: inout V)](./vdsp/formramp%28in,result%29-6ef26.md)
  Populates a single-precision vector with monotonically incrementing or decrementing values within a range.
### Vector generation with ramps and multiplication by a second vector
- [static func ramp<U>(withInitialValue: inout Float, multiplyingBy: U, increment: Float) -> [Float]](./vdsp/ramp%28withinitialvalue,multiplyingby,increment%29-6b5re.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func ramp<U>(withInitialValue: inout Double, multiplyingBy: U, increment: Double) -> [Double]](./vdsp/ramp%28withinitialvalue,multiplyingby,increment%29-1s3c9.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func formRamp<U, V>(withInitialValue: inout Float, multiplyingBy: U, increment: Float, result: inout V)](./vdsp/formramp%28withinitialvalue,multiplyingby,increment,result%29-4r0kz.md)
  Populates a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func formRamp<U, V>(withInitialValue: inout Double, multiplyingBy: U, increment: Double, result: inout V)](./vdsp/formramp%28withinitialvalue,multiplyingby,increment,result%29-p7s4.md)
  Populates a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
### Vector generation by extrapolation and interpolation
- [static func linearInterpolate<T, U>(values: T, atIndices: U) -> [Float]](./vdsp/linearinterpolate%28values,atindices%29-5mbnu.md)
  Returns the single-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U>(values: T, atIndices: U) -> [Double]](./vdsp/linearinterpolate%28values,atindices%29-9rxb4.md)
  Returns the double-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U, V>(values: T, atIndices: U, result: inout V)](./vdsp/linearinterpolate%28values,atindices,result%29-7nre0.md)
  Computes the double-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U, V>(values: T, atIndices: U, result: inout V)](./vdsp/linearinterpolate%28values,atindices,result%29-6i7sl.md)
  Computes the single-precision linearly interpolated values of a vector at the specified indices.
### Vector generation with lookup tables
- [static func linearInterpolate<T, U>(lookupTable: T, withOffsets: U, scale: Double, baseOffset: Double) -> [Double]](./vdsp/linearinterpolate%28lookuptable,withoffsets,scale,baseoffset%29-1ye2o.md)
  Returns the double-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U>(lookupTable: T, withOffsets: U, scale: Float, baseOffset: Float) -> [Float]](./vdsp/linearinterpolate%28lookuptable,withoffsets,scale,baseoffset%29-3nw6t.md)
  Returns the single-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U, V>(lookupTable: T, withOffsets: U, scale: Double, baseOffset: Double, result: inout V)](./vdsp/linearinterpolate%28lookuptable,withoffsets,scale,baseoffset,result%29-9l3uy.md)
  Computes the double-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U, V>(lookupTable: T, withOffsets: U, scale: Float, baseOffset: Float, result: inout V)](./vdsp/linearinterpolate%28lookuptable,withoffsets,scale,baseoffset,result%29-4ownc.md)
  Computes the single-precision linearly interpolated values of a lookup table from the specified offsets.
### Vector generation with window functions
- [Reducing spectral leakage with windowing](./reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [static func window<T>(ofType: T.Type, usingSequence: vDSP.WindowSequence, count: Int, isHalfWindow: Bool) -> [T]](./vdsp/window%28oftype,usingsequence,count,ishalfwindow%29.md)
  Returns an array that contains the specified window.
- [static func formWindow<V>(usingSequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool)](./vdsp/formwindow%28usingsequence,result,ishalfwindow%29-6cmve.md)
  Populates a double-precision vector with a specified window.
- [static func formWindow<V>(usingSequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool)](./vdsp/formwindow%28usingsequence,result,ishalfwindow%29-9dls5.md)
  Populates a single-precision vector with a specified window.
- [vDSP.WindowSequence](./vdsp/windowsequence.md)
  Constants that specify window sequence functions.
- [var vDSP_HALF_WINDOW: Int](./vdsp_half_window.md)
  Specifies that the window should only contain the bottom half of the values (`0` to `(N+1)/2`).
- [var vDSP_HANN_DENORM: Int](./vdsp_hann_denorm.md)
  Specifies a denormalized Hann window.
- [var vDSP_HANN_NORM: Int](./vdsp_hann_norm.md)
  Specifies a normalized Hann window
### Stereo ramp generation
- [static func stereoRamp<U>(withInitialValue: inout Double, multiplyingBy: U, U, increment: Double) -> (firstOutput: [Double], secondOutput: [Double])](./vdsp/stereoramp%28withinitialvalue,multiplyingby,_,increment%29-5utuo.md)
  Returns two double-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func stereoRamp<U>(withInitialValue: inout Float, multiplyingBy: U, U, increment: Float) -> (firstOutput: [Float], secondOutput: [Float])](./vdsp/stereoramp%28withinitialvalue,multiplyingby,_,increment%29-18f8z.md)
  Returns two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func formStereoRamp<U, V>(withInitialValue: inout Double, multiplyingBy: U, U, increment: Double, results: inout V, inout V)](./vdsp/formstereoramp%28withinitialvalue,multiplyingby,_,increment,results,_%29-99lyb.md)
  Populates two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func formStereoRamp<U, V>(withInitialValue: inout Float, multiplyingBy: U, U, increment: Float, results: inout V, inout V)](./vdsp/formstereoramp%28withinitialvalue,multiplyingby,_,increment,results,_%29-9be28.md)
  Populates two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.

## See Also

### Vector generation, filling, and clearing
- [Vector clear and fill functions](./vector-clear-and-fill-functions.md)
  Populate vectors with zeros or a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vector-generation)*