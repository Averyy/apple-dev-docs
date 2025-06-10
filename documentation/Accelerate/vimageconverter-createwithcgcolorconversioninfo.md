# vImageConverter_CreateWithCGColorConversionInfo(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates an any-to-any converter that uses a color conversion information object to convert from one image format to another.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func vImageConverter_CreateWithCGColorConversionInfo(_ colorConversionInfoRef: CGColorConversionInfo, _ sFormat: UnsafePointer<vImage_CGImageFormat>, _ dFormat: UnsafePointer<vImage_CGImageFormat>, _ bg: UnsafePointer<CGFloat>!, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!
```

#### Discussion

Use [`vImageConverter_CreateWithCGColorConversionInfo(_:_:_:_:_:_:)`](vimageconverter_createwithcgcolorconversioninfo(_:_:_:_:_:_:).md) to create a converter suitable for use with [`vImageConvert_AnyToAny(_:_:_:_:_:)`](vimageconvert_anytoany(_:_:_:_:_:).md), which uses [`CGColorConversionInfo`](https://developer.apple.com/documentation/CoreGraphics/CGColorConversionInfo) for color conversion. [`CGColorConversionInfo`](https://developer.apple.com/documentation/CoreGraphics/CGColorConversionInfo) provides greater control on the color-space conversion than, for example, using a converter returned by [`vImageConverter_CreateWithCGImageFormat(_:_:_:_:_:)`](vimageconverter_createwithcgimageformat(_:_:_:_:_:).md).

##### Convert Linear Color Space to Srgb

You can use [`vImageConverter_CreateWithCGColorConversionInfo(_:_:_:_:_:_:)`](vimageconverter_createwithcgcolorconversioninfo(_:_:_:_:_:_:).md) to convert an image with a linear response curve to sRGB. Many vImage operations provide optimal results when working on images with a linear response curve, this approach is ideal for converting between linear and sRGB.

Begin by creating the source and destination color spaces, and the [`CGColorConversionInfo`](https://developer.apple.com/documentation/CoreGraphics/CGColorConversionInfo) instance:

```swift
guard
    let sourceColorSpace = CGColorSpace(name: CGColorSpace.linearSRGB),
    let destinationColorSpace = CGColorSpace(name: CGColorSpace.sRGB),
    let conversionInfo = CGColorConversionInfo(src: sourceColorSpace,
                                               dst: destinationColorSpace)
else {
    return
}
```

Create a [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure, without a color space, that specifies the pixel memory requirement, number of channels, and alpha information:

```swift
var cgImageFormat = vImage_CGImageFormat(bitsPerComponent: 8,
                                         bitsPerPixel: 8 * 3,
                                         colorSpace: nil,
                                         bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue),
                                         version: 0,
                                         decode: nil,
                                         renderingIntent: .defaultIntent)
```

Create the converter and buffers:

```swift
guard
    let converter = vImageConverter_CreateWithCGColorConversionInfo(conversionInfo,
                                                                    &cgImageFormat,
                                                                    &cgImageFormat,
                                                                    [0],
                                                                    vImage_Flags(kvImageNoFlags),
                                                                    nil),
    var sourceBuffer = try? vImage_Buffer(cgImage: sourceCGImage,
                                          format: cgImageFormat),
    var destinationBuffer = try? vImage_Buffer(width: Int(image.size.width),
                                               height: Int(image.size.height),
                                               bitsPerPixel: cgImageFormat.bitsPerPixel) else {
    return
}
```

Pass the converter and the two buffers to [`vImageConvert_AnyToAny(_:_:_:_:_:)`](vimageconvert_anytoany(_:_:_:_:_:).md) to perform the conversion:

```swift
vImageConvert_AnyToAny(converter.takeRetainedValue(),
                       &sourceBuffer, &destinationBuffer,
                       nil,
                       vImage_Flags(kvImageNoFlags))
```

The following image shows the source image, on the left, and the contents of `destinationBuffer`, on the right, after conversion:

![Two photographs of a flower. The image on the left has a linear response curve and is very dark. The image on the right is sRGB and correctly rendered.](https://docs-assets.developer.apple.com/published/4646644c6ee3528f6eec9b5fb4678e09/media-3583042%402x.png)

## Parameters

- `colorConversionInfoRef`: The object that describes how to convert between color spaces.
- `sFormat`: A pointer to a populated   that describes the image format of the source image.
- `dFormat`: A pointer to a populated   that describes the image format of the destination image.
- `bg`: An array of single-precision values, in the range 0 to 1, that specifies the background color when required.
- `flags`: The options to use when performing this operation.
- `error`: An optional   value that receives an error code.

## See Also

- [class vImageConverter](vimageconverter.md)
  A description of a conversion from one image format to another.
- [func vImageConverter_CreateWithCGImageFormat(UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts from one vImage Core Graphics image format to another.
- [func vImageConverter_CreateForCGToCVImageFormat(UnsafePointer<vImage_CGImageFormat>, vImageCVImageFormat, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcgtocvimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.
- [func vImageConverter_CreateForCVToCGImageFormat(vImageCVImageFormat, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcvtocgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.
- [func vImageConverter_CreateWithColorSyncCodeFragment(CFTypeRef, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>!, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcolorsynccodefragment(_:_:_:_:_:_:).md)
  Creates a vImage converter to convert from one vImage Core Graphics image format to another, using custom ColorSync transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_createwithcgcolorconversioninfo(_:_:_:_:_:_:))*