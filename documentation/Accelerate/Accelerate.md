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
- [Decompressing and Parsing an Archived String](decompressing-and-parsing-an-archived-string.md)
  Recreate a string from an archive file.
### Compression
- [Compressing and Decompressing Files with Stream Compression](compressing-and-decompressing-files-with-stream-compression.md)
  Perform compression or the appropriate kind of decompression to a file based on its path extension.
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
### Protocols
- [protocol InitializableFromCGImage](initializablefromcgimage.md)
  A pixel format that supports initialization from a Core Graphics image.
- [protocol MultiplePlanePixelFormat](multipleplanepixelformat.md)
  A pixel format that contains multiple homogeneous planes represented by multiple underlying vImage buffers.
- [protocol PixelFormat](pixelformat.md)
  A pixel buffer pixel format.
- [protocol SinglePlanePixelFormat](singleplanepixelformat.md)
  A pixel format that contains a single underlying vImage buffer.
- [protocol StaticPixelFormat](staticpixelformat.md)
  A pixel format that’s known at compile time.
### Structures
- [struct DenseMatrix_Complex_Double](densematrix_complex_double.md)
  Contains a dense `rowCount` x `columnCount` matrix of complex double values stored in column-major order.
- [struct DenseMatrix_Complex_Float](densematrix_complex_float.md)
  Contains a dense `rowCount` x `columnCount` matrix of complex float values stored in column-major order.
- [struct DenseVector_Complex_Double](densevector_complex_double.md)
  Contains a dense vector of double complex values.
- [struct DenseVector_Complex_Float](densevector_complex_float.md)
  Contains a dense vector of float complex values.
- [struct SparseAttributesComplex_t](sparseattributescomplex_t.md)
  A type representing the attributes of a matrix.
- [struct SparseMatrixStructureComplex](sparsematrixstructurecomplex.md)
  A type representing the sparsity structure of a sparse complex matrix.
- [struct SparseMatrix_Complex_Double](sparsematrix_complex_double.md)
  A type representing a sparse complex matrix.
- [struct SparseMatrix_Complex_Float](sparsematrix_complex_float.md)
  A type representing a sparse complex matrix.
- [struct SparseOpaqueFactorization_Complex_Double](sparseopaquefactorization_complex_double.md)
  A semi-opaque type representing a matrix factorization in complex double.
- [struct SparseOpaqueFactorization_Complex_Float](sparseopaquefactorization_complex_float.md)
  A semi-opaque type representing a matrix factorization in complex float.
- [struct SparseOpaquePreconditioner_Complex_Double](sparseopaquepreconditioner_complex_double.md)
  Represents a preconditioner for matrices of complex double values .
- [struct SparseOpaquePreconditioner_Complex_Float](sparseopaquepreconditioner_complex_float.md)
  Represents a preconditioner for matrices of complex float values .
- [struct SparseOpaqueSubfactor_Complex_Double](sparseopaquesubfactor_complex_double.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).
- [struct SparseOpaqueSubfactor_Complex_Float](sparseopaquesubfactor_complex_float.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).
- [struct SparseUpdate_t](sparseupdate_t.md)
  Low-rank update algorithm selector
### Variables
- [var SparseFactorizationLU: SparseFactorization_t](sparsefactorizationlu.md)
  Types of factorization than can be performed.
- [var SparseFactorizationLUSPP: SparseFactorization_t](sparsefactorizationluspp.md)
  Types of factorization than can be performed.
- [var SparseFactorizationLUTPP: SparseFactorization_t](sparsefactorizationlutpp.md)
  Types of factorization than can be performed.
- [var SparseFactorizationLUUnpivoted: SparseFactorization_t](sparsefactorizationluunpivoted.md)
  Types of factorization than can be performed.
- [var SparseHermitian: SparseKind_t](sparsehermitian.md)
  A flag to describe the type of matrix represented.
- [var SparseSubfactorSc: SparseSubfactor_t](sparsesubfactorsc.md)
  Types of sub-factor object.
- [var SparseSubfactorSr: SparseSubfactor_t](sparsesubfactorsr.md)
  Types of sub-factor object.
- [var SparseUpdatePartialRefactor: SparseUpdate_t](sparseupdatepartialrefactor.md)
  Low-rank update algorithm selector
### Functions
- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](bnnsgraphcontextsetstreamingadvancecount(_:_:).md)
  Sets streaming advancement amount for cases with dynamically shaped inputs.
- [func SparseCleanup(SparseOpaquePreconditioner_Complex_Float)](sparsecleanup(_:)-1jxdh.md)
  Release a Sparse Preconditioner’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseOpaqueFactorization_Complex_Double)](sparsecleanup(_:)-28nz7.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseMatrix_Complex_Double)](sparsecleanup(_:)-3wccz.md)
  Release a Sparse matrix’s references to any memory allocated by the Sparse library.
- [func SparseCleanup(SparseOpaqueSubfactor_Complex_Float)](sparsecleanup(_:)-4enlt.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseMatrix_Complex_Float)](sparsecleanup(_:)-4z3l9.md)
  Release a Sparse matrix’s references to any memory allocated by the Sparse library.
- [func SparseCleanup(SparseOpaquePreconditioner_Complex_Double)](sparsecleanup(_:)-5ajx.md)
  Release a Sparse Preconditioner’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseOpaqueFactorization_Complex_Float)](sparsecleanup(_:)-61q1a.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseOpaqueSubfactor_Complex_Double)](sparsecleanup(_:)-7nhza.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributesComplex_t, UnsafePointer<Int32>, UnsafePointer<Int32>, OpaquePointer) -> SparseMatrix_Complex_Double](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:)-58kub.md)
  Convert from coordinate format arrays to a matrix of complex double values, dropping out-of-range entries and summing duplicates.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributesComplex_t, UnsafePointer<Int32>, UnsafePointer<Int32>, OpaquePointer) -> SparseMatrix_Complex_Float](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:)-58lgv.md)
  Convert from coordinate format arrays to a  matrix of complex float values, dropping out-of-range entries and summing duplicates.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributesComplex_t, UnsafePointer<Int32>, UnsafePointer<Int32>, OpaquePointer, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> SparseMatrix_Complex_Float](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-2blwb.md)
  Convert from coordinate format arrays to a  matrix of complex float values, dropping out-of-range entries and summing duplicates.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributesComplex_t, UnsafePointer<Int32>, UnsafePointer<Int32>, OpaquePointer, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> SparseMatrix_Complex_Double](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-6ocm1.md)
  Convert from coordinate format arrays to a  matrix of complex double values, dropping out-of-range entries and summing duplicates.
- [func SparseConvertFromOpaque(sparse_matrix_float_complex) -> SparseMatrix_Complex_Float](sparseconvertfromopaque(_:)-9ll2d.md)
  Converts an opaque matrix of complex float values object to a transparent sparse matrix object. When you are done with this matrix, release the memory that has been allocated by calling `SparseCleanup` on it.
- [func SparseConvertFromOpaque(sparse_matrix_double_complex) -> SparseMatrix_Complex_Double](sparseconvertfromopaque(_:)-9xju4.md)
  Converts an opaque matrix of complex double values object to a transparent sparse matrix object. When you are done with this matrix, release the memory that has been allocated by calling `SparseCleanup` on it.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Double) -> SparseOpaquePreconditioner_Complex_Double](sparsecreatepreconditioner(_:_:)-1yp4n.md)
  Create a preconditioner for the given matrix of complex double values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Float) -> SparseOpaquePreconditioner_Complex_Float](sparsecreatepreconditioner(_:_:)-95u9p.md)
  Create a preconditioner for the given matrix of complex float values.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparsecreatesubfactor(_:_:)-39487.md)
  Returns an opaque object representing a sub-factor of a factorization in complex double.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparsecreatesubfactor(_:_:)-udwd.md)
  Returns an opaque object representing a sub-factor of a factorization in complex float.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:)-1avkp.md)
  Returns the specified factorization of a sparse matrix of complex double values.
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructureComplex) -> SparseOpaqueSymbolicFactorization](sparsefactor(_:_:)-55tzk.md)
  Returns a symbolic factorization of the requested type for a complex matrix with the given structure.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:)-5zzpu.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:)-73n38.md)
  Returns the specified factorization of a sparse matrix of complex float values.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:)-7a3l4.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization.
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructureComplex, SparseSymbolicFactorOptions) -> SparseOpaqueSymbolicFactorization](sparsefactor(_:_:_:)-6s9g.md)
  Returns a symbolic factorization of the requested type for a complex matrix with the given structure, with the supplied options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:)-7kqvi.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:)-9ypz5.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization, using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:_:)-6hqfp.md)
  Returns the specified factorization of a sparse matrix of complex double values, using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:_:)-9ykfp.md)
  Returns the specified factorization of a sparse matrix of complex float values, using the specified options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:_:_:)-2dqfv.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:_:_:)-7j0dm.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.
- [func SparseGetConjugateTranspose(SparseMatrix_Complex_Float) -> SparseMatrix_Complex_Float](sparsegetconjugatetranspose(_:)-1e0js.md)
  Returns a conjugate transposed copy of the specified matrix of complex float values.
- [func SparseGetConjugateTranspose(SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparsegetconjugatetranspose(_:)-4hysc.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Float`.
- [func SparseGetConjugateTranspose(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparsegetconjugatetranspose(_:)-5hc5a.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Double`.
- [func SparseGetConjugateTranspose(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsegetconjugatetranspose(_:)-675y1.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Double`.
- [func SparseGetConjugateTranspose(SparseMatrix_Complex_Double) -> SparseMatrix_Complex_Double](sparsegetconjugatetranspose(_:)-9o30w.md)
  Returns a conjugate transposed copy of the specified specified matrix of complex double values.
- [func SparseGetConjugateTranspose(SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsegetconjugatetranspose(_:)-a56p.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Float`.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-2gc7f.md)
  Returns the inertia of an LDLT factorization in complex double.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Float, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-6ca5h.md)
  Returns the inertia of an LDLT factorization in complex float.
- [func SparseGetStateSize_Complex_Double(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_complex_double(_:_:_:_:_:).md)
  Returns size in bytes of state space required for call to `SparseIterate()` for complex double values.
- [func SparseGetStateSize_Complex_Float(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_complex_float(_:_:_:_:_:).md)
  Returns size in bytes of state space required for call to `SparseIterate()` for complex float values.
- [func SparseGetTranspose(SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsegettranspose(_:)-1fq2g.md)
  Returns a transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Float`.
- [func SparseGetTranspose(SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparsegettranspose(_:)-2fuzo.md)
  Returns a transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Float`.
- [func SparseGetTranspose(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparsegettranspose(_:)-4nr8u.md)
  Returns a transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Double`.
- [func SparseGetTranspose(SparseMatrix_Complex_Float) -> SparseMatrix_Complex_Float](sparsegettranspose(_:)-7dx1i.md)
  Returns a transposed copy of the specified matrix of complex float values.
- [func SparseGetTranspose(SparseMatrix_Complex_Double) -> SparseMatrix_Complex_Double](sparsegettranspose(_:)-9olfr.md)
  Returns a transposed copy of the specified matrix of complex double values.
- [func SparseGetTranspose(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsegettranspose(_:)-d0ny.md)
  Returns a transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Double`.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparseiterate(_:_:_:_:_:_:_:_:)-315ym.md)
  Perform a single iteration of the specified iterative method for complex double values.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparseiterate(_:_:_:_:_:_:_:_:)-9v7qh.md)
  Perform a single iteration of the specified iterative method for complex float values.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double)](sparseiterate(_:_:_:_:_:_:_:_:_:)-1wv28.md)
  Perform a single iteration of the specified iterative method for complex double values with preconditioner.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparseOpaquePreconditioner_Complex_Float)](sparseiterate(_:_:_:_:_:_:_:_:_:)-4td1l.md)
  Perform a single iteration of the specified iterative method for complex float values with preconditioner.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiply(_:_:)-34fp6.md)
  Perform the multiply operation `Y = Subfactor * X` in place for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsemultiply(_:_:)-3dwed.md)
  Perform the multiply operation `y = Subfactor * x` for complex floatr values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](sparsemultiply(_:_:)-3s0hu.md)
  Perform the multiply operation `Y = Subfactor * X` in place for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double)](sparsemultiply(_:_:)-9fn7j.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values, in place.
- [func SparseMultiply(SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsemultiply(_:_:_:)-1sjuk.md)
  Performs the multiplication `Y = AX` for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsemultiply(_:_:_:)-4fwfv.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsemultiply(_:_:_:)-58wuo.md)
  Perform the multiply operation `y = Subfactor * x` for complex float values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-5etjg.md)
  Perform the multiply operation `y = Subfactor * x` in place for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-5kh07.md)
  Perform the multiply operation `y = Subfactor * x` in place for complex float values.
- [func SparseMultiply(SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsemultiply(_:_:_:)-6gzb3.md)
  Performs the multiplication `y = Ax` for complex float values
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-6strd.md)
  Perform the multiply operation `Y = Subfactor * X `for complex float values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiply(_:_:_:)-6wrnf.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.
- [func SparseMultiply(SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsemultiply(_:_:_:)-6xiv8.md)
  Performs the multiplication `y = Ax` for complex double values
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-7mdi8.md)
  Perform the multiply operation `Y = Subfactor * X `for complex double values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsemultiply(_:_:_:)-7q8gs.md)
  Perform the multiply operation `Y = Subfactor * X` for complex double values.
- [func SparseMultiply(SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiply(_:_:_:)-85a24.md)
  Performs the multiplication `Y = AX` for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-4xr8.md)
  Perform the multiply operation `y = Subfactor * x` for complex float values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-581zl.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-7xipz.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-9v0nu.md)
  Perform the multiply operation `Y = Subfactor * X` for complex double values.
- [func SparseMultiplyAdd(SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiplyadd(_:_:_:)-4dpyu.md)
  Performs `Y += AX` for complex float values
- [func SparseMultiplyAdd(SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsemultiplyadd(_:_:_:)-658zk.md)
  Performs `Y += AX` for complex double values
- [func SparseMultiplyAdd(SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsemultiplyadd(_:_:_:)-6qi0p.md)
  Performs `y += Ax` for complex double values
- [func SparseMultiplyAdd(SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsemultiplyadd(_:_:_:)-8dqy7.md)
  Performs `y += Ax` for complex float values
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>)](sparserefactor(_:_:)-mgni.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>)](sparserefactor(_:_:)-zegz.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-4chx2.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, using different options.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-4ofvz.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, without any internal allocations.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-593yb.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, without any internal allocations.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-q0va.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, using different options.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-201rh.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, using updated options and without any internal allocations.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-20xqc.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, using updated options and without any internal allocations.
- [func SparseRetain(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparseretain(_:)-5sahb.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparseretain(_:)-6pp40.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparseretain(_:)-92857.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparseretain(_:)-92v4w.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:)-1psgz.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:)-31yj7.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:)-3x0vj.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-4fydu.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:)-4j17a.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-5apxy.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:)-78cl0.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:)-879na.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-2qlwo.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex float values in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:_:)-2rk1c.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of A`,` in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-3482l.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-34okt.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:_:)-3hev5.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-3qkkl.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:_:)-48njk.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of A`,` in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-6pudz.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex double values in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:_:)-76ge0.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:_:)-7day5.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:_:)-7krer.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-7ltk8.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:_:)-7qdpl.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:_:)-85y2u.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-8ikjb.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-90ojf.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Float, DenseVector_Complex_Float) -> Void, DenseVector_Complex_Float, DenseVector_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-2cenj.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Double, DenseVector_Complex_Double) -> Void, DenseVector_Complex_Double, DenseVector_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-35kl2.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-41c6p.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-4xwsw.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-5stp5.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-5xn6p.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6afcf.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6demt.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6od6k.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-6wjj9.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-7mtyx.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, and without any internal memory allocations.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-7zp1d.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-8bndu.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-8yld7.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-9ui81.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-9xxqn.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-155od.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-1fw3p.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-1i6u8.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Double, DenseVector_Complex_Double) -> Void, DenseVector_Complex_Double, DenseVector_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-1ogxn.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Float, DenseVector_Complex_Float) -> Void, DenseVector_Complex_Float, DenseVector_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-2bm9r.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-2ygeh.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-4fvqm.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-4xd4z.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-655i9.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7hdp4.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7m9vp.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7yfqx.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, Int32, UnsafePointer<Int32>, SparseMatrix_Complex_Float)](sparseupdatefactor(_:_:_:_:_:)-1n2be.md)
  Apply a low-rank update to an existing factorization of a matrix of complex float values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, Int32, UnsafePointer<Int32>, SparseMatrix_Complex_Double)](sparseupdatefactor(_:_:_:_:_:)-9h956.md)
  Apply a low-rank update to an existing factorization of a matrix of complex double values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, Int32, UnsafePointer<Int32>, SparseMatrix_Float)](sparseupdatefactor(_:_:_:_:_:)-9qg54.md)
  Apply a low-rank update to an existing factorization of a matrix of float values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, Int32, UnsafePointer<Int32>, SparseMatrix_Double)](sparseupdatefactor(_:_:_:_:_:)-wrqg.md)
  Apply a low-rank update to an existing factorization of a matrix of double values.
- [func cgedmd_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<__LAPACK_int>, OpaquePointer?, OpaquePointer?, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](cgedmd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgedmdq_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<__LAPACK_int>, OpaquePointer?, OpaquePointer?, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](cgedmdq_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, OpaquePointer, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](cgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func claqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, OpaquePointer, UnsafeMutablePointer<__LAPACK_int>)](claqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func claqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_bool>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, OpaquePointer?, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](claqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func crscl_(UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](crscl_(_:_:_:_:).md)
- [func dgedmd_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](dgedmd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func dgedmdq_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](dgedmdq_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func dgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](dgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func dlaqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>)](dlaqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func dlaqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_bool>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](dlaqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func sgedmd_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](sgedmd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func sgedmdq_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](sgedmdq_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func sgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](sgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func slaqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>)](slaqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func slaqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_bool>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](slaqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func sparse_elementwise_norm_double_complex(sparse_matrix_double_complex!, sparse_norm) -> Double](sparse_elementwise_norm_double_complex(_:_:).md)
- [func sparse_elementwise_norm_float_complex(sparse_matrix_float_complex!, sparse_norm) -> Float](sparse_elementwise_norm_float_complex(_:_:).md)
- [func sparse_extract_block_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, OpaquePointer!) -> sparse_status](sparse_extract_block_double_complex(_:_:_:_:_:_:).md)
- [func sparse_extract_block_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, OpaquePointer!) -> sparse_status](sparse_extract_block_float_complex(_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_column_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_double_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_column_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_row_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_double_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_row_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_get_vector_nonzero_count_double_complex(sparse_dimension, OpaquePointer!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_double_complex(_:_:_:).md)
- [func sparse_get_vector_nonzero_count_float_complex(sparse_dimension, OpaquePointer!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_float_complex(_:_:_:).md)
- [func sparse_insert_block_double_complex(sparse_matrix_double_complex!, OpaquePointer!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](sparse_insert_block_double_complex(_:_:_:_:_:_:).md)
- [func sparse_insert_block_float_complex(sparse_matrix_float_complex!, OpaquePointer!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](sparse_insert_block_float_complex(_:_:_:_:_:_:).md)
- [func sparse_insert_col_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_col_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_float_complex(_:_:_:_:_:).md)
- [func sparse_insert_entries_double_complex(sparse_matrix_double_complex!, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_entries_float_complex(sparse_matrix_float_complex!, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_float_complex(_:_:_:_:_:).md)
- [func sparse_insert_row_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_row_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_float_complex(_:_:_:_:_:).md)
- [func sparse_matrix_block_create_double_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_double_complex!](sparse_matrix_block_create_double_complex(_:_:_:_:).md)
- [func sparse_matrix_block_create_float_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_float_complex!](sparse_matrix_block_create_float_complex(_:_:_:_:).md)
- [func sparse_matrix_create_double_complex(sparse_dimension, sparse_dimension) -> sparse_matrix_double_complex!](sparse_matrix_create_double_complex(_:_:).md)
- [func sparse_matrix_create_float_complex(sparse_dimension, sparse_dimension) -> sparse_matrix_float_complex!](sparse_matrix_create_float_complex(_:_:).md)
- [func sparse_matrix_variable_block_create_double_complex(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_double_complex!](sparse_matrix_variable_block_create_double_complex(_:_:_:_:).md)
- [func sparse_matrix_variable_block_create_float_complex(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_float_complex!](sparse_matrix_variable_block_create_float_complex(_:_:_:_:).md)
- [func sparse_operator_norm_double_complex(sparse_matrix_double_complex!, sparse_norm) -> Double](sparse_operator_norm_double_complex(_:_:).md)
- [func sparse_operator_norm_float_complex(sparse_matrix_float_complex!, sparse_norm) -> Float](sparse_operator_norm_float_complex(_:_:).md)
- [func sparse_pack_vector_double_complex(sparse_dimension, sparse_dimension, OpaquePointer!, sparse_stride, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_double_complex(_:_:_:_:_:_:).md)
- [func sparse_pack_vector_float_complex(sparse_dimension, sparse_dimension, OpaquePointer!, sparse_stride, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_float_complex(_:_:_:_:_:_:).md)
- [func sparse_permute_cols_double_complex(sparse_matrix_double_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_double_complex(_:_:).md)
- [func sparse_permute_cols_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_float_complex(_:_:).md)
- [func sparse_permute_rows_double_complex(sparse_matrix_double_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_rows_double_complex(_:_:).md)
- [func sparse_permute_rows_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_rows_float_complex(_:_:).md)
- [func sparse_unpack_vector_double_complex(sparse_dimension, sparse_dimension, Bool, OpaquePointer!, UnsafePointer<sparse_index>!, OpaquePointer!, sparse_stride)](sparse_unpack_vector_double_complex(_:_:_:_:_:_:_:).md)
- [func sparse_unpack_vector_float_complex(sparse_dimension, sparse_dimension, Bool, OpaquePointer!, UnsafePointer<sparse_index>!, OpaquePointer!, sparse_stride)](sparse_unpack_vector_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_vector_norm_double_complex(sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, sparse_norm) -> Double](sparse_vector_norm_double_complex(_:_:_:_:).md)
- [func sparse_vector_norm_float_complex(sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, sparse_norm) -> Float](sparse_vector_norm_float_complex(_:_:_:_:).md)
- [func zgedmd_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<__LAPACK_int>, OpaquePointer?, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](zgedmd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zgedmdq_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<__LAPACK_int>, OpaquePointer?, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](zgedmdq_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, OpaquePointer, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](zgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zlaqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, OpaquePointer, UnsafeMutablePointer<__LAPACK_int>)](zlaqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zlaqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_bool>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, OpaquePointer?, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](zlaqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zrscl_(UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](zrscl_(_:_:_:_:).md)
### Type Aliases
- [typealias sparse_matrix_double_complex](sparse_matrix_double_complex.md)
- [typealias sparse_matrix_float_complex](sparse_matrix_float_complex.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate)*