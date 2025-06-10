# Functions that perform any-to-any conversion

**Framework**: Accelerate

Convert between Core Video or Core Graphics image data of arbitrary color spaces and bit depths.

## Topics

### Creating a converter
- [class vImageConverter](vimageconverter.md)
  A description of a conversion from one image format to another.
- [func vImageConverter_CreateWithCGImageFormat(UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts from one vImage Core Graphics image format to another.
- [func vImageConverter_CreateWithCGColorConversionInfo(CGColorConversionInfo, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgcolorconversioninfo(_:_:_:_:_:_:).md)
  Creates an any-to-any converter that uses a color conversion information object to convert from one image format to another.
- [func vImageConverter_CreateForCGToCVImageFormat(UnsafePointer<vImage_CGImageFormat>, vImageCVImageFormat, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcgtocvimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.
- [func vImageConverter_CreateForCVToCGImageFormat(vImageCVImageFormat, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcvtocgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.
- [func vImageConverter_CreateWithColorSyncCodeFragment(CFTypeRef, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>!, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcolorsynccodefragment(_:_:_:_:_:_:).md)
  Creates a vImage converter to convert from one vImage Core Graphics image format to another, using custom ColorSync transform.
### Performing a conversion
- [func vImageConvert_AnyToAny(vImageConverter, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimageconvert_anytoany(_:_:_:_:_:).md)
  Converts the pixels in a vImage buffer to another format, using the specified converter.
- [vImage Buffer Type Codes](1399056-vimage-buffer-type-codes.md)
  Constants that specify the contents of vImage buffers.
### Querying a converter’s properties
- [func vImageConverter_MustOperateOutOfPlace(vImageConverter, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](vimageconverter_mustoperateoutofplace(_:_:_:_:).md)
  Determines whether a converter is capable of operating in place.
- [func vImageConverter_GetSourceBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](vimageconverter_getsourcebufferorder(_:).md)
  Returns a list of vImage source buffer channel names, specifying the order of planes.
- [func vImageConverter_GetDestinationBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](vimageconverter_getdestinationbufferorder(_:).md)
  Returns a list of vImage destination buffer channel names, specifying the order of planes.
- [func vImageConverter_GetNumberOfSourceBuffers(vImageConverter) -> UInt](vimageconverter_getnumberofsourcebuffers(_:).md)
  Returns the number of source buffers consumed by the converter.
- [func vImageConverter_GetNumberOfDestinationBuffers(vImageConverter) -> UInt](vimageconverter_getnumberofdestinationbuffers(_:).md)
  Returns the number of destination buffers written to by the converter.
### Memory management
- [vImageConverter_Retain](vimageconverter_retain.md)
  Retains a vImage converter.
- [vImageConverter_Release](vimageconverter_release.md)
  Releases a vImage converter.

## See Also

- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
  Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.
- [Converting chroma-subsampled images](converting-chroma-subsampled-images.md)
  Create vImage buffers with the correct dimensions to convert to and from images with subsampled chroma information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-perform-any-to-any-conversion)*