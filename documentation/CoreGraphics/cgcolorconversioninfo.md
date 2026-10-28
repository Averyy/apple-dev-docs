# CGColorConversionInfo

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

An object that describes how to convert between color spaces for use by other system services.

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
class CGColorConversionInfo
```

```c
typedef const struct CGColorConversionInfo * CGColorConversionInfoRef;
```

## Overview

A [`CGColorConversionInfo`](./cgcolorconversioninfo.md) object specifies a conversion between two or more color spaces, including information about the intent of the conversion. You use color conversion objects to specify the work to be done by an [`MPSImageConversion`](../MetalPerformanceShaders/mpsimageconversion.md) filter, which can then perform GPU-accelerated image conversion.

## Topics

### Creating a Color Conversion
- [init?(src: CGColorSpace, dst: CGColorSpace)](./cgcolorconversioninfo/init%28src,dst%29.md)
  Creates a conversion between two specified color spaces.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](./cgcolorconversioninfo/init%28optionssrc,dst,options%29.md)
- [enum CGColorConversionInfoTransformType](./cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [CGColorConversionInfoCreateFromList](./cgcolorconversioninfocreatefromlist.md)
  Creates a conversion between an arbitrary number of specified color spaces.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgcolorconversioninfo/typeid.md)
  Returns the Core Foundation type identifier for a color conversion info data type.
### Instance Methods
- [func convert(width: Int, height: Int, to: UnsafeMutableRawPointer, format: CGColorBufferFormat, from: UnsafeRawPointer, format: CGColorBufferFormat, options: CFDictionary?) -> Bool](./cgcolorconversioninfo/convert%28width,height,to,format,from,format,options%29.md)
### Initializers
- [init?(src: CGColorSpace, srcHeadroom: Float, dst: CGColorSpace, dstHeadroom: Float, toneMapping: CGToneMapping, options: CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](./cgcolorconversioninfo/init%28src,srcheadroom,dst,dstheadroom,tonemapping,options,_%29.md)
### Color Conversion Options
- [kCGColorConversionBlackPointCompensation](./cgcolor/conversionblackpointcompensation.md)
  An option for whether to apply black point compensation when converting between color profiles.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Colors and Fonts
- [class CGColor](./cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [class CGColorSpace](./cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [class CGFont](./cgfont.md)
  A set of character glyphs and layout information for drawing text.
### Opaque Types
- [CGContextRef](./cgcontext.md)
  A Quartz 2D drawing environment.
- [CGDataConsumerRef](./cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProviderRef](./cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGFunctionRef](./cgfunction.md)
  A general facility for defining and using callback functions.
- [CGGradientRef](./cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGImageRef](./cgimage.md)
  A bitmap image or image mask.
- [CGLayerRef](./cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.
- [CGPathRef](./cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGPatternRef](./cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.
- [CGPDFArray](./cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo)*