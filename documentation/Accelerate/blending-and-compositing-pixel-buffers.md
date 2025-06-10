# Blending and compositing pixel buffers

**Framework**: Accelerate

Composite two pixel buffers to create a single image.

## Topics

### Alpha compositing
- [func alphaComposite(vImage.CompositeMode<Pixel_8>, topLayer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/alphacomposite(_:toplayer:destination:)-fybo.md)
  Performs alpha compositing of two 4-channel interleaved ARGB 8-bit pixel buffers using the specified composite mode.
- [func alphaComposite(vImage.CompositeMode<Pixel_F>, topLayer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/alphacomposite(_:toplayer:destination:)-w1zc.md)
  Performs alpha compositing of two 4-channel interleaved ARGB 32-bit pixel buffers using the specified composite mode.
- [vImage.CompositeMode](vimage/compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
### Alpha blending
- [func premultipliedAlphaBlend(vImage.BlendMode, topLayer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/premultipliedalphablend(_:toplayer:destination:).md)
  Performs alpha compositing of two 4-channel interleaved RGBA 8-bit pixel buffers using the specified blend mode to produce a premultiplied result.
- [vImage.BlendMode](vimage/blendmode.md)
  Constants that specify an alpha blending mode.
### Premultiply
- [func premultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/premultiply(alpha:)-11gly.md)
  Transforms an 8-bit planar pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/premultiply(alpha:)-76rr.md)
  Transforms a 32-bit planar pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/premultiply(channelordering:)-4xpq9.md)
  Transforms an 8-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/premultiply(channelordering:)-302ci.md)
  Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply()](vimage/pixelbuffer/premultiply.md)
  Transforms a floating-point 16-bit RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/premultiply(channelordering:)-fzwd.md)
  Transforms a floating-point 32-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
### Unpremultiply
- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-xnog.md)
  Transforms an 8-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-i0ri.md)
  Transforms a 32-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-1pkat.md)
  Transforms an 8-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-19l0s.md)
  Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply()](vimage/pixelbuffer/unpremultiply.md)
  Transforms a floating-point 16-bit RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-82uq3.md)
  Transforms a 32-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
### Linear interpolation
- [func linearInterpolate(bufferB: vImage.PixelBuffer<Format>, interpolationConstant: Float, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/linearinterpolate(bufferb:interpolationconstant:destination:).md)

## See Also

- [Applying geometric operations to pixel buffers](applying-geometric-operations-to-pixel-buffers.md)
  Reflect, shear, rotate, scale, and apply affine transforms to image data.
- [Applying color transforms to pixel buffers](applying-color-transforms-to-pixel-buffers.md)
  Adjust the colors of an image by applying gamma, polynomials, or multidimensional lookup.
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
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blending-and-compositing-pixel-buffers)*