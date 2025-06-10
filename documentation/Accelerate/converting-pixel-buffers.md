# Converting pixel buffers

**Framework**: Accelerate

Convert pixel buffer data between different bit-depths.

## Topics

### Conversion from YUV to RGB
- [func convert(lumaSource: vImage.PixelBuffer<vImage.Planar8>, chromaSource: vImage.PixelBuffer<vImage.Interleaved8x2>, conversionInfo: vImage_YpCbCrToARGB)](vimage/pixelbuffer/convert(lumasource:chromasource:conversioninfo:).md)
  Populates the pixel buffer with ARGB data from the given luminance and chrominance pixel buffers.
### Conversion from 8-bit to 16-bit
- [func convert(to: vImage.PixelBuffer<vImage.Planar16F>)](vimage/pixelbuffer/convert(to:)-3wpdu.md)
  Converts the contents of the 8-bit planar pixel buffer to floating-point 16-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx2>)](vimage/pixelbuffer/convert(to:)-4v16.md)
  Converts the contents of the 8-bit-per-channel, 2-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Ux4>)](vimage/pixelbuffer/convert(to:)-9j6eu.md)
  Converts the contents of the 8-bit-per-channel, 4-channel interleaved pixel buffer to unsigned 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx4>)](vimage/pixelbuffer/convert(to:)-6ci2d.md)
  Converts the contents of the 8-bit-per-channel, 4-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.
### Conversion from 8-bit to 32-bit
- [func convert(to: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/convert(to:)-7src4.md)
  Converts the contents of the 8-bit planar pixel buffer to 32-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/convert(to:)-8hivu.md)
  Converts the contents of the 8-bit-per-channel, 3-channel interleaved pixel buffer to 32-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/convert(to:)-1e0nd.md)
  Converts the contents of the 8-bit-per-channel, 4-channel interleaved pixel buffer to 32-bit-per-channel format.
### Conversion from 16-bit to 8-bit
- [func convert(to: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/convert(to:)-449hx.md)
  Converts the contents of the floating-point 16-bit planar pixel buffer to 8-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x2>)](vimage/pixelbuffer/convert(to:)-1h96t.md)
  Converts the contents of the floating-point 16-bit-per-channel, 2-channel interleaved pixel buffer to 8-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/convert(to:)-k50a.md)
  Converts the contents of the unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer to 8-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/convert(to:)-9xnxc.md)
  Converts the contents of the floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer to 8-bit-per-channel format.
### Conversion between 16-bit formats
- [func convert(to: vImage.PixelBuffer<vImage.Planar16F>)](vimage/pixelbuffer/convert(to:)-1zk6k.md)
  Converts the contents of the unsigned 16-bit planar pixel buffer to floating-point 16-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Planar16U>)](vimage/pixelbuffer/convert(to:)-ip9z.md)
  Converts the contents of the floating-point 16-bit planar pixel buffer to unsigned 16-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Ux2>)](vimage/pixelbuffer/convert(to:)-7dx2c.md)
  Converts the contents of the floating-point 16-bit-per-channel, 2-channel interleaved pixel buffer to unsigned 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx4>)](vimage/pixelbuffer/convert(to:)-7tdb1.md)
  Converts the contents of the unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Ux4>)](vimage/pixelbuffer/convert(to:)-3lg9p.md)
  Converts the contents of the floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer to unsigned 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx2>)](vimage/pixelbuffer/convert(to:)-8u16v.md)
  Converts the contents of the unsigned 16-bit-per-channel, 2-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.
### Conversion from 16-bit to 32-bit
- [func convert(to: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/convert(to:)-4876v.md)
  Converts the contents of the floating-point 16-bit planar pixel buffer to 32-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx2>)](vimage/pixelbuffer/convert(to:)-1xpk2.md)
  Converts the contents of the floating-point 16-bit-per-channel, 2-channel interleaved pixel buffer to 32-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/convert(to:)-674t9.md)
  Converts the contents of the unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer to 32-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/convert(to:)-8ljhz.md)
  Converts the contents of the floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer to 32-bit-per-channel format.
### Conversion from 32-bit to 8-bit
- [func convert(to: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/convert(to:)-1ka0r.md)
  Converts the contents of the 32-bit planar pixel buffer to 8-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/convert(to:)-69qa2.md)
  Converts the contents of the 32-bit-per-channel, 3-channel interleaved pixel buffer to 8-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/convert(to:)-24xu0.md)
  Converts the contents of the 32-bit-per-channel, 4-channel interleaved pixel buffer to 8-bit-per-channel format.
### Conversion from 32-bit to 16-bit
- [func convert(to: vImage.PixelBuffer<vImage.Planar16F>)](vimage/pixelbuffer/convert(to:)-2bc8n.md)
  Converts the contents of the 32-bit planar pixel buffer to floating-point 16-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx2>)](vimage/pixelbuffer/convert(to:)-56zhe.md)
  Converts the contents of the 32-bit-per-channel, 2-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx4>)](vimage/pixelbuffer/convert(to:)-1132q.md)
  Converts the contents of the 32-bit-per-channel, 4-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Ux4>)](vimage/pixelbuffer/convert(to:)-2dbbo.md)
  Converts the contents of the 32-bit-per-channel, 4-channel interleaved pixel buffer to unsigned 16-bit-per-channel format.
### Conversion from four channels to three channels
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx3>, channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/convert(to:channelordering:)-1nll2.md)
  Converts the 32-bit-per-channel RGBA or ARGB pixel buffer to RGB.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x3>, channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/convert(to:channelordering:)-9h53.md)
  Converts the 8-bit-per-channel RGBA or ARGB pixel buffer to RGB.

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
- [Interleaving and deinterleaving pixel buffers](interleaving-and-deinterleaving-pixel-buffers.md)
  Convert pixel buffer data between interleaved and planar formats.
- [Cropping and working with regions of interest](cropping-and-working-with-regions-of-interest.md)
  Crop images and apply operations to regions of interest.
- [Applying channel operations](applying-channel-operations.md)
  Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/converting-pixel-buffers)*