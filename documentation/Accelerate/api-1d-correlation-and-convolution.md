# 1D correlation and convolution

**Framework**: Accelerate

Use correlation to compare and convolution to combine vectors of real or complex data.

#### Overview

The vDSP library provides functions that calculate the convolution and correlation of a signal and a filter. Both operations compute the sliding dot product of the filter and the section of the input signal that the filter is over. What the operation produced depends on whether the stride is positive or negative:

- With a positive stride through the filter, the correlation operation computes the similarity between the signal and the filter.
- With a negative stride through the filter, the convolution operation computes the effect of the filter on the signal. For example, to apply a low-pass filter to a signal.

## Topics

### Real Vectors
- [static func convolve<T, U>(T, withKernel: U) -> [Double]](vdsp/convolve(_:withkernel:)-1nv65.md)
  Returns the 1D convolution of a double-precision vector.
- [static func convolve<T, U>(T, withKernel: U) -> [Float]](vdsp/convolve(_:withkernel:)-4p0rt.md)
  Returns the 1D convolution of a single-precision vector.
- [static func convolve<T, U, V>(T, withKernel: U, result: inout V)](vdsp/convolve(_:withkernel:result:)-8j76l.md)
  Calculates the 1D convolution of a double-precision vector.
- [static func convolve<T, U, V>(T, withKernel: U, result: inout V)](vdsp/convolve(_:withkernel:result:)-2z66w.md)
  Calculates the 1D convolution of a single-precision vector.
- [static func correlate<T, U>(T, withKernel: U) -> [Double]](vdsp/correlate(_:withkernel:)-7f6o0.md)
  Returns the correlation of a double-precision signal vector and a filter vector.
- [static func correlate<T, U>(T, withKernel: U) -> [Float]](vdsp/correlate(_:withkernel:)-9sol8.md)
  Returns the correlation of a single-precision signal vector and a filter vector.
- [static func correlate<T, U, V>(T, withKernel: U, result: inout V)](vdsp/correlate(_:withkernel:result:)-1lb82.md)
  Calculates the correlation of a double-precision signal vector and a filter vector.
- [static func correlate<T, U, V>(T, withKernel: U, result: inout V)](vdsp/correlate(_:withkernel:result:)-377zj.md)
  Calculates the correlation of a single-precision signal vector and a filter vector.
- [vDSP_conv](vdsp_conv.md)
  Performs either correlation or convolution on two real single-precision vectors.
- [vDSP_convD](vdsp_convd.md)
  Performs either correlation or convolution on two real double-precision vectors.
### Complex Vectors
- [vDSP_zconv](vdsp_zconv.md)
  Performs either correlation or convolution on two complex single-precision vectors.
- [vDSP_zconvD](vdsp_zconvd.md)
  Performs either correlation or convolution on two complex double-precision vectors.

## See Also

- [2D convolution](2d-convolution.md)
  Perform convolution operations on matrices of real data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/1d-correlation-and-convolution)*