# CGPDFContentStream

**Framework**: Core Graphics  
**Role**: API Collection

A representation of one or more content data streams in a PDF page.

## Overview

A [`CGPDFContentStreamRef`](./cgpdfcontentstreamref.md) object represents one or more PDF content streams for a page and their associated resource dictionaries. A PDF content stream is a sequential set of instructions that specifies how to paint items on a PDF page. A resource dictionary contains information needed by the content stream in order to decode the sequential instructions of the content stream.

[`CGPDFContentStreamRef`](./cgpdfcontentstreamref.md) functions can retrieve both the content streams and the resource dictionaries associated with a PDF page.

This type is not derived from [`CFTypeRef`](../CoreFoundation/cftyperef.md) and therefore there are no functions for retaining and releasing it. [`CGPDFContentStreamRef`](./cgpdfcontentstreamref.md) objects exist only as constituent parts of a [`CGPDFDocument`](./cgpdfdocument.md) object, and they are managed by their container.

## Topics

### Creating a PDF Content Stream Object
- [func CGPDFContentStreamCreateWithPage(CGPDFPage) -> CGPDFContentStreamRef](./cgpdfcontentstreamcreatewithpage%28_%29.md)
  Creates a content stream object from a PDF page object.
- [func CGPDFContentStreamCreateWithStream(CGPDFStreamRef, CGPDFDictionaryRef, CGPDFContentStreamRef) -> CGPDFContentStreamRef](./cgpdfcontentstreamcreatewithstream%28_,_,_%29.md)
  Creates a PDF content stream object from an existing PDF content stream object.
### Getting Data from a PDF Content Stream Object
- [func CGPDFContentStreamGetStreams(CGPDFContentStreamRef) -> CFArray?](./cgpdfcontentstreamgetstreams%28_%29.md)
  Gets the array of PDF content streams contained in a PDF content stream object.
- [func CGPDFContentStreamGetResource(CGPDFContentStreamRef, UnsafePointer<CChar>, UnsafePointer<CChar>) -> CGPDFObjectRef?](./cgpdfcontentstreamgetresource%28_,_,_%29.md)
  Gets the specified resource from a PDF content stream object.
### Retaining and Releasing a PDF Content Stream Object
- [func CGPDFContentStreamRetain(CGPDFContentStreamRef) -> CGPDFContentStreamRef](./cgpdfcontentstreamretain%28_%29.md)
  Increments the retain count of a PDF content stream object.
- [func CGPDFContentStreamRelease(CGPDFContentStreamRef)](./cgpdfcontentstreamrelease%28_%29.md)
  Decrements the retain count of a PDF content stream object.
### Data Types
- [typealias CGPDFContentStreamRef](./cgpdfcontentstreamref.md)
  An opaque type that provides access to the data that describes the appearance of a PDF page.

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
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstream)*