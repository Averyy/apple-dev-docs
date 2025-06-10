# Applying geometric operations to pixel buffers

**Framework**: Accelerate

Reflect, shear, rotate, scale, and apply affine transforms to image data.

## Topics

### Reflecting images
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-9ezqm.md)
  Reflects an 8-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-529j0.md)
  Reflects a floating-point 16-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-4i4vi.md)
  Reflects a 32-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-6syq1.md)
  Reflects a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-7o9tt.md)
  Reflects an 8-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-fg4a.md)
  Reflects an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-97wi9.md)
  Reflects a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-7b1md.md)
  Reflects a 32-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [vImage.ReflectionAxis](vimage/reflectionaxis.md)
  The axis to reflect an image.
### Rotating images
- [func rotate(vImage.Rotation, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-7patt.md)
  Rotates an 8-bit planar pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:usefloat16accumulator:destination:)-9harr.md)
  Rotates a floating-point 16-bit planar pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-7tzsn.md)
  Rotates a 32-bit planar pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:usefloat16accumulator:destination:)-61l7b.md)
  Rotates a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-2li9v.md)
  Rotates an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-692ke.md)
  Rotates an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:usefloat16accumulator:destination:)-8glur.md)
  Rotates a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-9bnb6.md)
  Rotates a 32-bit-per-channel, four-channel interleaved pixel buffer.
- [vImage.Rotation](vimage/rotation.md)
  The angle to rotate an image.
### Scaling images
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-5euvc.md)
  Scales an 8-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-9si6m.md)
  Scales an unsigned 16-bit planar pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(usefloat16accumulator:destination:)-5lt9n.md)
  Scales a floating-point 16-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-6xwro.md)
  Scales a 32-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-6gy9p.md)
  Scales an 8-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-4p5r6.md)
  Scales an unsigned 16-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(usefloat16accumulator:destination:)-thg7.md)
  Scales a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-y1zi.md)
  Scales an 8-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-5tpok.md)
  Scales an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(usefloat16accumulator:destination:)-st2u.md)
  Scales a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-2hqm3.md)
  Scales a 32-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
### Shearing images
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-2gf4y.md)
  Performs a horizontal or vertical shear operation on an 8-bit planar pixel buffer.
- [func shear(direction: vImage.ShearDirection, translate: Float, slope: Float, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-5busu.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:usefloat16accumulator:destination:)-26sh4.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-85o1n.md)
  Performs a horizontal or vertical shear operation on a 32-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16U16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-57dzf.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear(direction: vImage.ShearDirection, translate: Float, slope: Float, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_88?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-7fou8.md)
  Performs a horizontal or vertical shear operation on an 8-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:usefloat16accumulator:destination:)-7nh4n.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-95446.md)
  Performs a horizontal or vertical shear operation on an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-2ezuh.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:usefloat16accumulator:destination:)-7kddt.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-7r29q.md)
  Performs a horizontal or vertical shear operation on a 32-bit-per-channel, four-channel interleaved pixel buffer.
- [vImage.ShearDirection](vimage/sheardirection.md)
  The shear direction.
### Applying affine transformations to images
- [func transform(CGAffineTransform, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-4wy4q.md)
  Applies a Core Graphics affine transformation to an 8-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:usefloat16accumulator:destination:)-1470p.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-1s38.md)
  Applies a Core Graphics affine transformation to a floating-point 32-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:usefloat16accumulator:destination:)-4w4jr.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-5kxj6.md)
  Applies a Core Graphics affine transformation to an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-nl6g.md)
  Applies a Core Graphics affine transformation to an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:usefloat16accumulator:destination:)-1lvaa.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-9ggt.md)
  Applies a Core Graphics affine transformation to a floating-point 32-bit-per-channel, four-channel interleaved pixel buffer.
### Applying projective transformations to images
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_8, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:interpolation:backgroundcolor:destination:)-94t75.md)
  Applies a perspective warp to an 8-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_8888, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:interpolation:backgroundcolor:destination:)-902c9.md)
  Applies a perspective warp to an interleaved 4-channel, 8-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_16U, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:interpolation:backgroundcolor:destination:)-9pv8u.md)
  Applies a perspective warp to an unsigned-integer 16-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_ARGB_16U, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:interpolation:backgroundcolor:destination:)-4wvdj.md)
  Applies a perspective warp to an interleaved 4-channel, unsigned 16-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_16F, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:interpolation:backgroundcolor:destination:)-79mov.md)
  Applies a perspective warp to a floating-point 16-bit planar image.
- [func transform(vImage_PerpsectiveTransform, interpolation: vImage_PerpsectiveTransform.Interpolation, backgroundColor: Pixel_ARGB_16F, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:interpolation:backgroundcolor:destination:)-7qnl8.md)
  Applies a perspective warp to an interleaved 4-channel, floating-point 16-bit planar image.

## See Also

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
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-geometric-operations-to-pixel-buffers)*