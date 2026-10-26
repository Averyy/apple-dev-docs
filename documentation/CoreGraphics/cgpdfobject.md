# CGPDFObject

**Framework**: Core Graphics  
**Role**: API Collection

An object representing content within a PDF document.

#### Overview

PDF supports several basic types of object: Boolean values, integer and real numbers, strings, names, arrays, dictionaries, and streams. Most of these are represented in Core Graphics by corresponding specific types. A CGPDFObject can represent any of these types. You use CGPDFObject functions to determine the type of the object, and retrieve the object value if it is of an expected type.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it. CGPDFObject objects exist as constituent parts of a CGPDFDocument object, and are managed by their container.

## Topics

### Getting Object Types and Values
- [func CGPDFObjectGetType(CGPDFObjectRef) -> CGPDFObjectType](./cgpdfobjectgettype%28_%29.md)
  Returns the PDF type identifier of an object.
- [func CGPDFObjectGetValue(CGPDFObjectRef, CGPDFObjectType, UnsafeMutableRawPointer?) -> Bool](./cgpdfobjectgetvalue%28_,_,_%29.md)
  Returns whether an object is of a given type and if it is, retrieves its value.
### Data Types
- [struct CGPDFObjectRef](./cgpdfobjectref.md)
  A type that contains information about a PDF object.
- [typealias CGPDFBoolean](./cgpdfboolean.md)
  A PDF Boolean value.
- [typealias CGPDFInteger](./cgpdfinteger.md)
  A PDF integer value.
- [typealias CGPDFReal](./cgpdfreal.md)
  A PDF real value.
### Constants
- [enum CGPDFObjectType](./cgpdfobjecttype.md)
  Types of PDF object.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfobject)*