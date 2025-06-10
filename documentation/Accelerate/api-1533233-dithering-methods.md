# Dithering Methods

**Framework**: Accelerate

Specify the dithering method some vImage conversion functions use.

## Topics

### Constants
- [var kvImageConvert_DitherNone: UInt32](kvimageconvert_dithernone.md)
  A constant that indicates the conversion will not apply dithering.
- [var kvImageConvert_DitherOrdered: UInt32](kvimageconvert_ditherordered.md)
  A constant that indicates the conversion will add randomized, pre-computed blue noise to the image.
- [var kvImageConvert_DitherOrderedReproducible: UInt32](kvimageconvert_ditherorderedreproducible.md)
  A constant that indicates the conversion will add reproducible, pre-computed blue noise to the image.
- [var kvImageConvert_DitherFloydSteinberg: UInt32](kvimageconvert_ditherfloydsteinberg.md)
  A constant that indicates the conversion will add Floyd-Steinberg dithering to the image.
- [var kvImageConvert_DitherAtkinson: UInt32](kvimageconvert_ditheratkinson.md)
  A constant that indicates the conversion will add Atkinson dithering to the image.
- [var kvImageConvert_OrderedGaussianBlue: UInt32](kvimageconvert_orderedgaussianblue.md)
  A constant that indicates the conversion will distribute the noise according to a Gaussian distribution.
- [var kvImageConvert_OrderedUniformBlue: UInt32](kvimageconvert_ordereduniformblue.md)
  A constant that indicates the conversion will distribute the noise uniformly.
- [var kvImageConvert_OrderedNoiseShapeMask: UInt32](kvimageconvert_orderednoiseshapemask.md)

## See Also

- [Error codes](1578972-error-codes.md)
  Error codes that vImage functions return when an operation fails.
- [Core Video Image Format Errors](1498271-core-video-image-format-errors.md)
- [Processing Flags](1578976-processing-flags.md)
  Set flags on vImage operations to specify processing options.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/1533233-dithering-methods)*