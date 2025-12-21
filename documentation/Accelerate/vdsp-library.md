# vDSP

**Framework**: Accelerate

Perform basic arithmetic operations and common digital signal processing (DSP) routines on large vectors.

#### Overview

The vDSP library contains a collection of highly optimized functions for DSP, type conversion, and general purpose arithmetic on large collections. The library includes DSP operations such as convolution and correlation, Fourier transformation, and biquadratic filtering. For arithmetic on large collections, vDSP includes functions such as multiply-add and reduction functions including sum, mean, and maximum.

The following sequence of images illustrates an example of the vDSP library’s capabilities. The [`vDSP_vtmerg`](vdsp_vtmerg.md) function combines two waveforms to produce a vector to create a smooth transition between two signals.

![A flow diagram that depicts how the tapered merge function combines two sine waves. The top row shows a low-frequency sine wave on the left and a high-frequency sine wave on the right. The bottom row shows the merged result. The resulting signal starts with a low-frequency wave and gradually transforms to a high-frequency wave.](https://docs-assets.developer.apple.com/published/a3694216774f4879f22facd838b98c34/media-4310314%402x.png)

> **Note**:  Unless otherwise mentioned, vDSP functions with the same input and output sizes (in bytes) work in-place.

The majority of vDSP operations are single-threaded and run on a single core. However, the following functions may be multithreaded depending on the size of the data they’re operating on:

- [`vDSP_mmul`](vdsp_mmul.md)
- [`vDSP_mmulD`](vdsp_mmuld.md)
- [`vDSP_zmma`](vdsp_zmma.md)
- [`vDSP_zmmaD`](vdsp_zmmad.md)
- [`vDSP_zmms`](vdsp_zmms.md)
- [`vDSP_zmmsD`](vdsp_zmmsd.md)
- [`vDSP_zmmul`](vdsp_zmmul.md)
- [`vDSP_zmmulD`](vdsp_zmmuld.md)
- [`vDSP_zmsm`](vdsp_zmsm.md)
- [`vDSP_zmsmD`](vdsp_zmsmd.md)

## Topics

### Fundamentals
- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)
  Operate selectively on the elements of a vector at regular intervals.
- [Using vDSP for vector-based arithmetic](using-vdsp-for-vector-based-arithmetic.md)
  Increase the performance of common mathematical tasks with vDSP vector-vector and vector-scalar operations.
### Swift overlay
- [enum vDSP](vdsp.md)
  An enumeration that acts as a namespace for Swift overlays to vDSP.
- [vDSP Protocols](vdsp-protocols.md)
  Protocols that support Swift implementations of vDSP operations.
### Vector generation, filling, and clearing
- [Vector generation](vector-generation.md)
  Populate vectors with ramps, values from lookup tables, interpolated values, and window functions.
- [Vector clear and fill functions](vector-clear-and-fill-functions.md)
  Populate vectors with zeros or a scalar value.
### Vector reduction
- [Vector extrema calculation](vector-extrema-calculation.md)
  Calculate the minimum and maximum values in a vector.
- [Vector average calculation](vector-average-calculation.md)
  Calculate the average value in a vector.
- [Vector summation](vector-summation.md)
  Sum the values in a vector.
### Vector geometry functions
- [Vector distance and Pythagorean computation](vector-distance-and-pythagorean-computation.md)
  Calculate distance and hypotenuse of vectors.
- [Dot product calculation](dot-product-calculation.md)
  Calculate the scalar product of two vectors.
### Element-wise vector arithmetic
- [Arithmetic operations](arithmetic-operations.md)
  Perform operations on large vectors.
### Vector-scalar arithmetic
- [Vector-scalar real arithmetic functions](vector-scalar-real-arithmetic-functions.md)
  Perform element-wise operations on combinations of vectors of real values and scalar values.
### Vector-vector arithmetic
- [Vector-vector real arithmetic functions](vector-vector-real-arithmetic-functions.md)
  Perform element-wise operations on vectors of real values.
- [Complex basic arithmetic](complex-basic-arithmetic.md)
  Perform elementwise operations on vectors of complex values.
- [Integer arithmetic](integer-arithmetic.md)
  Perform elementwise operations on vectors of integer values.
- [Linear averaging functions](linear-averaging-functions.md)
  Calculate the element-wise linear average of two vectors.
- [Polynomial evaluation](polynomial-evaluation.md)
  Evaluate polynomials using coefficients and independent variables that you supply.
### Vector operations
- [Compression and gathering functions](compression-and-gathering-functions.md)
  Compress vectors based on the nonzero elements in a gating vector, or gather vectors based on a separate vector that contains indices.
- [Copying, element swapping, and merging functions](copying-element-swapping-and-merging-functions.md)
  Copy, swap, and merge the elements of two vectors.
- [Reversing and sorting functions](reversing-and-sorting-functions.md)
  Perform in-place reverse and sort operations on a vector.
### Vector interpolation
- [Linear interpolation functions](linear-interpolation-functions.md)
  Compute the linear average between two vectors or between the neighboring elements in one vector.
- [Quadratic interpolation functions](quadratic-interpolation-functions.md)
  Compute the quadratic interpolation between the neighboring elements in a vector.
### Vector filtering
- [Biquadratic IIR filters](biquadratic-iir-filters.md)
  Apply biquadratic filters to single-channel and multichannel data.
- [Single-channel biquadratic filters](single-channel-biquadratic-filters.md)
  Filter a single-channel signal with a cascade of biquadratic sections.
- [Multichannel biquadratic filters](multichannel-biquadratic-filters.md)
  Filter a multichannel signal with a cascade of biquadratic sections.
- [Finite impulse response filters](finite-impulse-response-filters.md)
  Perform finite impulse response filtering with decimation and antialiasing on vectors of real or complex values.
- [Recursive filters](recursive-filters.md)
  Perform two-pole two-zero recursive filtering on a vector.
### Vector conversion functions
- [Conversion to decibel equivalents](conversion-to-decibel-equivalents.md)
  Convert vectors that contain power or amplitude data to decibels.
- [Type conversion](type-conversion.md)
  Perform element-wise floating-point to integer and integer to floating-point conversion.
- [Complex vector conversion](complex-vector-conversion.md)
  Perform element-wise split-complex to interleaved and interleaved to split-complex conversion.
- [Polar-rectangular conversion](polar-rectangular-conversion.md)
  Convert each element of a vector between radius-angle and Cartesian pairs.
### Single-vector arithmetic functions
- [Absolute and negation functions](absolute-and-negation-functions.md)
  Compute the absolute or negated value of each element in a vector.
- [Integration functions](integration-functions.md)
  Compute the running sum, Simpson, or trapezoidal integration of a vector.
- [Clipping, limit, and threshold operations](clipping-limit-and-threshold-operations.md)
  Apply clipping, limit, or threshold rules to the elements in a vector.
- [Normalization functions](normalization-functions.md)
  Compute the mean and standard deviation of a vector and calculate new elements to have a zero mean and a unit standard deviation.
- [Phase computation functions](phase-computation-functions.md)
  Calculate the element-wise phase values, in radians, of a complex vector.
- [Complex conjugation functions](complex-conjugation-functions.md)
  Calculate the complex conjugate of the elements in a vector.
- [Vector squaring functions](vector-squaring-functions.md)
  Compute the square, signed square, or squared magnitude of the elements in a vector.
- [Fractional part extraction](fractional-part-extraction.md)
  Truncate the elements of a vector to a fraction.
- [Zero crossing search](zero-crossing-search.md)
  Count and find the zero crossings in a vector.
### Single-vector sliding-window operations
- [Sliding-window reduction functions](sliding-window-reduction-functions.md)
  Calculate maximum values and sums of values in a sliding window.
### Vector-to-vector spectra and coherence computation
- [Autospectrum computation](autospectrum-computation.md)
  Compute the element-wise sum of the squares of the real and imaginary parts of a complex vector.
- [Cross-spectrum computation](cross-spectrum-computation.md)
  Compute the element-wise product of a vector and the conjugate of a second vector.
- [Coherence function computation](coherence-function-computation.md)
  Compute the coherence of two vectors.
### Vector-to-vector extrema functions
- [Vector-to-vector minima and maxima](vector-to-vector-minima-and-maxima.md)
  Compute the element-wise minimum or maximum values or magnitudes in a vector.
- [Extrema finding functions](extrema-finding-functions.md)
  Extract the values from a vector that fall outside a range.
### Matrix operations
- [Multiplication](multiplication.md)
  Multiply vectors that contain real or complex values.
- [Transposition](transposition-vdsp.md)
  Tranpose vectors that contain real values.
- [Matrix and submatrix copying functions](matrix-and-submatrix-copying-functions.md)
  Copy the contents of a submatrix to another submatrix.
### Vector and matrix correlation and convolution
- [1D correlation and convolution](1d-correlation-and-convolution.md)
  Use correlation to compare and convolution to combine vectors of real or complex data.
- [2D convolution](2d-convolution.md)
  Perform convolution operations on matrices of real data.
### Vector and matrix Fourier transforms
- [Fast Fourier transforms](fast-fourier-transforms.md)
  Transform vectors and matrices of temporal and spatial domain complex values to the frequency domain, and vice versa.
- [Discrete Fourier transforms](discrete-fourier-transforms.md)
  Transform vectors of temporal and spatial domain complex values to the frequency domain, and vice versa.
- [Discrete Cosine transforms](discrete-cosine-transforms.md)
  Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.
### Data types
- [typealias vDSP_Length](vdsp_length.md)
  An unsigned-integer value that represents the size of vectors and the indices of elements in vectors.
- [typealias vDSP_Stride](vdsp_stride.md)
  An integer value that represents the differences between indices of elements, including the lengths of strides.
- [struct DSPComplex](dspcomplex.md)
  A structure that represents a single-precision complex value.
- [typealias COMPLEX_SPLIT](complex_split.md)
- [struct DSPDoubleComplex](dspdoublecomplex.md)
  A structure that represents a double-precision complex value.
- [typealias DOUBLE_COMPLEX_SPLIT](double_complex_split.md)
- [struct DSPSplitComplex](dspsplitcomplex.md)
  A structure that represents a single-precision complex vector with the real and imaginary parts stored in separate arrays.
- [struct DSPDoubleSplitComplex](dspdoublesplitcomplex.md)
  A structure that represents a double-precision complex vector with the real and imaginary parts stored in separate arrays.
- [struct VectorizableDouble](vdsp/vectorizabledouble.md)
  A structure that represents a double-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct VectorizableFloat](vdsp/vectorizablefloat.md)
  A structure that represents a single-precision real value for biquadratic filtering and discrete Fourier transforms.
### Constants
- [vDSP Compile-Time Version Information](vdsp-compile-time-version-information.md)
  The version of vDSP at compile time.

## See Also

- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)
  Operate selectively on the elements of a vector at regular intervals.
- [Using linear interpolation to construct new data points](using-linear-interpolation-to-construct-new-data-points.md)
  Fill the gaps in arrays of numerical data using linear interpolation.
- [Using vDSP for vector-based arithmetic](using-vdsp-for-vector-based-arithmetic.md)
  Increase the performance of common mathematical tasks with vDSP vector-vector and vector-scalar operations.
- [Resampling a signal with decimation](resampling-a-signal-with-decimation.md)
  Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp-library)*