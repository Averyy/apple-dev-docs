# vImageConverter_CreateForCVToCGImageFormat(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConverter_CreateForCVToCGImageFormat(_ srcFormat: vImageCVImageFormat, _ destFormat: UnsafePointer<vImage_CGImageFormat>, _ backgroundColor: UnsafePointer<CGFloat>!, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes described in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function creates a [`vImageConverter`](vimageconverter.md) instance that’s used with [`vImageConvert_AnyToAny(_:_:_:_:_:)`](vimageconvert_anytoany(_:_:_:_:_:).md) to convert a Core Video formatted image, described by [`vImageCVImageFormat`](vimagecvimageformat.md), to Core Graphics image data, described by [`vImage_CGImageFormat`](vimage_cgimageformat.md).

## Parameters

- `srcFormat`: The   structure that describes the pixel format associated with the source image buffers.
- `destFormat`: The   structure that describes the pixel format associated with the destination buffers.
- `backgroundColor`: In cases where the source format has an alpha channel and the destination doesn’t (or is   or  ) the conversion removes the alpha channel by flattening it against an opaque background color. The background color is specified as three   values corresponding to red, green, and blue in sRGB.
- `flags`: The options to use when performing this operation. The following flags are supported:

## See Also

- [class vImageConverter](vimageconverter.md)
  A description of a conversion from one image format to another.
- [func vImageConverter_CreateWithCGImageFormat(UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts from one vImage Core Graphics image format to another.
- [func vImageConverter_CreateWithCGColorConversionInfo(CGColorConversionInfo, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgcolorconversioninfo(_:_:_:_:_:_:).md)
  Creates an any-to-any converter that uses a color conversion information object to convert from one image format to another.
- [func vImageConverter_CreateForCGToCVImageFormat(UnsafePointer<vImage_CGImageFormat>, vImageCVImageFormat, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcgtocvimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.
- [func vImageConverter_CreateWithColorSyncCodeFragment(CFTypeRef, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>!, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcolorsynccodefragment(_:_:_:_:_:_:).md)
  Creates a vImage converter to convert from one vImage Core Graphics image format to another, using custom ColorSync transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_createforcvtocgimageformat(_:_:_:_:_:))*