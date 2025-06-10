# Applying arithmetic operations

**Framework**: Accelerate

Multiply the pixel values of a buffer by scalar values or matrices.

## Topics

### Scalar Multiplication
- [func multiply(by: Int, divisor: Int, preBias: Int, postBias: Int, destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-7jo6v.md)
  Multiplies each pixel in an 8-bit planar pixel buffer by the specified factor.
- [func multiply(by: Float, preBias: Float, postBias: Float, destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-3bh2a.md)
  Multiplies each pixel in a 32-bit planar pixel buffer by the specified factor.
### Matrix Multiplication
- [func multiply<Matrix>(by: Matrix, divisor: Int, preBias: (Int, Int, Int, Int), postBias: (Int, Int, Int, Int), destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-7ikb7.md)
  Multiplies each four channel pixel in an 8-bit-per channel, 4-channel pixel buffer by a 4 x 4 matrix to produce a four channel result.
- [func multiply<Matrix>(by: Matrix, preBias: (Float, Float, Float, Float), postBias: (Float, Float, Float, Float), destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-5tm47.md)
  Multiplies each four channel pixel in a 32-bit-per channel, 4-channel pixel buffer by a 4 x 4 matrix to produce a four channel result.
- [func multiply(by: simd_float4x4, preBias: (Float, Float, Float, Float), postBias: (Float, Float, Float, Float), destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-5tq68.md)
  Multiplies each four channel pixel in a 32-bit-per channel, 4-channel pixel buffer by a 4 x 4 simd matrix to produce a four channel result.
- [func multiply<Matrix, DestFormat>(by: Matrix, divisor: Int, preBias: [Int], postBias: [Int], destination: vImage.PixelBuffer<DestFormat>)](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-86hbw.md)
  Multiplies each four channel pixel in an 8-bit multiple-plane pixel buffer by a 4 x 4 matrix to produce a four channel result.
- [func multiply<Matrix, DestFormat>(by: Matrix, preBias: [Float], postBias: [Float], destination: vImage.PixelBuffer<DestFormat>)](vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-3kltz.md)
  Multiplies each four channel pixel in a 32-bit multiple-plane pixel buffer by a 4 x 4 matrix to produce a four channel result.
### Pixel Multiplication
- [func multiply(by: (Int, Int, Int, Int), divisor: Int, preBias: (Int, Int, Int, Int), postBias: Int, destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-4q614.md)
  Multiplies each four channel pixel in an 8-bit-per channel, 4-channel pixel buffer by a four element matrix to produce a single channel result.
- [func multiply(by: (Float, Float, Float, Float), preBias: (Float, Float, Float, Float), postBias: Float, destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-1sp5l.md)
  Multiplies each four channel pixel in a 32-bit-per channel, 4-channel pixel buffer by a four element matrix to produce a single channel result.

## See Also

- [Applying geometric operations to pixel buffers](applying-geometric-operations-to-pixel-buffers.md)
  Reflect, shear, rotate, scale, and apply affine transforms to image data.
- [Applying color transforms to pixel buffers](applying-color-transforms-to-pixel-buffers.md)
  Adjust the colors of an image by applying gamma, polynomials, or multidimensional lookup.
- [Blending and compositing pixel buffers](blending-and-compositing-pixel-buffers.md)
  Composite two pixel buffers to create a single image.
- [Convolving and applying morphology](convolving-and-applying-morphology.md)
  Apply convolution, dilation, or erosion to a pixel buffer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-arithmetic-operations)*