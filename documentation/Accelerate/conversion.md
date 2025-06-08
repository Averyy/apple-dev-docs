# Conversion

**Framework**: Accelerate

Convert an image to a different format.

## Topics

### Converting any-to-any
- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
  Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.
- [Converting chroma-subsampled images](converting-chroma-subsampled-images.md)
  Create vImage buffers with the correct dimensions to convert to and from images with subsampled chroma information.
- [Functions that perform any-to-any conversion](functions-that-perform-any-to-any-conversion.md)
  Convert between Core Video or Core Graphics image data of arbitrary color spaces and bit depths.
### Type conversion
- [Functions that convert between integer planar buffers](functions-that-convert-between-integer-planar-buffers.md)
  Convert the bit depths of planar integer image data.
- [Functions that convert between integer interleaved buffers](functions-that-convert-between-integer-interleaved-buffers.md)
  Convert the bit depths of interleaved integer image data.
- [Functions that convert from integer planar buffers to noninteger planar buffers](functions-that-convert-from-integer-planar-buffers-to-noninteger-planar-buffers.md)
  Convert planar integer image data to fixed- and floating-point format.
- [Functions that convert from integer interleaved buffers to noninteger interleaved buffers](functions-that-convert-from-integer-interleaved-buffers-to-noninteger-interleaved-buffers.md)
  Convert interleaved integer image data to fixed- and floating-point format.
- [Functions that convert between noninteger planar buffers](functions-that-convert-between-noninteger-planar-buffers.md)
  Convert the bit depths and formats of planar fixed- and floating-point image data.
- [Functions that convert between noninteger interleaved buffers](functions-that-convert-between-noninteger-interleaved-buffers.md)
  Convert the bit depths and formats of interleaved fixed- and floating-point image data.
- [Functions that convert from noninteger planar buffers to integer planar buffers](functions-that-convert-from-noninteger-planar-buffers-to-integer-planar-buffers.md)
  Convert planar fixed- and floating-point image data to integer format.
- [Functions that convert from noninteger interleaved buffers to integer interleaved buffers](functions-that-convert-from-noninteger-interleaved-buffers-to-integer-interleaved-buffers.md)
  Convert interleaved fixed- and floating-point image data to integer format.
### Converting between interleaved and planar formats
- [Functions that interleave integer planar buffers](functions-that-interleave-integer-planar-buffers.md)
  Combine discrete integer planar buffers into an interleaved buffer.
- [Functions that interleave noninteger planar buffers](functions-that-interleave-noninteger-planar-buffers.md)
  Combine discrete fixed- and floating-point planar buffers into an interleaved buffer.
- [Functions that deinterleave integer interleaved buffers](functions-that-deinterleave-integer-interleaved-buffers.md)
  Separate integer interleaved buffers into discrete planar buffers.
- [Functions that deinterleave noninteger interleaved buffers](functions-that-deinterleave-noninteger-interleaved-buffers.md)
  Separate fixed- and floating-point interleaved buffers into discrete planar buffers.
### Adding and removing alpha channels
- [Functions that add an alpha channel to three-channel buffers](functions-that-add-an-alpha-channel-to-three-channel-buffers.md)
  Add a constant alpha value or planar alpha buffer to an RGB image.
- [Functions that remove an alpha channel from four-channel buffers](functions-that-remove-an-alpha-channel-from-four-channel-buffers.md)
  Remove the alpha channel from an RGBA or ARGB buffer.
### Converting between YCbCr and RGB color spaces
- [Functions that convert from YCbCr to RGB](functions-that-convert-from-ycbcr-to-rgb.md)
  Convert image data represented by luma, blue-difference, and red-difference channels to red, green, and blue channels.
- [Functions that convert from RGB to YCbCr](functions-that-convert-from-rgb-to-ycbcr.md)
  Convert image data represented by red, green, and blue channels to luma, blue-difference, and red-difference channels.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/conversion)*