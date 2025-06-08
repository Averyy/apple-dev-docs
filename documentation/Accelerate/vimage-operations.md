# vImage Operations

**Framework**: Accelerate

Apply image manipulation operations to vImage buffers.

#### Overview

A vImage function name includes the data type of the buffer it operates on. For example, [`vImageConvolve_Planar8(_:_:_:_:_:_:_:_:_:_:_:)`](vimageconvolve_planar8(_:_:_:_:_:_:_:_:_:_:_:).md) works with 8-bit planar buffers, and [`vImageConvolve_ARGBFFFF(_:_:_:_:_:_:_:_:_:_:)`](vimageconvolve_argbffff(_:_:_:_:_:_:_:_:_:_:).md) works with 32-bits-per-channel, four-channel interleaved buffers.

## Topics

### Applying color transforms to images
- [Transforming with lookup tables](transforming-with-lookup-tables.md)
  Use lookup tables to apply color transformations to images.
- [Transforming with polynomials](transforming-with-polynomials.md)
  Use polynomials to apply color transformations to images.
- [Transforming with matrix multiplication](transforming-with-matrix-multiplication.md)
  Use matrix multiplication to apply color transformations to images.
- [Transforming with a gamma function](transforming-with-a-gamma-function.md)
  Use gamma functions to apply color transformations to images.
- [Applying a flood fill to an image](applying-a-flood-fill-to-an-image.md)
  Fill connected components of an image with a new color.
### Applying geometric transforms to image buffers
- [Resampling in vImage](resampling-in-vimage.md)
  Learn how vImage resamples image data during geometric operations.
- [Applying affine transformations to images](applying-affine-transformations-to-images.md)
  Translate, rotate, and scale images.
- [Applying projective transformations to images](applying-projective-transformations-to-images.md)
  Warp images in three dimensions.
- [Image reflection](image-reflection.md)
  Reflect images horizontally and vertically.
- [Image shearing](image-shearing.md)
  Shear images horizontally and vertically.
- [Image rotation](image-rotation.md)
  Rotate images by arbitrary angles or by multiples of 90 degrees.
- [Image scaling](image-scaling.md)
  Scale interlaced and planar images.
- [Getting the Buffer Size](getting-the-buffer-size.md)
  Calculate the size of the temporary buffer needed by a high-level geometry functions.
### Applying morphological operations to images
- [Morphology](morphology.md)
  Dilate and erode images.
### Calculating and modifying an image’s histogram
- [Histogram](histogram.md)
  Calculate or manipulate an image’s histogram.
### Clipping data
- [Clipping data](clipping-data.md)
  Clip the pixel values of an image.
### Compositing images using alpha information
- [Alpha compositing](alpha-compositing.md)
  Composite images together.
### Converting image buffers between formats
- [Conversion](conversion.md)
  Convert an image to a different format.
### Convolving images
- [Convolution](convolution.md)
  Apply a convolution kernel to an image.
### Extracting channels
- [Extracting channels](extracting-channels.md)
  Extract one channel from a four-channel interleaved buffer.
### Filling buffers
- [Filling buffers](filling-buffers.md)
  Fill a buffer with a specified color.
### Filtering data prior to decompressing
- [Decompression Filtering](decompression-filtering.md)
  Filter data prior to decompression.
### Flattening data
- [Flattening data](flattening-data.md)
  Perform an alpha composite of a four-channel image over a solid background color.
### Overwriting channels
- [Overwriting channels](overwriting-channels.md)
  Overwrite the channels of a buffer.
### Permuting channels
- [Permuting Channels](permuting-channels.md)
  Reorder the channels in an image.
### Swapping bytes
- [Swapping bytes](swapping-bytes.md)
  Byte-swap a buffer.

## See Also

- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [Blurring an image](blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [Adding a bokeh effect to images](adding-a-bokeh-effect-to-images.md)
  Simulate a bokeh effect by applying dilation.
- [Converting color images to grayscale](converting-color-images-to-grayscale.md)
  Convert an RGB image to grayscale using matrix multiplication.
- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
  Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Reducing artifacts with custom resampling filters](reducing-artifacts-with-custom-resampling-filters.md)
  Implement custom linear interpolation to prevent the ringing effects associated with scaling an image with the default Lanczos algorithm.
- [Finding the sharpest image in a sequence of captured images](finding-the-sharpest-image-in-a-sequence-of-captured-images.md)
  Share image data between vDSP and vImage to compute the sharpest image from a bracketed photo sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage-operations)*