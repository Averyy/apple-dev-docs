# Availability Flags

**Framework**: Accelerate

Obtain the availability of particular vImage features.

## Topics

### Constants
- [var VIMAGE_AFFINETRANSFORM_DOUBLE_IS_AVAILABLE: Int32](vimage_affinetransform_double_is_available.md)
  Defined as `1` if double-precision affine transforms and related functions are supported on the current architecture and in the current SDK, else undefined. See [`vImage_AffineTransform_Double`](vimage_affinetransform_double.md) for more information.
- [var VIMAGE_CGAFFINETRANSFORM_IS_AVAILABLE: Int32](vimage_cgaffinetransform_is_available.md)
  Defined as `1` if Core Graphics affine transforms and related functions are supported on the current architecture and in the current SDK, else undefined. See [`vImage_CGAffineTransform`](vimage_cgaffinetransform.md) for more information.

## See Also

- [Error codes](1578972-error-codes.md)
  Error codes that vImage functions return when an operation fails.
- [Core Video Image Format Errors](1498271-core-video-image-format-errors.md)
- [Processing Flags](1578976-processing-flags.md)
  Set flags on vImage operations to specify processing options.
- [Dithering Methods](1533233-dithering-methods.md)
  Specify the dithering method some vImage conversion functions use.
- [Decode Arrays](decode-arrays.md)
  Specify the decode array constant to use with 16Q12-formatted data.
- [Buffer Types](buffer-types.md)
  Look up buffer type codes vImage conversions provide.
- [typealias vImageMatrixType](vimagematrixtype.md)
  An enumeration of RGB -> Y’CbCr conversion matrix types.
- [typealias vImage_WarpInterpolation](vimage_warpinterpolation.md)
  Constants for selecting the interpolation mode


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/availability-flags)*