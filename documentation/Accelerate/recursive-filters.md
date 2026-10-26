# Recursive filters

**Framework**: Accelerate  
**Role**: API Collection

Perform two-pole two-zero recursive filtering on a vector.

## Topics

### Vector-to-Vector Recursive Filtering on Real Vectors
- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Double, Double, Double, Double, Double)) -> [Double]](./vdsp/twopoletwozerofilter%28_,coefficients%29-8oaux.md)
  Returns the result of double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U>(U, coefficients: (Float, Float, Float, Float, Float)) -> [Float]](./vdsp/twopoletwozerofilter%28_,coefficients%29-3jbcg.md)
  Returns the result of single-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Double, Double, Double, Double, Double), result: inout V)](./vdsp/twopoletwozerofilter%28_,coefficients,result%29-fe5l.md)
  Performs double-precision, two-pole, two-zero recursive filtering.
- [static func twoPoleTwoZeroFilter<U, V>(U, coefficients: (Float, Float, Float, Float, Float), result: inout V)](./vdsp/twopoletwozerofilter%28_,coefficients,result%29-gq5l.md)
  Performs single-precision, two-pole, two-zero recursive filtering.
- [vDSP_deq22](./vdsp_deq22.md)
  Performs two-pole two-zero recursive filtering on a single-precision vector.
- [vDSP_deq22D](./vdsp_deq22d.md)
  Performs two-pole two-zero recursive filtering on a double-precision vector.

## See Also

### Vector filtering
- [Biquadratic IIR filters](./biquadratic-iir-filters.md)
  Apply biquadratic filters to single-channel and multichannel data.
- [Single-channel biquadratic filters](./single-channel-biquadratic-filters.md)
  Filter a single-channel signal with a cascade of biquadratic sections.
- [Multichannel biquadratic filters](./multichannel-biquadratic-filters.md)
  Filter a multichannel signal with a cascade of biquadratic sections.
- [Finite impulse response filters](./finite-impulse-response-filters.md)
  Perform finite impulse response filtering with decimation and antialiasing on vectors of real or complex values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/recursive-filters)*