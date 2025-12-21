# Finite impulse response filters

**Framework**: Accelerate

Perform finite impulse response filtering with decimation and antialiasing on vectors of real or complex values.

## Topics

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