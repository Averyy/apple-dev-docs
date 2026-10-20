# Applying geometric operations to pixel buffers

**Framework**: Accelerate  
**Role**: API Collection

Reflect, shear, rotate, scale, and apply affine transforms to image data.

## Topics

### Reflecting images
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/reflect%28over,destination%29-9ezqm.md)
  Reflects an 8-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/reflect%28over,destination%29-529j0.md)
  Reflects a floating-point 16-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/reflect%28over,destination%29-4i4vi.md)
  Reflects a 32-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/reflect%28over,destination%29-6syq1.md)
  Reflects a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/reflect%28over,destination%29-7o9tt.md)
  Reflects an 8-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/reflect%28over,destination%29-fg4a.md)
  Reflects an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/reflect%28over,destination%29-97wi9.md)
  Reflects a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/reflect%28over,destination%29-7b1md.md)
  Reflects a 32-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [vImage.ReflectionAxis](./vimage/reflectionaxis.md)
  The axis to reflect an image.
### Rotating images
- [func rotate(vImage.Rotation, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/rotate%28_,backgroundcolor,destination%29-7patt.md)
  Rotates an 8-bit planar pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/rotate%28_,backgroundcolor,usefloat16accumulator,destination%29-9harr.md)
  Rotates a floating-point 16-bit planar pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/rotate%28_,backgroundcolor,destination%29-7tzsn.md)
  Rotates a 32-bit planar pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/rotate%28_,backgroundcolor,usefloat16accumulator,destination%29-61l7b.md)
  Rotates a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/rotate%28_,backgroundcolor,destination%29-2li9v.md)
  Rotates an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/rotate%28_,backgroundcolor,destination%29-692ke.md)
  Rotates an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/rotate%28_,backgroundcolor,usefloat16accumulator,destination%29-8glur.md)
  Rotates a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/rotate%28_,backgroundcolor,destination%29-9bnb6.md)
  Rotates a 32-bit-per-channel, four-channel interleaved pixel buffer.
- [vImage.Rotation](./vimage/rotation.md)
  The angle to rotate an image.
### Scaling images
- [func scale(destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28destination%29-5euvc.md)
  Scales an 8-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28destination%29-9si6m.md)
  Scales an unsigned 16-bit planar pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28usefloat16accumulator,destination%29-5lt9n.md)
  Scales a floating-point 16-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28destination%29-6xwro.md)
  Scales a 32-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28destination%29-6gy9p.md)
  Scales an 8-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28destination%29-4p5r6.md)
  Scales an unsigned 16-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28usefloat16accumulator,destination%29-thg7.md)
  Scales a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28destination%29-y1zi.md)
  Scales an 8-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28destination%29-5tpok.md)
  Scales an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28usefloat16accumulator,destination%29-st2u.md)
  Scales a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/scale%28destination%29-2hqm3.md)
  Scales a 32-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
### Shearing images
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-2gf4y.md)
  Performs a horizontal or vertical shear operation on an 8-bit planar pixel buffer.
- [func shear(direction: vImage.ShearDirection, translate: Float, slope: Float, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16U?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-5busu.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,usefloat16accumulator,destination%29-26sh4.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-85o1n.md)
  Performs a horizontal or vertical shear operation on a 32-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16U16U?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-57dzf.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear(direction: vImage.ShearDirection, translate: Float, slope: Float, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_88?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-7fou8.md)
  Performs a horizontal or vertical shear operation on an 8-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,usefloat16accumulator,destination%29-7nh4n.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-95446.md)
  Performs a horizontal or vertical shear operation on an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-2ezuh.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,usefloat16accumulator,destination%29-7kddt.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-7r29q.md)
  Performs a horizontal or vertical shear operation on a 32-bit-per-channel, four-channel interleaved pixel buffer.
- [vImage.ShearDirection](./vimage/sheardirection.md)
  The shear direction.
### Applying affine transformations to images
- [func transform(CGAffineTransform, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,backgroundcolor,destination%29-4wy4q.md)
  Applies a Core Graphics affine transformation to an 8-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,backgroundcolor,usefloat16accumulator,destination%29-1470p.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,backgroundcolor,destination%29-1s38.md)
  Applies a Core Graphics affine transformation to a floating-point 32-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,backgroundcolor,usefloat16accumulator,destination%29-4w4jr.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,backgroundcolor,destination%29-5kxj6.md)
  Applies a Core Graphics affine transformation to an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,backgroundcolor,destination%29-nl6g.md)
  Applies a Core Graphics affine transformation to an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,backgroundcolor,usefloat16accumulator,destination%29-1lvaa.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,backgroundcolor,destination%29-9ggt.md)
  Applies a Core Graphics affine transformation to a floating-point 32-bit-per-channel, four-channel interleaved pixel buffer.
### Applying projective transformations to images
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_8, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,interpolation,backgroundcolor,destination%29-94t75.md)
  Applies a perspective warp to an 8-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_8888, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,interpolation,backgroundcolor,destination%29-902c9.md)
  Applies a perspective warp to an interleaved 4-channel, 8-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_16U, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,interpolation,backgroundcolor,destination%29-9pv8u.md)
  Applies a perspective warp to an unsigned-integer 16-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_ARGB_16U, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,interpolation,backgroundcolor,destination%29-4wvdj.md)
  Applies a perspective warp to an interleaved 4-channel, unsigned 16-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_16F, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,interpolation,backgroundcolor,destination%29-79mov.md)
  Applies a perspective warp to a floating-point 16-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_ARGB_16F, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/transform%28_,interpolation,backgroundcolor,destination%29-7qnl8.md)
  Applies a perspective warp to an interleaved 4-channel, floating-point 16-bit planar image.

## See Also

### Pixel buffer operations
- [Applying color transforms to pixel buffers](./applying-color-transforms-to-pixel-buffers.md)
  Adjust the colors of an image by applying gamma, polynomials, or multidimensional lookup.
- [Blending and compositing pixel buffers](./blending-and-compositing-pixel-buffers.md)
  Composite two pixel buffers to create a single image.
- [Convolving and applying morphology](./convolving-and-applying-morphology.md)
  Apply convolution, dilation, or erosion to a pixel buffer.
- [Thresholding and clipping pixel buffer values](./thresholding-and-clipping-pixel-buffer-values.md)
  Limit the values in a pixel buffer to a threshold or a range.
- [Calculating and transforming histograms](./calculating-and-transforming-histograms.md)
  Enhance and adjust the contrast of an image with histogram equalization, contrast stretching, and specification.
- [Converting pixel buffers](./converting-pixel-buffers.md)
  Convert pixel buffer data between different bit-depths.
- [Interleaving and deinterleaving pixel buffers](./interleaving-and-deinterleaving-pixel-buffers.md)
  Convert pixel buffer data between interleaved and planar formats.
- [Cropping and working with regions of interest](./cropping-and-working-with-regions-of-interest.md)
  Crop images and apply operations to regions of interest.
- [Applying channel operations](./applying-channel-operations.md)
  Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.
- [Applying arithmetic operations](./applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-geometric-operations-to-pixel-buffers)*