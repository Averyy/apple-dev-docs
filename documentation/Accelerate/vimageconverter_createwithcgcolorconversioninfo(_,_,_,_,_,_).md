# vImageConverter_CreateWithCGColorConversionInfo(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
vImageConverterRefvImageConverter_CreateWithCGColorConversionInfo(CGColorConversionInfoRef colorConversionInfoRef, const vImage_CGImageFormat *sFormat, const vImage_CGImageFormat *dFormat, const CGFloat *bg, vImage_Flags flags, vImage_Error *error);
```

#### Discussion

Use [`vImageConverter_CreateWithCGColorConversionInfo(_:_:_:_:_:_:)`](./vimageconverter_createwithcgcolorconversioninfo%28_,_,_,_,_,_%29.md) to create a converter suitable for use with [`vImageConvert_AnyToAny(_:_:_:_:_:)`](./vimageconvert_anytoany%28_,_,_,_,_%29.md), which uses [`CGColorConversionInfo`](../CoreGraphics/cgcolorconversioninfo.md) for color conversion. [`CGColorConversionInfo`](../CoreGraphics/cgcolorconversioninfo.md) provides greater control on the color-space conversion than, for example, using a converter returned by [`vImageConverter_CreateWithCGImageFormat(_:_:_:_:_:)`](./vimageconverter_createwithcgimageformat%28_,_,_,_,_%29.md).

##### Convert Linear Color Space to sRGB

You can use [`vImageConverter_CreateWithCGColorConversionInfo(_:_:_:_:_:_:)`](./vimageconverter_createwithcgcolorconversioninfo%28_,_,_,_,_,_%29.md) to convert an image with a linear response curve to sRGB. Many vImage operations provide optimal results when working on images with a linear response curve, this approach is ideal for converting between linear and sRGB.

Begin by creating the source and destination color spaces, and the [`CGColorConversionInfo`](../CoreGraphics/cgcolorconversioninfo.md) instance, as follows:

**Swift**:

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

**Objective-C**:

```objc
CGColorSpaceRef sourceColorSpace = CGColorSpaceCreateWithName(kCGColorSpaceLinearSRGB);
CGColorSpaceRef destinationColorSpace = CGColorSpaceCreateWithName(kCGColorSpaceSRGB);
CGColorConversionInfoRef conversionInfo = CGColorConversionInfoCreate(sourceColorSpace,
                                                                      destinationColorSpace);
```

Create a [`vImage_CGImageFormat`](./vimage_cgimageformat.md) structure, without a color space, that specifies the pixel memory requirement, number of channels, and alpha information, as follows:

**Swift**:

```swift
var cgImageFormat = vImage_CGImageFormat(bitsPerComponent: 8,
                                         bitsPerPixel: 8 * 3,
                                         colorSpace: nil,
                                         bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue),
                                         version: 0,
                                         decode: nil,
                                         renderingIntent: .defaultIntent)
```

**Objective-C**:

```objc
vImage_CGImageFormat cgImageFormat = {
    .bitsPerComponent = 8,
    .bitsPerPixel = 8 * 3,
    .colorSpace = NULL,
    .bitmapInfo = kCGBitmapByteOrderDefault | kCGImageAlphaNone,
    .version = 0,
    .decode = NULL,
    .renderingIntent = kCGRenderingIntentDefault
};
```

Create the converter and buffers:

**Swift**:

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

**Objective-C**:

```objc
const CGFloat bg[1] = {0};
vImageConverterRef converter = vImageConverter_CreateWithCGColorConversionInfo(
    conversionInfo,
    &cgImageFormat,
    &cgImageFormat,
    bg,
    kvImageNoFlags,
    NULL);
```

Pass the converter and the two buffers to [`vImageConvert_AnyToAny(_:_:_:_:_:)`](./vimageconvert_anytoany%28_,_,_,_,_%29.md) to perform the conversion:

**Swift**:

```swift
vImageConvert_AnyToAny(converter.takeRetainedValue(),
                       &sourceBuffer, &destinationBuffer,
                       nil,
                       vImage_Flags(kvImageNoFlags))
```

**Objective-C**:

```objc
vImageConvert_AnyToAny(converter,
                       &sourceBuffer, &destinationBuffer,
                       NULL,
                       kvImageNoFlags);
```

The following image shows the source image, on the left, and the contents of `destinationBuffer`, on the right, after conversion:

![Two photographs of a flower. The image on the left has a linear response curve and is very dark. The image on the right is sRGB and correctly rendered.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3583042@2x.png)

## Parameters

- `colorConversionInfoRef`: The object that describes how to convert between color spaces.
- `sFormat`: A pointer to a populated [`vImage_CGImageFormat`](./vimage_cgimageformat.md) that describes the image format of the source image.
- `dFormat`: A pointer to a populated [`vImage_CGImageFormat`](./vimage_cgimageformat.md) that describes the image format of the destination image.
- `bg`: An array of single-precision values, in the range 0 to 1, that specifies the background color when required.
- `flags`: The options to use when performing this operation.
- `error`: An optional `inout` value that receives an error code.

## See Also

### Creating a converter
- [class vImageConverter](./vimageconverter.md)
  A description of a conversion from one image format to another.
- [func vImageConverter_CreateWithCGImageFormat(UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](./vimageconverter_createwithcgimageformat%28_,_,_,_,_%29.md)
  Creates a vImage converter that converts from one vImage Core Graphics image format to another.
- [func vImageConverter_CreateForCGToCVImageFormat(UnsafePointer<vImage_CGImageFormat>, vImageCVImageFormat, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](./vimageconverter_createforcgtocvimageformat%28_,_,_,_,_%29.md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.
- [func vImageConverter_CreateForCVToCGImageFormat(vImageCVImageFormat, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](./vimageconverter_createforcvtocgimageformat%28_,_,_,_,_%29.md)
  Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.
- [func vImageConverter_CreateWithColorSyncCodeFragment(CFTypeRef, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>!, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](./vimageconverter_createwithcolorsynccodefragment%28_,_,_,_,_,_%29.md)
  Creates a vImage converter to convert from one vImage Core Graphics image format to another, using custom ColorSync transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_createwithcgcolorconversioninfo(_:_:_:_:_:_:))*