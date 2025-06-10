# vImage Buffer Type Codes

**Framework**: Accelerate

Constants that specify the contents of vImage buffers.

## Topics

### Type
- [typealias vImageBufferTypeCode](vimagebuffertypecode.md)
  Type codes, such as chrominance or luminance, for the contents of a vImage buffer.
### Constants
- [var kvImageBufferTypeCode_Alpha: Int](kvimagebuffertypecode_alpha.md)
  The buffer contains the alpha channel.
- [var kvImageBufferTypeCode_CGFormat: Int](kvimagebuffertypecode_cgformat.md)
  The buffer contains data describable as a vImage Core Graphics image format as a single buffer.
- [var kvImageBufferTypeCode_CMYK_Black: Int](kvimagebuffertypecode_cmyk_black.md)
  If the image has a CMYK color model, the buffer contains the black channel.
- [var kvImageBufferTypeCode_CMYK_Cyan: Int](kvimagebuffertypecode_cmyk_cyan.md)
  If the image has a CMYK color model, the buffer contains the cyan channel.
- [var kvImageBufferTypeCode_CMYK_Magenta: Int](kvimagebuffertypecode_cmyk_magenta.md)
  If the image has a CMYK color model, the buffer contains the magenta channel.
- [var kvImageBufferTypeCode_CMYK_Yellow: Int](kvimagebuffertypecode_cmyk_yellow.md)
  If the image has a CMYK color model, the buffer contains the yellow channel.
- [var kvImageBufferTypeCode_CVPixelBuffer_YCbCr: Int](kvimagebuffertypecode_cvpixelbuffer_ycbcr.md)
  The buffer contains luminance and both chroma channels interleaved according to the [`vImageConstCVImageFormat`](vimageconstcvimageformat.md) image type.
- [var kvImageBufferTypeCode_Cb: Int](kvimagebuffertypecode_cb.md)
  The buffer contains the blue chrominance channel.
- [var kvImageBufferTypeCode_Chroma: Int](kvimagebuffertypecode_chroma.md)
  The buffer contains both chrominance channels, interleaved.
- [var kvImageBufferTypeCode_Chunky: Int](kvimagebuffertypecode_chunky.md)
  The buffer contains chunky data not describable as a vImage Core Graphics image format.
- [var kvImageBufferTypeCode_ColorSpaceChannel1: Int](kvimagebuffertypecode_colorspacechannel1.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel10: Int](kvimagebuffertypecode_colorspacechannel10.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel11: Int](kvimagebuffertypecode_colorspacechannel11.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel12: Int](kvimagebuffertypecode_colorspacechannel12.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel13: Int](kvimagebuffertypecode_colorspacechannel13.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel14: Int](kvimagebuffertypecode_colorspacechannel14.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel15: Int](kvimagebuffertypecode_colorspacechannel15.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel16: Int](kvimagebuffertypecode_colorspacechannel16.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel2: Int](kvimagebuffertypecode_colorspacechannel2.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel3: Int](kvimagebuffertypecode_colorspacechannel3.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel4: Int](kvimagebuffertypecode_colorspacechannel4.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel5: Int](kvimagebuffertypecode_colorspacechannel5.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel6: Int](kvimagebuffertypecode_colorspacechannel6.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel7: Int](kvimagebuffertypecode_colorspacechannel7.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel8: Int](kvimagebuffertypecode_colorspacechannel8.md)
- [var kvImageBufferTypeCode_ColorSpaceChannel9: Int](kvimagebuffertypecode_colorspacechannel9.md)
- [var kvImageBufferTypeCode_Cr: Int](kvimagebuffertypecode_cr.md)
  The buffer contains the red chrominance channel.
- [var kvImageBufferTypeCode_EndOfList: Int](kvimagebuffertypecode_endoflist.md)
  End of list marker.
- [var kvImageBufferTypeCode_Indexed: Int](kvimagebuffertypecode_indexed.md)
  The buffer contains data in an indexed colorspace.
- [var kvImageBufferTypeCode_LAB_A: Int](kvimagebuffertypecode_lab_a.md)
  If the image has a LAB color model, the buffer contains the  channel.
- [var kvImageBufferTypeCode_LAB_B: Int](kvimagebuffertypecode_lab_b.md)
  If the image has a LAB color model, the buffer contains the  channel.
- [var kvImageBufferTypeCode_LAB_L: Int](kvimagebuffertypecode_lab_l.md)
  If the image has a LAB color model, the buffer contains the  channel.
- [var kvImageBufferTypeCode_Luminance: Int](kvimagebuffertypecode_luminance.md)
  The buffer contains only luminance data.
- [var kvImageBufferTypeCode_Monochrome: Int](kvimagebuffertypecode_monochrome.md)
  The buffer contains a single color channel.
- [var kvImageBufferTypeCode_RGB_Blue: Int](kvimagebuffertypecode_rgb_blue.md)
  If the image has a RGB color model, the buffer contains the blue channel.
- [var kvImageBufferTypeCode_RGB_Green: Int](kvimagebuffertypecode_rgb_green.md)
  If the image has a RGB color model, the buffer contains the green channel.
- [var kvImageBufferTypeCode_RGB_Red: Int](kvimagebuffertypecode_rgb_red.md)
  If the image has a RGB color model, the buffer contains the red channel.
- [var kvImageBufferTypeCode_UniqueFormatCount: Int](kvimagebuffertypecode_uniqueformatcount.md)
- [var kvImageBufferTypeCode_XYZ_X: Int](kvimagebuffertypecode_xyz_x.md)
  If the image has a XYZ color model, the buffer contains the  channel.
- [var kvImageBufferTypeCode_XYZ_Y: Int](kvimagebuffertypecode_xyz_y.md)
  If the image has a XYZ color model, the buffer contains the  channel.
- [var kvImageBufferTypeCode_XYZ_Z: Int](kvimagebuffertypecode_xyz_z.md)
  If the image has a XYZ color model, the buffer contains the  channel.

## See Also

- [func vImageConvert_AnyToAny(vImageConverter, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimageconvert_anytoany(_:_:_:_:_:).md)
  Converts the pixels in a vImage buffer to another format, using the specified converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/1399056-vimage-buffer-type-codes)*