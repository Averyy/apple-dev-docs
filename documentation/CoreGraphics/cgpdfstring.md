# CGPDFString

**Framework**: Core Graphics  
**Role**: API Collection

A text string in a PDF document.

#### Overview

A PDF string object is a series of bytes—unsigned integer values in the range 0 to 255.

The string elements are not integer objects, but are stored in a more compact format. For more information on the representation of strings in PDF, see the latest version of *PDF Reference*, Adobe Systems Incorporated.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it. CGPDFString objects exist as constituent parts of a CGPDFDocument object, and are managed by their container.

## Topics

### Converting PDF Strings
- [func CGPDFStringCopyTextString(CGPDFStringRef) -> CFString?](./cgpdfstringcopytextstring%28_%29.md)
  Returns a CFString object that represents a PDF string as a text string.
- [func CGPDFStringCopyDate(CGPDFStringRef) -> CFDate?](./cgpdfstringcopydate%28_%29.md)
  Converts a string to a date.
### Getting PDF String Data
- [func CGPDFStringGetBytePtr(CGPDFStringRef) -> UnsafePointer<UInt8>?](./cgpdfstringgetbyteptr%28_%29.md)
  Returns a pointer to the bytes of a PDF string.
- [func CGPDFStringGetLength(CGPDFStringRef) -> Int](./cgpdfstringgetlength%28_%29.md)
  Returns the number of bytes in a PDF string.
### Data Types
- [struct CGPDFStringRef](./cgpdfstringref.md)
  A data type that represents a string in a PDF document.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstring)*