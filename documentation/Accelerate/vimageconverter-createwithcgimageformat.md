# vImageConverter_CreateWithCGImageFormat(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates a vImage converter that converts from one vImage Core Graphics image format to another.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConverter_CreateWithCGImageFormat(_ srcFormat: UnsafePointer<vImage_CGImageFormat>, _ destFormat: UnsafePointer<vImage_CGImageFormat>, _ backgroundColor: UnsafePointer<CGFloat>!, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!
```

## Mentions

- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes.

#### Discussion

This function creates a [`vImageConverter`](vimageconverter.md) instance to convert between image formats described by [`vImage_CGImageFormat`](vimage_cgimageformat.md).  The [`vImageConverter`](vimageconverter.md) is intended to be used and reused with [`vImageConvert_AnyToAny(_:_:_:_:_:)`](vimageconvert_anytoany(_:_:_:_:_:).md) to convert images from one format to another.

## Parameters

- `srcFormat`: A pointer to a populated   structure describing the image format of the source image. If the   value is  , sRGB is used as the default value. The   reference is retained by this function and is released when the   is destroyed.
- `destFormat`: A pointer to a populated   structure describing the image format of the destination image. If the   value is  , sRGB is used as the default value. The   reference is retained by this function and is released when the   is destroyed.
- `backgroundColor`: An array of floats to be used as a background color if one is needed. The   range is assumed to be [0,1]. The channel ordering and number of color channels must match the natural order of the destination colorspace (for example, RGB or CMYK). The   value may be   if no background color is needed.
- `flags`: The options to use when performing this operation. The following flags are supported:

## See Also

- [class vImageConverter](vimageconverter.md)
  A description of a conversion from one image format to another.
- [func vImageConverter_CreateWithCGColorConversionInfo(CGColorConversionInfo, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgcolorconversioninfo(_:_:_:_:_:_:).md)
  Creates an any-to-any converter that uses a color conversion information object to convert from one image format to another.
- [func vImageConverter_CreateForCGToCVImageFormat(UnsafePointer<vImage_CGImageFormat>, vImageCVImageFormat, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcgtocvimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.
- [func vImageConverter_CreateForCVToCGImageFormat(vImageCVImageFormat, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcvtocgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.
- [func vImageConverter_CreateWithColorSyncCodeFragment(CFTypeRef, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>!, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcolorsynccodefragment(_:_:_:_:_:_:).md)
  Creates a vImage converter to convert from one vImage Core Graphics image format to another, using custom ColorSync transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_createwithcgimageformat(_:_:_:_:_:))*