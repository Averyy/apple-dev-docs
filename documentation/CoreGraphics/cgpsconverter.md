# CGPSConverter

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

An opaque data type used to convert PostScript data to PDF data.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class CGPSConverter
```

```c
typedef struct CGPSConverter * CGPSConverterRef;
```

## Overview

The PostScript data is supplied by a data provider and written into a data consumer. When you create a PostScript converter object, you can supply callback functions to invoke at various stages of the conversion process.

## Topics

### Initializers
- [init?(info: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGPSConverterCallbacks>, options: CFDictionary?)](./cgpsconverter/init%28info,callbacks,options%29.md)
  Creates a new PostScript converter.
### Instance Properties
- [var isConverting: Bool](./cgpsconverter/isconverting.md)
  Checks whether the converter is currently converting data.
### Type Properties
- [class var typeID: CFTypeID](./cgpsconverter/typeid.md)
  Returns the Core Foundation type identifier for PostScript converters.
### Instance Methods
- [func abort() -> Bool](./cgpsconverter/abort%28%29.md)
  Tells a PostScript converter to abort a conversion at the next available opportunity.
- [func convert(CGDataProvider, consumer: CGDataConsumer, options: CFDictionary?) -> Bool](./cgpsconverter/convert%28_,consumer,options%29.md)
  Uses a PostScript converter to convert PostScript data to PDF data.
### Callbacks
- [CGPSConverterCallbacks](./cgpsconvertercallbacks.md)
  A structure for holding the callbacks provided when you create a PostScript converter object.
- [CGPSConverterBeginDocumentCallback](./cgpsconverterbegindocumentcallback.md)
  Performs custom tasks at the beginning of a PostScript conversion process.
- [CGPSConverterEndDocumentCallback](./cgpsconverterenddocumentcallback.md)
  Performs custom tasks at the end of a PostScript conversion process.
- [CGPSConverterBeginPageCallback](./cgpsconverterbeginpagecallback.md)
  Performs custom tasks at the beginning of each page in a PostScript conversion process.
- [CGPSConverterEndPageCallback](./cgpsconverterendpagecallback.md)
  Performs custom tasks at the end of each page of a PostScript conversion process.
- [CGPSConverterProgressCallback](./cgpsconverterprogresscallback.md)
  Reports progress periodically during a PostScript conversion process.
- [CGPSConverterMessageCallback](./cgpsconvertermessagecallback.md)
  Passes messages generated during a PostScript conversion process.
- [CGPSConverterReleaseInfoCallback](./cgpsconverterreleaseinfocallback.md)
  Performs custom tasks when a PostScript converter is released.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
### Opaque Types
- [CGContextRef](./cgcontext.md)
  A Quartz 2D drawing environment.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverter)*