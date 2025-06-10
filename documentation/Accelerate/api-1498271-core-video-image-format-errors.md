# Core Video Image Format Errors

**Framework**: Accelerate

## Topics

### Type Aliases
- [typealias vImageCVImageFormatError](vimagecvimageformaterror.md)
  Additional error codes for functions that use the vImageCVImageFormatRef
### Constants
- [var kvImageCVImageFormat_NoError: Int](kvimagecvimageformat_noerror.md)
  An error code that indicates the conversion completed without error.
- [var kvImageCVImageFormat_ConversionMatrix: Int](kvimagecvimageformat_conversionmatrix.md)
  An error code that indicates the required conversion matrix is absent.
- [var kvImageCVImageFormat_ChromaSiting: Int](kvimagecvimageformat_chromasiting.md)
  An error code that indicates the chroma siting information is absent.
- [var kvImageCVImageFormat_ColorSpace: Int](kvimagecvimageformat_colorspace.md)
  An error code that indicates the image’s color space is missing.
- [var kvImageCVImageFormat_VideoChannelDescription: Int](kvimagecvimageformat_videochanneldescription.md)
  An error code that indicates the range and clipping information is missing.
- [var kvImageCVImageFormat_AlphaIsOneHint: Int](kvimagecvimageformat_alphaisonehint.md)
  A hint that indicates the alpha channel is opaque.

## See Also

- [Error codes](1578972-error-codes.md)
  Error codes that vImage functions return when an operation fails.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/1498271-core-video-image-format-errors)*