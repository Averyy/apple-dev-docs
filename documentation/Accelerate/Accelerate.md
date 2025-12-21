# Accelerate

**Framework**: Accelerate  
**Kind**: module

Make large-scale mathematical computations and image calculations, optimized for high performance and low energy consumption.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

Accelerate provides high-performance, energy-efficient computation on the CPU by leveraging its vector-processing capability. The following Accelerate libraries abstract that capability so that code written for them executes appropriate instructions for the processor available at runtime:

Although not part of the Accelerate framework, the following libraries are closely related:

## Topics

### Neural Networks
- [Training a neural network to recognize digits](training-a-neural-network-to-recognize-digits.md)
  Build a simple neural network and train it to recognize randomly generated numbers.
- [BNNS](bnns-library.md)
  Implement and run neural networks for training and inference.
### Directories, Files, and Data Archives
- [Compressing single files](compressing-single-files.md)
  Compress a single file and store the result on the file system.
- [Decompressing single files](decompressing-single-files.md)
  Recreate a single file from a compressed file.
- [Compressing file system directories](compressing-file-system-directories.md)
  Compress the contents of an entire directory and store the result on the file system.
- [Decompressing and extracting an archived directory](decompressing-and-extracting-an-archived-directory.md)
  Recreate an entire file system directory from an archive file.
- [Compressing and saving a string to the file system](compressing-and-saving-a-string-to-the-file-system.md)
  Compress the contents of a Unicode string and store the result on the file system.
- [Decompressing and parsing an archived string](decompressing-and-parsing-an-archived-string.md)
  Recreate a string from an archive file.
### Compression
- [Compressing and decompressing files with stream compression](compressing-and-decompressing-files-with-stream-compression.md)
  Perform compression for all files and decompression for files with supported extension types.
- [Compressing and decompressing data with buffer compression](compressing-and-decompressing-data-with-buffer-compression.md)
  Compress a string, write it to the file system, and decompress the same file using buffer compression.
- [Compressing and decompressing data with input and output filters](compressing-and-decompressing-data-with-input-and-output-filters.md)
  Compress and decompress streamed or from-memory data, using input and output filters.
### Image Processing Essentials
- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)
  Initialize vImage buffers from Core Graphics images.
- [Creating a Core Graphics Image from a vImage Buffer](creating-a-core-graphics-image-from-a-vimage-buffer.md)
  Create displayable representations of vImage buffers.
- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)
  Resize an image with vImage.
- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
  Limit the effect of vImage operations to rectangular regions of interest.
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
  Improve your app’s performance by converting image buffer formats from interleaved to planar.
- [vImage](vimage-library.md)
  Manipulate large images using the CPU’s vector processor.
### Signal Processing Essentials
- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)
  Operate selectively on the elements of a vector at regular intervals.
- [Using linear interpolation to construct new data points](using-linear-interpolation-to-construct-new-data-points.md)
  Fill the gaps in arrays of numerical data using linear interpolation.
- [Using vDSP for vector-based arithmetic](using-vdsp-for-vector-based-arithmetic.md)
  Increase the performance of common mathematical tasks with vDSP vector-vector and vector-scalar operations.
- [Resampling a signal with decimation](resampling-a-signal-with-decimation.md)
  Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.
- [vDSP](vdsp-library.md)
  Perform basic arithmetic operations and common digital signal processing (DSP) routines on large vectors.
### Fourier and Cosine Transforms
- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Finding the component frequencies in a composite sine wave](finding-the-component-frequencies-in-a-composite-sine-wave.md)
  Use 1D fast Fourier transform to compute the frequency components of a signal.
- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
  Optimize discrete Fourier transform (DFT) performance with the vDSP interleaved DFT routines.
- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [Signal extraction from noise](signal-extraction-from-noise.md)
  Use Accelerate’s discrete cosine transform to remove noise from a signal.
- [Performing Fourier Transforms on Multiple Signals](performing-fourier-transforms-on-multiple-signals.md)
  Use Accelerate’s multiple-signal fast Fourier transform (FFT) functions to transform multiple signals with a single function call.
- [Halftone descreening with 2D fast Fourier transform](halftone-descreening-with-2d-fast-fourier-transform.md)
  Reduce or remove periodic artifacts from images.
- [Fast Fourier transforms](fast-fourier-transforms.md)
  Transform vectors and matrices of temporal and spatial domain complex values to the frequency domain, and vice versa.
- [Discrete Fourier transforms](discrete-fourier-transforms.md)
  Transform vectors of temporal and spatial domain complex values to the frequency domain, and vice versa.
- [Discrete Cosine transforms](discrete-cosine-transforms.md)
  Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.
### Core Video Interoperation
- [Using vImage pixel buffers to generate video effects](using-vimage-pixel-buffers-to-generate-video-effects.md)
  Render real-time video effects with the vImage Pixel Buffer.
- [Integrating vImage pixel buffers into a Core Image workflow](integrating-vimage-pixel-buffers-into-a-core-image-workflow.md)
  Share image data between Core Video pixel buffers and vImage buffers to integrate vImage operations into a Core Image workflow.
- [Applying vImage operations to video sample buffers](applying-vimage-operations-to-video-sample-buffers.md)
  Use the vImage convert-any-to-any functionality to perform real-time image processing of video frames streamed from your device’s camera.
- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [Core Video interoperability](core-video-interoperability.md)
  Pass image data between Core Video and vImage.
### Vectors, Matrices, and Quaternions
- [Working with Vectors](working-with-vectors.md)
  Use vectors to calculate geometric values, calculate dot products and cross products, and interpolate between values.
- [Working with Matrices](working-with-matrices.md)
  Solve simultaneous equations and transform points in space.
- [Working with Quaternions](working-with-quaternions.md)
  Rotate points around the surface of a sphere, and interpolate between them.
- [Rotating a cube by transforming its vertices](rotating-a-cube-by-transforming-its-vertices.md)
  Rotate a cube through a series of keyframes using quaternion interpolation to transition between them.
- [simd](simd-library.md)
  Perform computations on small vectors and matrices.
- [vForce](vforce-library.md)
  Perform transcendental and trigonometric functions on vectors of any length.
### Audio Processing
- [Visualizing sound as an audio spectrogram](visualizing-sound-as-an-audio-spectrogram.md)
  Share image data between vDSP and vImage to visualize audio that a device microphone captures.
- [Applying biquadratic filters to a music loop](applying-biquadratic-filters-to-a-music-loop.md)
  Change the frequency response of an audio signal using a cascaded biquadratic filter.
- [Equalizing audio with discrete cosine transforms (DCTs)](equalizing-audio-with-discrete-cosine-transforms-dcts.md)
  Change the frequency response of an audio signal by manipulating frequency-domain data.
- [Biquadratic IIR filters](biquadratic-iir-filters.md)
  Apply biquadratic filters to single-channel and multichannel data.
- [Discrete Cosine transforms](discrete-cosine-transforms.md)
  Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.
### Conversion Between Image Formats
- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
  Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.
- [Converting color images to grayscale](converting-color-images-to-grayscale.md)
  Convert an RGB image to grayscale using matrix multiplication.
- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)
  Precompute translation values to optimize color space conversion and other pointwise operations.
- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
  Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.
- [Converting luminance and chrominance planes to an ARGB image](converting-luminance-and-chrominance-planes-to-an-argb-image.md)
  Create a displayable ARGB image using the luminance and chrominance information from your device’s camera.
- [Conversion](conversion.md)
  Convert an image to a different format.
### Image Resampling
- [Resampling in vImage](resampling-in-vimage.md)
  Learn how vImage resamples image data during geometric operations.
- [Reducing artifacts with custom resampling filters](reducing-artifacts-with-custom-resampling-filters.md)
  Implement custom linear interpolation to prevent the ringing effects associated with scaling an image with the default Lanczos algorithm.
- [Image shearing](image-shearing.md)
  Shear images horizontally and vertically.
### Convolution and Morphology
- [Blurring an image](blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [Adding a bokeh effect to images](adding-a-bokeh-effect-to-images.md)
  Simulate a bokeh effect by applying dilation.
- [Convolution](convolution.md)
  Apply a convolution kernel to an image.
- [Morphology](morphology.md)
  Dilate and erode images.
### Color and Tone Adjustment
- [Adjusting the brightness and contrast of an image](adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [Applying tone curve adjustments to images](applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [Adjusting the hue of an image](adjusting-the-hue-of-an-image.md)
  Convert an image to L*a*b* color space and apply hue adjustment.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Histogram](histogram.md)
  Calculate or manipulate an image’s histogram.
### vImage / vDSP Interoperability
- [Finding the sharpest image in a sequence of captured images](finding-the-sharpest-image-in-a-sequence-of-captured-images.md)
  Share image data between vDSP and vImage to compute the sharpest image from a bracketed photo sequence.
- [Visualizing sound as an audio spectrogram](visualizing-sound-as-an-audio-spectrogram.md)
  Share image data between vDSP and vImage to visualize audio that a device microphone captures.
### Sparse Matrices
- [Creating sparse matrices](creating-sparse-matrices.md)
  Create sparse matrices for factorization and solving systems.
- [Solving systems using direct methods](solving-systems-using-direct-methods.md)
  Use direct methods to solve systems of equations where the coefficient matrix is sparse.
- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)
  Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Creating a sparse matrix from coordinate format arrays](creating-a-sparse-matrix-from-coordinate-format-arrays.md)
  Use separate coordinate format arrays to create sparse matrices.
- [Sparse Solvers](sparse-solvers-library.md)
  Solve systems of equations where the coefficient matrix is sparse.
### Arithmetic and Transcendental Functions
- [vecLib](veclib.md)
  Perform computations on large vectors.
### Linear Algebra
- [Solving systems of linear equations with LAPACK](solving-systems-of-linear-equations-with-lapack.md)
  Select the optimal LAPACK routine to solve a system of linear equations.
- [Finding an interpolating polynomial using the Vandermonde method](finding-an-interpolating-polynomial-using-the-vandermonde-method.md)
  Use LAPACK to solve a linear system and find an interpolating polynomial to construct new points between a series of known data points.
- [Compressing an image using linear algebra](compressing-an-image-using-linear-algebra.md)
  Reduce the storage size of an image using singular value decomposition (SVD).
- [BLAS](blas-library.md)
  Perform common linear algebra operations with Apple’s implementation of the Basic Linear Algebra Subprograms (BLAS).
### Definite Integration
- [Quadrature](quadrature.md)
  Approximate the definite integral of a function over a finite or infinite interval.
### Macros
- [Macros](macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Accelerate)*