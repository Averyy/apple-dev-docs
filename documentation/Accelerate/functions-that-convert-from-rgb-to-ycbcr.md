# Functions that convert from RGB to YCbCr

**Framework**: Accelerate

Convert image data represented by red, green, and blue channels to luma, blue-difference, and red-difference channels.

## Topics

### Converting to 4:2:0
- [func vImageConvert_ARGB8888To420Yp8_CbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to420yp8_cbcr8(_:_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to a planar Yp buffer and a 2-channel CbCr buffer.
- [func vImageConvert_ARGB8888To420Yp8_Cb8_Cr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to420yp8_cb8_cr8(_:_:_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to planar Yp, Cb, and Cr buffers.
### Converting to 4:2:2
- [func vImageConvert_ARGB8888To422CbYpCrYp8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to422cbypcryp8(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:2:2 CbCrYp buffer.
- [func vImageConvert_ARGB8888To422YpCbYpCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to422ypcbypcr8(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:2:2 YpCbYpCr buffer.
- [func vImageConvert_ARGB8888To422CbYpCrYp8_AA8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to422cbypcryp8_aa8(_:_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:2:2 CbYpCrYp buffer and an 8-bit alpha buffer.
- [func vImageConvert_ARGB8888To422CbYpCrYp16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to422cbypcryp16(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to a 16-bit-per-channel 4:2:2 CbYpCrYp buffer.
- [func vImageConvert_ARGB8888To422CrYpCbYpCbYpCbYpCrYpCrYp10(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to422crypcbypcbypcbypcrypcryp10(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to a 10-bit-per-channel 4:2:2 CrYpCbYpCbYpCbYpCrYpCrYp buffer.
- [func vImageConvert_ARGB16UTo422CbYpCrYp16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16uto422cbypcryp16(_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel ARGB buffer to a 16-bit-per-channel 4:2:2 CbYpCrYp buffer.
- [func vImageConvert_ARGB16Q12To422CrYpCbYpCbYpCbYpCrYpCrYp10(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16q12to422crypcbypcbypcbypcrypcryp10(_:_:_:_:_:).md)
  Converts a fixed-point 16-bit-per-channel, 4-channel ARGB buffer to a 10-bit-per-channel 4:2:2 CrYpCbYpCbYpCbYpCrYpCrYp buffer.
### Converting to 4:4:4
- [func vImageConvert_ARGB8888To444CrYpCb8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444crypcb8(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:4:4 CrYpCb buffer.
- [func vImageConvert_ARGB8888To444AYpCbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444aypcbcr8(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:4:4 YpCbCr buffer.
- [func vImageConvert_ARGB8888To444CbYpCrA8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444cbypcra8(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:4:4 CrYpCbA buffer.
- [func vImageConvert_ARGB8888To444CrYpCb10(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444crypcb10(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 10-bit-per-channel 4:4:4 CrYpCb buffer.
- [func vImageConvert_ARGB8888To444AYpCbCr16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444aypcbcr16(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 16-bit-per-channel 4:4:4 YpCbCr buffer.
- [func vImageConvert_ARGB16UTo444AYpCbCr16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16uto444aypcbcr16(_:_:_:_:_:).md)
  Converts an  unsigned 16-bit-per-channel, 4-channel ARGB buffer to an 16-bit-per-channel 4:4:4 AYpCbCr buffer.
- [func vImageConvert_ARGB16Q12To444CrYpCb10(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16q12to444crypcb10(_:_:_:_:_:).md)
  Converts a fixed-point 16-bit-per-channel, 4-channel ARGB buffer to an 10-bit-per-channel 4:4:4 CrYpCb buffer.
### Generating conversion information
- [func vImageConvert_ARGBToYpCbCr_GenerateConversion(UnsafePointer<vImage_ARGBToYpCbCrMatrix>, UnsafePointer<vImage_YpCbCrPixelRange>, UnsafeMutablePointer<vImage_ARGBToYpCbCr>, vImageARGBType, vImageYpCbCrType, vImage_Flags) -> vImage_Error](vimageconvert_argbtoypcbcr_generateconversion(_:_:_:_:_:_:).md)
  Generates the information that describes the conversion from ARGB to YpCbCr.
- [struct vImageYpCbCrType](vimageypcbcrtype.md)
  Constants that describe the encoding of a YpCbCr image for conversions between RGB and YpCbCr.
- [struct vImageARGBType](vimageargbtype.md)
  Constants that describe the encoding of an ARGB image for conversions between RGB and YpCbCr.
- [struct vImage_ARGBToYpCbCrMatrix](vimage_argbtoypcbcrmatrix.md)
  The 3 x 3 matrix that the vImage library uses to convert from RGB to YpCbCr.
- [struct vImage_ARGBToYpCbCr](vimage_argbtoypcbcr.md)
  The information that describes the conversion from ARGB to YpCbCr.
- [struct vImage_YpCbCrPixelRange](vimage_ypcbcrpixelrange.md)
  The description of range and clamping information for YpCbCr pixel formats.

## See Also

- [Functions that convert from YCbCr to RGB](functions-that-convert-from-ycbcr-to-rgb.md)
  Convert image data represented by luma, blue-difference, and red-difference channels to red, green, and blue channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-convert-from-rgb-to-ycbcr)*