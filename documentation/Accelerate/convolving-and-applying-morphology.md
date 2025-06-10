# Convolving and applying morphology

**Framework**: Accelerate

Apply convolution, dilation, or erosion to a pixel buffer.

## Topics

### Morphology
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-2bbx4.md)
  Applies a morphology operation to an 8-bit planar pixel buffer.
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-9f8lh.md)
  Applies a morphology operation to a 32-bit planar pixel buffer.
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-1wacj.md)
  Applies a morphology operation to an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-65xg3.md)
  Applies a morphology operation to a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [vImage.MorphologyOperation](vimage/morphologyoperation.md)
  Describes which morphology operation to perform.
- [typealias StructuringElement](vimage/structuringelement.md)
  A 2D matrix that represents a morphology kernel.
### General convolution
- [func convolve(with: vImage.ConvolutionKernel2D<Int16>, divisor: Int32?, bias: Int32?, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:divisor:bias:edgemode:destination:)-4o5w6.md)
  Convolves an 8-bit planar pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_16F>, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:usefloat16accumulator:destination:)-1xkvu.md)
  Convolves a floating-point 16-bit planar pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:destination:)-tn07.md)
  Convolves a 32-bit planar pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Int16>, divisor: Int32?, bias: Int32?, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:divisor:bias:edgemode:destination:)-1oul9.md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func convolve(with: (vImage.ConvolutionKernel2D<Int16>, vImage.ConvolutionKernel2D<Int16>, vImage.ConvolutionKernel2D<Int16>, vImage.ConvolutionKernel2D<Int16>), divisors: (Int32, Int32, Int32, Int32)?, biases: (Int32, Int32, Int32, Int32), edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:divisors:biases:edgemode:destination:).md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer with separate kernels for each channel.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_ARGB_16F>, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:usefloat16accumulator:destination:)-81lqa.md)
  Convolves a floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_FFFF>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:destination:)-8syhw.md)
  Convolves a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Int16>, divisor: Int32?, bias: Int32?, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:divisor:bias:edgemode:destination:)-4jjbx.md)
  Convolves an 8-bit multiple plane pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:destination:)-3219s.md)
  Convolves a 32-bit multiple plane pixel buffer.
- [vImage.EdgeMode](vimage/edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.ConvolutionKernel2D](vimage/convolutionkernel2d.md)
  A 2D matrix that represents a convolution kernel.
### Separable convolution
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_16U>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-2iyq6.md)
  Performs separable convolution on an 8-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_16F>, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:usefloat16accumulator:destination:).md)
  Performs separable convolution on a 16-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-2qofv.md)
  Performs separable convolution on a 32-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_16U>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-6t9b3.md)
  Performs separable convolution on a multiple plane 8-bit pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-6q5ro.md)
  Performs separable convolution on a multiple plane 32-bit pixel buffer.
- [vImage.ConvolutionKernel](vimage/convolutionkernel.md)
  Constants that describe 1D convolution kernels.
### Box convolution
- [func boxConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/boxconvolve(kernelsize:edgemode:destination:)-2h7fy.md)
  Convolves an 8-bit planar pixel buffer with a box filter.
- [func boxConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/boxconvolve(kernelsize:edgemode:destination:)-2m20d.md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer with a box filter.
- [func boxConvolved(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>) -> vImage.PixelBuffer<Format>](vimage/pixelbuffer/boxconvolved(kernelsize:edgemode:).md)
  Returns a box-filter convolved 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func boxConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/boxconvolve(kernelsize:edgemode:destination:)-3kabm.md)
  Convolves a multiple-plane 8-bit-per-channel pixel buffer with a box filter.
### Tent convolution
- [func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/tentconvolve(kernelsize:edgemode:destination:)-1fpap.md)
  Convolves an 8-bit planar pixel buffer with a tent filter.
- [func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/tentconvolve(kernelsize:edgemode:destination:)-150xp.md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer with a tent filter.
- [func tentConvolved(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>) -> vImage.PixelBuffer<Format>](vimage/pixelbuffer/tentconvolved(kernelsize:edgemode:).md)
  Returns a tent-filter convolved 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/tentconvolve(kernelsize:edgemode:destination:)-2dp48.md)
  Convolves a multiple-plane 8-bit-per-channel pixel buffer with a tent filter.

## See Also

- [Applying geometric operations to pixel buffers](applying-geometric-operations-to-pixel-buffers.md)
  Reflect, shear, rotate, scale, and apply affine transforms to image data.
- [Applying color transforms to pixel buffers](applying-color-transforms-to-pixel-buffers.md)
  Adjust the colors of an image by applying gamma, polynomials, or multidimensional lookup.
- [Blending and compositing pixel buffers](blending-and-compositing-pixel-buffers.md)
  Composite two pixel buffers to create a single image.
- [Thresholding and clipping pixel buffer values](thresholding-and-clipping-pixel-buffer-values.md)
  Limit the values in a pixel buffer to a threshold or a range.
- [Calculating and transforming histograms](calculating-and-transforming-histograms.md)
  Enhance and adjust the contrast of an image with histogram equalization, contrast stretching, and specification.
- [Converting pixel buffers](converting-pixel-buffers.md)
  Convert pixel buffer data between different bit-depths.
- [Interleaving and deinterleaving pixel buffers](interleaving-and-deinterleaving-pixel-buffers.md)
  Convert pixel buffer data between interleaved and planar formats.
- [Cropping and working with regions of interest](cropping-and-working-with-regions-of-interest.md)
  Crop images and apply operations to regions of interest.
- [Applying channel operations](applying-channel-operations.md)
  Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/convolving-and-applying-morphology)*