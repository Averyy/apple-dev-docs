# Vector generation

**Framework**: Accelerate

Populate vectors with ramps, values from lookup tables, interpolated values, and window functions.

## Topics

### Vector generation with ramps using an initial value and increment
- [static func ramp(withInitialValue: Float, increment: Float, count: Int) -> [Float]](vdsp/ramp(withinitialvalue:increment:count:)-mjsa.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values using an initial value and increment.
- [static func ramp(withInitialValue: Double, increment: Double, count: Int) -> [Double]](vdsp/ramp(withinitialvalue:increment:count:)-3cast.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values using an initial value and increment.
- [static func formRamp<V>(withInitialValue: Float, increment: Float, result: inout V)](vdsp/formramp(withinitialvalue:increment:result:)-40zxg.md)
  Populates a single-precision vector with monotonically incrementing or decrementing values using an initial value and increment.
- [static func formRamp<V>(withInitialValue: Double, increment: Double, result: inout V)](vdsp/formramp(withinitialvalue:increment:result:)-4ibjw.md)
  Populates a double-precision vector with monotonically incrementing or decrementing values using an initial value and increment.
- [vDSP_vramp](vdsp_vramp.md)
  Generates a single-precision vector with monotonically incrementing or decrementing values using an initial value and increment.
- [vDSP_vrampD](vdsp_vrampd.md)
  Generates a double-precision vector with monotonically incrementing or decrementing values using an initial value and increment.
### Vector generation with ramps using a range
- [static func ramp(in: ClosedRange<Float>, count: Int) -> [Float]](vdsp/ramp(in:count:)-79aw7.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values within a range.
- [static func ramp(in: ClosedRange<Double>, count: Int) -> [Double]](vdsp/ramp(in:count:)-744b4.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values within a range.
- [static func formRamp<V>(in: ClosedRange<Float>, result: inout V)](vdsp/formramp(in:result:)-8lsid.md)
  Populates a double-precision vector with monotonically incrementing or decrementing values within a range.
- [static func formRamp<V>(in: ClosedRange<Double>, result: inout V)](vdsp/formramp(in:result:)-6ef26.md)
  Populates a single-precision vector with monotonically incrementing or decrementing values within a range.
- [vDSP_vgen](vdsp_vgen.md)
  Generates a single-precision vector that contains monotonically incrementing or decrementing values within a range.
- [vDSP_vgenD](vdsp_vgend.md)
  Generates a double-precision vector that contains monotonically incrementing or decrementing values within a range.
### Vector generation with ramps and multiplication by a second vector
- [static func ramp<U>(withInitialValue: inout Float, multiplyingBy: U, increment: Float) -> [Float]](vdsp/ramp(withinitialvalue:multiplyingby:increment:)-6b5re.md)
  Returns a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func ramp<U>(withInitialValue: inout Double, multiplyingBy: U, increment: Double) -> [Double]](vdsp/ramp(withinitialvalue:multiplyingby:increment:)-1s3c9.md)
  Returns a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func formRamp<U, V>(withInitialValue: inout Float, multiplyingBy: U, increment: Float, result: inout V)](vdsp/formramp(withinitialvalue:multiplyingby:increment:result:)-4r0kz.md)
  Populates a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [static func formRamp<U, V>(withInitialValue: inout Double, multiplyingBy: U, increment: Double, result: inout V)](vdsp/formramp(withinitialvalue:multiplyingby:increment:result:)-p7s4.md)
  Populates a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmul](vdsp_vrampmul.md)
  Generates a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmulD](vdsp_vrampmuld.md)
  Generates a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmul_s1_15](vdsp_vrampmul_s1_15.md)
  Generates a fixed-point 1.15 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmul_s8_24](vdsp_vrampmul_s8_24.md)
  Generates a fixed-point 8.24 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
### Vector addition with ramps and multiplication by a second vector
- [vDSP_vrampmuladd](vdsp_vrampmuladd.md)
  Adds a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmuladdD](vdsp_vrampmuladdd.md)
  Adds a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmuladd_s1_15](vdsp_vrampmuladd_s1_15.md)
  Adds a fixed-point 1.15 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmuladd_s8_24](vdsp_vrampmuladd_s8_24.md)
  Adds a fixed-point 8.24 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
### Vector generation by extrapolation and interpolation
- [static func linearInterpolate<T, U>(values: T, atIndices: U) -> [Float]](vdsp/linearinterpolate(values:atindices:)-5mbnu.md)
  Returns the single-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U>(values: T, atIndices: U) -> [Double]](vdsp/linearinterpolate(values:atindices:)-9rxb4.md)
  Returns the double-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U, V>(values: T, atIndices: U, result: inout V)](vdsp/linearinterpolate(values:atindices:result:)-7nre0.md)
  Computes the double-precision linearly interpolated values of a vector at the specified indices.
- [static func linearInterpolate<T, U, V>(values: T, atIndices: U, result: inout V)](vdsp/linearinterpolate(values:atindices:result:)-6i7sl.md)
  Computes the single-precision linearly interpolated values of a vector at the specified indices.
- [vDSP_vgenp](vdsp_vgenp.md)
  Generates the single-precision linearly interpolated values of a vector at the specified indices.
- [vDSP_vgenpD](vdsp_vgenpd.md)
  Generates the double-precision linearly interpolated values of a vector at the specified indices.
### Vector generation with lookup tables
- [static func linearInterpolate<T, U>(lookupTable: T, withOffsets: U, scale: Double, baseOffset: Double) -> [Double]](vdsp/linearinterpolate(lookuptable:withoffsets:scale:baseoffset:)-1ye2o.md)
  Returns the double-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U>(lookupTable: T, withOffsets: U, scale: Float, baseOffset: Float) -> [Float]](vdsp/linearinterpolate(lookuptable:withoffsets:scale:baseoffset:)-3nw6t.md)
  Returns the single-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U, V>(lookupTable: T, withOffsets: U, scale: Double, baseOffset: Double, result: inout V)](vdsp/linearinterpolate(lookuptable:withoffsets:scale:baseoffset:result:)-9l3uy.md)
  Computes the double-precision linearly interpolated values of a lookup table from the specified offsets.
- [static func linearInterpolate<T, U, V>(lookupTable: T, withOffsets: U, scale: Float, baseOffset: Float, result: inout V)](vdsp/linearinterpolate(lookuptable:withoffsets:scale:baseoffset:result:)-4ownc.md)
  Computes the single-precision linearly interpolated values of a lookup table from the specified offsets.
- [vDSP_vtabi](vdsp_vtabi.md)
  Generates a single-precision vector by interpolating values from a lookup table.
- [vDSP_vtabiD](vdsp_vtabid.md)
  Generates a double-precision vector by interpolating values from a lookup table.
### Vector generation with window functions
- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [static func window<T>(ofType: T.Type, usingSequence: vDSP.WindowSequence, count: Int, isHalfWindow: Bool) -> [T]](vdsp/window(oftype:usingsequence:count:ishalfwindow:).md)
  Returns an array that contains the specified window.
- [static func formWindow<V>(usingSequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool)](vdsp/formwindow(usingsequence:result:ishalfwindow:)-6cmve.md)
  Populates a double-precision vector with a specified window.
- [static func formWindow<V>(usingSequence: vDSP.WindowSequence, result: inout V, isHalfWindow: Bool)](vdsp/formwindow(usingsequence:result:ishalfwindow:)-9dls5.md)
  Populates a single-precision vector with a specified window.
- [vDSP.WindowSequence](vdsp/windowsequence.md)
  Constants that specify window sequence functions.
- [vDSP_blkman_window](vdsp_blkman_window.md)
  Creates a single-precision Blackman window.
- [vDSP_blkman_windowD](vdsp_blkman_windowd.md)
  Creates a double-precision Blackman window.
- [vDSP_hamm_window](vdsp_hamm_window.md)
  Creates a single-precision Hamming window.
- [vDSP_hamm_windowD](vdsp_hamm_windowd.md)
  Creates a double-precision Hamming window.
- [vDSP_hann_window](vdsp_hann_window.md)
  Creates a single-precision Hann window.
- [vDSP_hann_windowD](vdsp_hann_windowd.md)
  Creates a double-precision Hann window.
- [var vDSP_HALF_WINDOW: Int](vdsp_half_window.md)
  Specifies that the window should only contain the bottom half of the values (`0` to `(N+1)/2`).
- [var vDSP_HANN_DENORM: Int](vdsp_hann_denorm.md)
  Specifies a denormalized Hann window.
- [var vDSP_HANN_NORM: Int](vdsp_hann_norm.md)
  Specifies a normalized Hann window
### Stereo ramp generation
- [static func stereoRamp<U>(withInitialValue: inout Double, multiplyingBy: U, U, increment: Double) -> (firstOutput: [Double], secondOutput: [Double])](vdsp/stereoramp(withinitialvalue:multiplyingby:_:increment:)-5utuo.md)
  Returns two double-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func stereoRamp<U>(withInitialValue: inout Float, multiplyingBy: U, U, increment: Float) -> (firstOutput: [Float], secondOutput: [Float])](vdsp/stereoramp(withinitialvalue:multiplyingby:_:increment:)-18f8z.md)
  Returns two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func formStereoRamp<U, V>(withInitialValue: inout Double, multiplyingBy: U, U, increment: Double, results: inout V, inout V)](vdsp/formstereoramp(withinitialvalue:multiplyingby:_:increment:results:_:)-99lyb.md)
  Populates two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [static func formStereoRamp<U, V>(withInitialValue: inout Float, multiplyingBy: U, U, increment: Float, results: inout V, inout V)](vdsp/formstereoramp(withinitialvalue:multiplyingby:_:increment:results:_:)-9be28.md)
  Populates two single-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.
- [vDSP_vrampmul2](vdsp_vrampmul2.md)
  Generates a single-precision, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2D](vdsp_vrampmul2d.md)
  Generates a double-precision, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2_s1_15](vdsp_vrampmul2_s1_15.md)
  Generates a fixed-point, 1.15 format, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2_s8_24](vdsp_vrampmul2_s8_24.md)
  Generates a fixed-point, 8.24 format, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmuladd2](vdsp_vrampmuladd2.md)
  Multiplies a single-precision, stereo input vector by a value that ramps up on successive calls, and cumulatively adds the result to the output vector.
- [vDSP_vrampmuladd2D](vdsp_vrampmuladd2d.md)
  Multiplies a double-precision, stereo input vector by a value that ramps up on successive calls, and cumulatively adds the result to the output vector.
- [vDSP_vrampmuladd2_s1_15](vdsp_vrampmuladd2_s1_15.md)
  Multiplies a fixed-point, 1.15 format, stereo input vector by a value that ramps on successive calls, and adds the result to the output vector.
- [vDSP_vrampmuladd2_s8_24](vdsp_vrampmuladd2_s8_24.md)
  Multiplies a fixed-point, 8.24 format, stereo input vector by a value that ramps on successive calls, and adds the result to the output vector.

## See Also

- [Vector clear and fill functions](vector-clear-and-fill-functions.md)
  Populate vectors with zeros or a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vector-generation)*