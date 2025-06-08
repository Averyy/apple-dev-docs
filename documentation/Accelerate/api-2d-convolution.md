# 2D convolution

**Framework**: Accelerate

Perform convolution operations on matrices of real data.

#### Overview

Use the functions in this group to apply a convolution kernel to a 2D matrix. The vDSP library provides functions to convolve with fixed-sized kernels and kernels with an arbitrary size.

> ❗ **Important**:  The functions in this group don’t support in-place operation.

## Topics

### Fixed-Size Kernel
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U) -> [Double]](vdsp/convolve(_:rowcount:columncount:with3x3kernel:)-1r5oa.md)
  Returns the 2D convolution of a double-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U) -> [Float]](vdsp/convolve(_:rowcount:columncount:with3x3kernel:)-7qjgw.md)
  Returns the 2D convolution of a single-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U, result: inout V)](vdsp/convolve(_:rowcount:columncount:with3x3kernel:result:)-34k76.md)
  Calculates the 2D convolution of a double-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U, result: inout V)](vdsp/convolve(_:rowcount:columncount:with3x3kernel:result:)-2worq.md)
  Calculates the 2D convolution of a single-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U) -> [Double]](vdsp/convolve(_:rowcount:columncount:with5x5kernel:)-7cvh9.md)
  Returns the 2D convolution of a double-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U) -> [Float]](vdsp/convolve(_:rowcount:columncount:with5x5kernel:)-101d6.md)
  Returns the 2D convolution of a single-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U, result: inout V)](vdsp/convolve(_:rowcount:columncount:with5x5kernel:result:)-g68r.md)
  Calculates the 2D convolution of a double-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U, result: inout V)](vdsp/convolve(_:rowcount:columncount:with5x5kernel:result:)-76h85.md)
  Calculates the 2D convolution of a single-precision vector with a 5 x 5 kernel.
- [vDSP_f3x3](vdsp_f3x3.md)
  Filters a single-precision image by performing a 2D convolution with a 3 x 3 kernel.
- [vDSP_f3x3D](vdsp_f3x3d.md)
  Filters a double-precision image by performing a 2D convolution with a 3 x 3 kernel.
- [vDSP_f5x5](vdsp_f5x5.md)
  Filters a single-precision image by performing a 2D convolution with a 5 x 5 kernel.
- [vDSP_f5x5D](vdsp_f5x5d.md)
  Filters a double-precision image by performing a 2D convolution with a 5 x 5 kernel.
### Arbitrary-Size Kernel
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int) -> [Double]](vdsp/convolve(_:rowcount:columncount:withkernel:kernelrowcount:kernelcolumncount:)-1sswe.md)
  Returns the 2D convolution of a double-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int) -> [Float]](vdsp/convolve(_:rowcount:columncount:withkernel:kernelrowcount:kernelcolumncount:)-267yl.md)
  Returns the 2D convolution of a single-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int, result: inout V)](vdsp/convolve(_:rowcount:columncount:withkernel:kernelrowcount:kernelcolumncount:result:)-4211m.md)
  Calculates the 2D convolution of a double-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int, result: inout V)](vdsp/convolve(_:rowcount:columncount:withkernel:kernelrowcount:kernelcolumncount:result:)-5hiro.md)
  Calculates the 2D convolution of a single-precision vector with an arbitrarily sized kernel.
- [vDSP_imgfir](vdsp_imgfir.md)
  Filters a single-precision image by performing a 2D convolution with an arbitrarily sized kernel.
- [vDSP_imgfirD](vdsp_imgfird.md)
  Filters a double-precision image by performing a 2D convolution with an arbitrarily sized kernel.

## See Also

- [1D correlation and convolution](1d-correlation-and-convolution.md)
  Use correlation to compare and convolution to combine vectors of real or complex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/2d-convolution)*