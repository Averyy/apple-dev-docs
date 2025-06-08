# Data Types and Constants

**Framework**: Accelerate

Look up type aliases, data types, and constants the vImage library uses.

#### Overview

The vImage library defines data types for planar and interleaved pixel types, a resampling callback filter, and an affine transform. vImage provides constants that specify errors and flags that you pass to a function to specify a variety of processing options.

## Topics

### Pixel Formats
- [typealias Pixel_8](pixel_8.md)
  A type for a planar, 8-bits-per-channel, unsigned pixel.
- [typealias Pixel_88](pixel_88.md)
  A type for a two-channel, 8-bits-per-channel, unsigned pixel.
- [typealias Pixel_8888](pixel_8888.md)
  A type for a four-channel, 8-bits-per-channel, unsigned pixel.
- [typealias Pixel_F](pixel_f.md)
  A type for a planar, 32-bits-per-channel, floating-point pixel.
- [typealias Pixel_FFFF](pixel_ffff.md)
  A type for a four-channel, 32-bits-per-channel, floating-point pixel.
- [typealias Pixel_32U](pixel_32u.md)
  A type you use for the XRGB2101010 format.
- [typealias Pixel_16U](pixel_16u.md)
  A type for a planar, 16-bits-per-channel, unsigned pixel.
- [typealias Pixel_ARGB_16U](pixel_argb_16u.md)
  A type for a four-channel, 16-bits-per-channel, unsigned pixel.
- [typealias Pixel_16U16U](pixel_16u16u.md)
  A type for a two-channel, 16-bits-per-channel, unsigned pixel.
- [typealias Pixel_16Q12](pixel_16q12.md)
  A type for a signed 16-bit, fixed-point number with 12 bits of fractional precision.
- [typealias Pixel_16S](pixel_16s.md)
  A type for a planar, 16-bits-per-channel, signed pixel.
- [typealias Pixel_ARGB_16S](pixel_argb_16s.md)
  A type for a four-channel, 16-bits-per-channel, signed pixel.
- [typealias Pixel_16F](pixel_16f.md)
- [typealias Pixel_16F16F](pixel_16f16f.md)
- [typealias Pixel_16S16S](pixel_16s16s.md)
- [typealias Pixel_ARGB_16F](pixel_argb_16f.md)
- [typealias Pixel_FF](pixel_ff.md)
### Data Types
- [struct vImage_Buffer](vimage_buffer.md)
  An image buffer that stores an image’s pixel data, dimensions, and row stride.
- [typealias vImagePixelCount](vimagepixelcount.md)
  A type for the number of pixels.
- [struct vImage_AffineTransform](vimage_affinetransform.md)
  A structure for values that represent an affine transformation.
- [struct vImage_AffineTransform_Double](vimage_affinetransform_double.md)
  A structure for values that represent a double-precision affine transformation.
- [typealias vImage_CGAffineTransform](vimage_cgaffinetransform.md)
  A structure for values that represent a Core Graphics–compatible affine transformation.
- [typealias vImage_Error](vimage_error.md)
  A type for image errors.
- [typealias vImage_Flags](vimage_flags.md)
  A type for processing options.
- [typealias GammaFunction](gammafunction.md)
  A type for a gamma function.
- [typealias ResamplingFilter](resamplingfilter.md)
  A pointer to a resampling filter callback function.
### Constants
- [Error codes](1578972-error-codes.md)
  Error codes that vImage functions return when an operation fails.
- [Core Video Image Format Errors](1498271-core-video-image-format-errors.md)
- [Processing Flags](1578976-processing-flags.md)
  Set flags on vImage operations to specify processing options.
- [Dithering Methods](1533233-dithering-methods.md)
  Specify the dithering method some vImage conversion functions use.
- [Availability Flags](availability-flags.md)
  Obtain the availability of particular vImage features.
- [Decode Arrays](decode-arrays.md)
  Specify the decode array constant to use with 16Q12-formatted data.
- [Buffer Types](buffer-types.md)
  Look up buffer type codes vImage conversions provide.
- [typealias vImageMatrixType](vimagematrixtype.md)
  An enumeration of RGB -> Y’CbCr conversion matrix types.
- [typealias vImage_WarpInterpolation](vimage_warpinterpolation.md)
  Constants for selecting the interpolation mode

## See Also

- [vImage Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/vImage/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001001)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/data-types-and-constants)*