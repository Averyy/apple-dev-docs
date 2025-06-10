# Cropping and working with regions of interest

**Framework**: Accelerate

Crop images and apply operations to regions of interest.

## Topics

### Cropping
- [func crop(at: CGPoint, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/crop(at:destination:).md)
  Crops the pixel buffer to a rectangle that’s defined by an origin and the destination buffer’s dimensions.
- [func cropped(to: CGRect) -> vImage.PixelBuffer<Format>](vimage/pixelbuffer/cropped(to:).md)
  Returns a new pixel buffer that contains a copy of the data specified as a subregion of an existing pixel buffer.
### Region of Interest
- [func withUnsafeRegionOfInterest<R>(CGRect, (vImage.PixelBuffer<Format>) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsaferegionofinterest(_:_:).md)
  Calls the given closure with a pixel buffer that references the image data within the specified region of interest.

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
- [Applying channel operations](applying-channel-operations.md)
  Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cropping-and-working-with-regions-of-interest)*