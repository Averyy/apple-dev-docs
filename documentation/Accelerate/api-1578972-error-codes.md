# Error codes

**Framework**: Accelerate

Error codes that vImage functions return when an operation fails.

## Topics

### Constants
- [vImage.Error](vimage/error.md)
  An error that occurs during a vImage operation.
- [var kvImageNoError: Int](kvimagenoerror.md)
  The vImage function completed without error.
- [var kvImageRoiLargerThanInputBuffer: Int](kvimageroilargerthaninputbuffer.md)
  The region of interest, as specified by the `srcOffsetToROI_X` and `srcOffsetToROI_Y` parameters and the height and width of the destination buffer, extends beyond the bottom edge or right edge of the source buffer.
- [var kvImageInvalidKernelSize: Int](kvimageinvalidkernelsize.md)
  Either the kernel height, the kernel width, or both, are even.
- [var kvImageInvalidEdgeStyle: Int](kvimageinvalidedgestyle.md)
  The edge style specified is invalid.
- [var kvImageInvalidOffset_X: Int](kvimageinvalidoffset_x.md)
  The `srcOffsetToROI_X` parameter that specifies the left edge of the region of interest is greater than the width of the source image.
- [var kvImageInvalidOffset_Y: Int](kvimageinvalidoffset_y.md)
  The `srcOffsetToROI_Y` parameter that specifies the top edge of the region of interest is greater than the height of the source image.
- [var kvImageMemoryAllocationError: Int](kvimagememoryallocationerror.md)
  An attempt to allocate memory failed.
- [var kvImageNullPointerArgument: Int](kvimagenullpointerargument.md)
  A pointer parameter is `NULL` and it must not be.
- [var kvImageInvalidParameter: Int](kvimageinvalidparameter.md)
  Invalid parameter.
- [var kvImageBufferSizeMismatch: Int](kvimagebuffersizemismatch.md)
  The function requires the source and destination buffers to have the same height and the same width, but they do not.
- [var kvImageUnknownFlagsBit: Int](kvimageunknownflagsbit.md)
  The flag is not recognized.
- [var kvImageColorSyncIsAbsent: Int](kvimagecolorsyncisabsent.md)
- [var kvImageCoreVideoIsAbsent: Int](kvimagecorevideoisabsent.md)
- [var kvImageInternalError: Int](kvimageinternalerror.md)
  A serious error occured inside vImage, which prevented vImage from continuing.
- [var kvImageInvalidCVImageFormat: Int](kvimageinvalidcvimageformat.md)
- [var kvImageInvalidImageFormat: Int](kvimageinvalidimageformat.md)
- [var kvImageInvalidImageObject: Int](kvimageinvalidimageobject.md)
- [var kvImageInvalidRowBytes: Int](kvimageinvalidrowbytes.md)
- [var kvImageOutOfPlaceOperationRequired: Int](kvimageoutofplaceoperationrequired.md)
- [var kvImageUnsupportedConversion: Int](kvimageunsupportedconversion.md)
  Some lower level conversion APIs only support conversion among a sparse matrix of image formats.
### Core Video Image Format Errors
- [var kvImageCVImageFormat_NoError: Int](kvimagecvimageformat_noerror.md)
  An error code that indicates the conversion completed without error.
- [var kvImageCVImageFormat_ColorSpace: Int](kvimagecvimageformat_colorspace.md)
  An error code that indicates the image’s color space is missing.
- [var kvImageCVImageFormat_ChromaSiting: Int](kvimagecvimageformat_chromasiting.md)
  An error code that indicates the chroma siting information is absent.
- [var kvImageCVImageFormat_AlphaIsOneHint: Int](kvimagecvimageformat_alphaisonehint.md)
  A hint that indicates the alpha channel is opaque.
- [var kvImageCVImageFormat_ConversionMatrix: Int](kvimagecvimageformat_conversionmatrix.md)
  An error code that indicates the required conversion matrix is absent.
- [var kvImageCVImageFormat_VideoChannelDescription: Int](kvimagecvimageformat_videochanneldescription.md)
  An error code that indicates the range and clipping information is missing.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/1578972-error-codes)*