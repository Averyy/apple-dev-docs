# CGImage

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A bitmap image or image mask.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CGImage
```

```c
typedef struct CGImage * CGImageRef;
```

#### Overview

A bitmap image is a rectangular array of pixels, each of which represents a single sample or data point from a source image.

## Topics

### Creating images
- [init?(width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](./cgimage/init%28width,height,bitspercomponent,bitsperpixel,bytesperrow,space,bitmapinfo,provider,decode,shouldinterpolate,intent%29.md)
  Creates a bitmap image from data supplied by a data provider.
- [init?(jpegDataProviderSource: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](./cgimage/init%28jpegdataprovidersource,decode,shouldinterpolate,intent%29.md)
  Creates a bitmap image using JPEG-encoded data supplied by a data provider.
- [init?(pngDataProviderSource: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](./cgimage/init%28pngdataprovidersource,decode,shouldinterpolate,intent%29.md)
  Creates a bitmap image using PNG-encoded data supplied by a data provider.
- [init?(headroom: Float, width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](./cgimage/init%28headroom,width,height,bitspercomponent,bitsperpixel,bytesperrow,space,bitmapinfo,provider,decode,shouldinterpolate,intent%29.md)
### Examining an image
- [var isMask: Bool](./cgimage/ismask.md)
  Returns whether a bitmap image is an image mask.
- [var width: Int](./cgimage/width.md)
  Returns the width of a bitmap image, in pixels.
- [var height: Int](./cgimage/height.md)
  Returns the height of a bitmap image.
- [var bitsPerComponent: Int](./cgimage/bitspercomponent.md)
  Returns the number of bits allocated for a single color component of a bitmap image.
- [var bitsPerPixel: Int](./cgimage/bitsperpixel.md)
  Returns the number of bits allocated for a single pixel in a bitmap image.
- [var bytesPerRow: Int](./cgimage/bytesperrow.md)
  Returns the number of bytes allocated for a single row of a bitmap image.
- [var colorSpace: CGColorSpace?](./cgimage/colorspace.md)
  Return the color space for a bitmap image.
- [var alphaInfo: CGImageAlphaInfo](./cgimage/alphainfo.md)
  Returns the alpha channel information for a bitmap image.
- [enum CGImageAlphaInfo](./cgimagealphainfo.md)
  Storage options for alpha component data.
- [var dataProvider: CGDataProvider?](./cgimage/dataprovider.md)
  Returns the data provider for a bitmap image or image mask.
- [var decode: UnsafePointer<CGFloat>?](./cgimage/decode.md)
  Returns the decode array for a bitmap image.
- [var shouldInterpolate: Bool](./cgimage/shouldinterpolate.md)
  Returns the interpolation setting for a bitmap image.
- [var renderingIntent: CGColorRenderingIntent](./cgimage/renderingintent.md)
  Returns the rendering intent setting for a bitmap image.
- [var bitmapInfo: CGBitmapInfo](./cgimage/bitmapinfo.md)
  Returns the bitmap information for a bitmap image.
- [struct CGBitmapInfo](./cgbitmapinfo.md)
  Component information for a bitmap image.
- [var utType: CFString?](./cgimage/uttype.md)
  The Universal Type Identifier for the image.
### Copying an image
- [func copy() -> CGImage?](./cgimage/copy%28%29.md)
  Creates a copy of a bitmap image.
- [func copy(colorSpace: CGColorSpace) -> CGImage?](./cgimage/copy%28colorspace%29.md)
  Creates a copy of a bitmap image, replacing its colorspace.
### Creating images by modifying an image
- [func cropping(to: CGRect) -> CGImage?](./cgimage/cropping%28to%29.md)
  Creates a bitmap image using the data contained within a subregion of an existing bitmap image.
- [func masking(CGImage) -> CGImage?](./cgimage/masking%28_%29.md)
  Creates a bitmap image from an existing image and an image mask.
- [func copy(maskingColorComponents: [CGFloat]) -> CGImage?](./cgimage/copy%28maskingcolorcomponents%29.md)
### Creating image masks
- [init?(maskWidth: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool)](./cgimage/init%28maskwidth,height,bitspercomponent,bitsperpixel,bytesperrow,provider,decode,shouldinterpolate%29.md)
  Creates a bitmap image mask from data supplied by a data provider.
- [CGImageCreateWithMaskingColors](./cgimagecreatewithmaskingcolors.md)
  Creates a bitmap image by masking an existing bitmap image with the provided color values.
### Adopting high dynamic range (HDR)
- [Enhancing high dynamic range image rendering](./adopting-advancements-in-hdr-image-rendering.md)
  Improve your app’s High Dynamic Range (HDR) image support with metadata.
- [var contentHeadroom: Float](./cgimage/contentheadroom.md)
- [var calculatedContentHeadroom: Float](./cgimage/calculatedcontentheadroom.md)
- [var contentAverageLightLevel: Float](./cgimage/contentaveragelightlevel.md)
- [var calculatedContentAverageLightLevel: Float](./cgimage/calculatedcontentaveragelightlevel.md)
- [func copy(contentAverageLightLevel: Float) -> CGImage?](./cgimage/copy%28contentaveragelightlevel%29.md)
- [func copyWithCalculatedHDRStats() -> CGImage?](./cgimage/copywithcalculatedhdrstats%28%29.md)
### Constants
- [enum CGImageAlphaInfo](./cgimagealphainfo.md)
  Storage options for alpha component data.
- [struct CGBitmapInfo](./cgbitmapinfo.md)
  Component information for a bitmap image.
- [Host Endian Bitmap Formats](./host-endian-bitmap-formats.md)
  Bit-depth constants for image bitmaps in host-endian byte order.
### Working with Core Foundation types
- [class var typeID: CFTypeID](./cgimage/typeid.md)
  Returns the type identifier for CGImage objects.
### Instance properties
- [var byteOrderInfo: CGImageByteOrderInfo](./cgimage/byteorderinfo.md)
- [var containsImageSpecificToneMappingMetadata: Bool](./cgimage/containsimagespecifictonemappingmetadata.md)
- [var contentHeadroom: Float](./cgimage/contentheadroom.md)
- [var pixelFormatInfo: CGImagePixelFormatInfo](./cgimage/pixelformatinfo.md)
- [var shouldToneMap: Bool](./cgimage/shouldtonemap.md)
### Retaining and releasing images
- [CGImageRetain](./cgimageretain.md)
  Increments the retain count of a bitmap image.
- [CGImageRelease](./cgimagerelease.md)
  Decrements the retain count of a bitmap image.

## Relationships

### Conforms To
- [AttachableAsImage](../Testing/attachableasimage.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
### 2D Drawing
- [class CGContext](./cgcontext.md)
  A Quartz 2D drawing environment.
- [class CGPath](./cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGMutablePath](./cgmutablepath.md)
  A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGLayer](./cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.
### Opaque Types
- [CGColorRef](./cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorConversionInfoRef](./cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [CGColorSpaceRef](./cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [CGDataConsumerRef](./cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProviderRef](./cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGFontRef](./cgfont.md)
  A set of character glyphs and layout information for drawing text.
- [CGFunctionRef](./cgfunction.md)
  A general facility for defining and using callback functions.
- [CGGradientRef](./cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGPatternRef](./cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.
- [CGPDFArray](./cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage)*