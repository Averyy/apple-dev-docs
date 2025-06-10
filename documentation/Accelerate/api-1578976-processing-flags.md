# Processing Flags

**Framework**: Accelerate

Set flags on vImage operations to specify processing options.

#### Overview

You can pass multiple flags to a function by adding the flag values together. For example, to leave alpha unchanged and turn off tiling, you can pass:

```objc
kvImageLeaveAlphaUnchanged + kvImageDoNotTile
```

Three of the flags are mutually exclusive: `kvImageCopyInPlace`, `kvImageBackgroundColorFill`, and `kvImageEdgeExtend`. Never pass more than one of these flag values in the same flag parameter.

When passing flags to a function, do not set values for flags that are not used by the function. If the function requires you to set certain flag values, do so. For example, for the convolution function, you must set exactly one of `kvImageCopyInPlace`, `kvImageBackgroundColorFill`, and `kvImageEdgeExtend`.  Otherwise the function may return an error. If you don’t want to set flag values, pass `kvImageNoFlags`.

## Topics

### Constants
- [vImage.Options](vimage/options.md)
  Set flags on vImage operations to specify processing options.
- [var kvImageNoFlags: Int](kvimagenoflags.md)
  A flag that sets the behavior to the default.
- [var kvImageLeaveAlphaUnchanged: Int](kvimageleavealphaunchanged.md)
  A flag that restricts the operation to red, green, and blue channels only.
- [var kvImageDoNotTile: Int](kvimagedonottile.md)
  A flag that disables vImage internal tiling routines.
- [var kvImageHighQualityResampling: Int](kvimagehighqualityresampling.md)
  A flag that uses a higher-quality, slower resampling filter for geometry operations.
- [var kvImageGetTempBufferSize: Int](kvimagegettempbuffersize.md)
  A flag that returns the minimum temporary buffer size for the operation, given the parameters provided.
- [var kvImagePrintDiagnosticsToConsole: Int](kvimageprintdiagnosticstoconsole.md)
  A flag that prints a debug message if the operation fails.
- [var kvImageNoAllocate: Int](kvimagenoallocate.md)
  A flag that prevents vImage from allocating additional storage.
- [var kvImageHDRContent: Int](kvimagehdrcontent.md)
  A flag that uses HDR-aware methods.
- [var kvImageDoNotClamp: Int](kvimagedonotclamp.md)
  A flag that disables clamping in some conversions to floating-point formats.
- [var kvImageUseFP16Accumulator: Int](kvimageusefp16accumulator.md)
  A flag that specifies vImage uses faster but lower-precision internal arithmetic for floating-point 16-bit operations.
### Edging Modes
- [var kvImageCopyInPlace: Int](kvimagecopyinplace.md)
  A flag that copies the value of the edge pixel in the source to the destination.
- [var kvImageBackgroundColorFill: Int](kvimagebackgroundcolorfill.md)
  A flag that uses the background color for missing pixels.
- [var kvImageEdgeExtend: Int](kvimageedgeextend.md)
  A flag that extends the edges of the image infinitely.
- [var kvImageTruncateKernel: Int](kvimagetruncatekernel.md)
  A flag that uses only the part of the kernel that overlaps the image.

## See Also

- [Error codes](1578972-error-codes.md)
  Error codes that vImage functions return when an operation fails.
- [Core Video Image Format Errors](1498271-core-video-image-format-errors.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/1578976-processing-flags)*