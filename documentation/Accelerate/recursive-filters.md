# Recursive filters

**Framework**: Accelerate

Perform two-pole two-zero recursive filtering on a vector.

## Topics

### Vector-to-Vector Recursive Filtering on Real Vectors
- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Double, Double, Double, Double, Double)) -> [Double]](vdsp/twopoletwozerofilter(_:coefficients:)-8oaux.md)
  Returns the result of double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Float, Float, Float, Float, Float)) -> [Float]](vdsp/twopoletwozerofilter(_:coefficients:)-3jbcg.md)
  Returns the result of single-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Double, Double, Double, Double, Double), result: inout V)](vdsp/twopoletwozerofilter(_:coefficients:result:)-fe5l.md)
  Performs double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Float, Float, Float, Float, Float), result: inout V)](vdsp/twopoletwozerofilter(_:coefficients:result:)-gq5l.md)
  Performs single-precision, two-pole, two-zero recursive filtering.

## See Also

- [Biquadratic IIR filters](biquadratic-iir-filters.md)
  Apply biquadratic filters to single-channel and multichannel data.
- [Single-channel biquadratic filters](single-channel-biquadratic-filters.md)
  Filter a single-channel signal with a cascade of biquadratic sections.
- [Multichannel biquadratic filters](multichannel-biquadratic-filters.md)
  Filter a multichannel signal with a cascade of biquadratic sections.
- [Finite impulse response filters](finite-impulse-response-filters.md)
  Perform finite impulse response filtering with decimation and antialiasing on vectors of real or complex values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/recursive-filters)*