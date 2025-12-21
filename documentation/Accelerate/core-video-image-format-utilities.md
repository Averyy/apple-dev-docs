# Core Video image format utilities

**Framework**: Accelerate

Create, copy, and query Core Video image format descriptions.

## Topics

### Creating Core Video image formats
- [class vImageCVImageFormat](vimagecvimageformat.md)
  A mutable description of image encoding in a Core Video pixel buffer.
- [class vImageConstCVImageFormat](vimageconstcvimageformat.md)
  An immutable description of image encoding in a Core Video pixel buffer.
- [func vImageCVImageFormat_CreateWithCVPixelBuffer(CVPixelBuffer!) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_createwithcvpixelbuffer(_:).md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.
- [func vImageCVImageFormat_Create(UInt32, UnsafePointer<vImage_ARGBToYpCbCrMatrix>!, CFString!, CGColorSpace!, Int32) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_create(_:_:_:_:_:).md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.
### Copying Core Video image formats
- [func vImageCVImageFormat_Copy(vImageConstCVImageFormat) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_copy(_:).md)
  Returns a mutable copy of an immutable Core Video image format.
### Querying and setting the alpha hint
- [func vImageCVImageFormat_GetAlphaHint(vImageConstCVImageFormat) -> Int32](vimagecvimageformat_getalphahint(_:).md)
  Returns the alpha hint of a Core Video image format.
- [func vImageCVImageFormat_SetAlphaHint(vImageCVImageFormat, Int32) -> vImage_Error](vimagecvimageformat_setalphahint(_:_:).md)
  Sets the alpha hint of a Core Video image format.
### Querying and setting channel information
- [func vImageCVImageFormat_GetChannelCount(vImageConstCVImageFormat) -> UInt32](vimagecvimageformat_getchannelcount(_:).md)
  Returns the number of channels, including alpha, for the Core Video image format.
- [func vImageCVImageFormat_GetChannelDescription(vImageConstCVImageFormat, vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription>!](vimagecvimageformat_getchanneldescription(_:_:).md)
  Returns the channel description for a particular channel type.
- [func vImageCVImageFormat_CopyChannelDescription(vImageCVImageFormat, UnsafePointer<vImageChannelDescription>, vImageBufferTypeCode) -> vImage_Error](vimagecvimageformat_copychanneldescription(_:_:_:).md)
  Copies the channel description for a particular channel type to an image format.
- [func vImageCVImageFormat_GetChannelNames(vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode>!](vimagecvimageformat_getchannelnames(_:).md)
  Returns the names of the channels of a Core Video image format.
- [struct vImageChannelDescription](vimagechanneldescription.md)
  A description of the range and clamp limits for a pixel format.
### Querying and setting the chrominance siting
- [func vImageCVImageFormat_GetChromaSiting(vImageConstCVImageFormat) -> Unmanaged<CFString>!](vimagecvimageformat_getchromasiting(_:).md)
  Returns the chrominance siting of a Core Video image format.
- [func vImageCVImageFormat_SetChromaSiting(vImageCVImageFormat, CFString!) -> vImage_Error](vimagecvimageformat_setchromasiting(_:_:).md)
  Sets the chrominance siting of a Core Video image format.
### Querying and setting the color space
- [func vImageCVImageFormat_GetColorSpace(vImageConstCVImageFormat) -> Unmanaged<CGColorSpace>!](vimagecvimageformat_getcolorspace(_:).md)
  Returns the color space of a Core Video image format.
- [func vImageCVImageFormat_SetColorSpace(vImageCVImageFormat, CGColorSpace!) -> vImage_Error](vimagecvimageformat_setcolorspace(_:_:).md)
  Sets the color space of a Core Video image format.
### Querying and setting the conversion matrix
- [func vImageCVImageFormat_GetConversionMatrix(vImageConstCVImageFormat, UnsafeMutablePointer<vImageMatrixType>!) -> UnsafeRawPointer!](vimagecvimageformat_getconversionmatrix(_:_:).md)
  Returns a pointer to the RGB-to-YpCbCr conversion matrix of a Core Video image format.
- [func vImageCVImageFormat_CopyConversionMatrix(vImageCVImageFormat, UnsafeRawPointer, vImageMatrixType) -> vImage_Error](vimagecvimageformat_copyconversionmatrix(_:_:_:).md)
  Copies an RGB-to-YpCbCr conversion matrix to an image format’s internal matrix.
### Querying the image format code
- [func vImageCVImageFormat_GetFormatCode(vImageConstCVImageFormat) -> UInt32](vimagecvimageformat_getformatcode(_:).md)
  Returns the four-character code that encodes the pixel format of a Core Video image format.
### Querying and setting the user data
- [func vImageCVImageFormat_GetUserData(vImageConstCVImageFormat) -> UnsafeMutableRawPointer!](vimagecvimageformat_getuserdata(_:).md)
  Returns the user data of a Core Video image format.
- [func vImageCVImageFormat_SetUserData(vImageCVImageFormat, UnsafeMutableRawPointer!, ((vImageCVImageFormat?, UnsafeMutableRawPointer?) -> Void)!) -> vImage_Error](vimagecvimageformat_setuserdata(_:_:_:).md)
  Sets the user data of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/core-video-image-format-utilities)*