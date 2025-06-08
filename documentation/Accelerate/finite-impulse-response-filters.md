# Finite impulse response filters

**Framework**: Accelerate

Perform finite impulse response filtering with decimation and antialiasing on vectors of real or complex values.

## Topics

### FIR Filter Creation
- [vDSP_wiener](vdsp_wiener.md)
  Solves a system of linear equations for a single-precision symmetric Toeplitz coefficient matrix.
- [vDSP_wienerD](vdsp_wienerd.md)
  Solves a system of linear equations for a double-precision symmetric Toeplitz coefficient matrix.
### Real Vectors
- [Resampling a signal with decimation](resampling-a-signal-with-decimation.md)
  Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.
- [static func downsample<T, U>(U, decimationFactor: Int, filter: T) -> [Double]](vdsp/downsample(_:decimationfactor:filter:)-1o8it.md)
  Returns the downsampled double-precision vector.
- [static func downsample<T, U>(U, decimationFactor: Int, filter: T) -> [Float]](vdsp/downsample(_:decimationfactor:filter:)-40d8o.md)
  Returns the downsampled single-precision vector.
- [static func downsample<T, U, V>(U, decimationFactor: Int, filter: T, result: inout V)](vdsp/downsample(_:decimationfactor:filter:result:)-2y1iv.md)
  Calculates the downsampled double-precision vector.
- [static func downsample<T, U, V>(U, decimationFactor: Int, filter: T, result: inout V)](vdsp/downsample(_:decimationfactor:filter:result:)-1g4a.md)
  Calculates the downsampled single-precision vector.
- [vDSP_desamp](vdsp_desamp.md)
  Performs single-precision FIR filtering with decimation and antialiasing.
- [vDSP_desampD](vdsp_desampd.md)
  Performs double-precision FIR filtering with decimation and antialiasing.
### Complex Vectors
- [vDSP_zrdesamp](vdsp_zrdesamp.md)
  Performs complex-real single-precision FIR filtering with decimation and antialiasing.
- [vDSP_zrdesampD](vdsp_zrdesampd.md)
  Performs complex-real double-precision FIR filtering with decimation and antialiasing.

## See Also

- [Biquadratic IIR filters](biquadratic-iir-filters.md)
  Apply biquadratic filters to single-channel and multichannel data.
- [Single-channel biquadratic filters](single-channel-biquadratic-filters.md)
  Filter a single-channel signal with a cascade of biquadratic sections.
- [Multichannel biquadratic filters](multichannel-biquadratic-filters.md)
  Filter a multichannel signal with a cascade of biquadratic sections.
- [Recursive filters](recursive-filters.md)
  Perform two-pole two-zero recursive filtering on a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/finite-impulse-response-filters)*