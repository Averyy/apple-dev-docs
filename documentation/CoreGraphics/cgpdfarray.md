# CGPDFArray

**Framework**: Core Graphics  
**Role**: API Collection

An array structure within a PDF document.

## Overview

PDF arrays may be heterogeneous—that is, they may contain any other PDF objects, including PDF strings, PDF dictionaries, and other PDF arrays.

Many `CGPDFArray` functions to retrieve values from a PDF array take the form:

```objc
bool CGPDFArrayGet<DataType> (
 CGPDFArrayRef array,
 size_t index,
 <DataType>Ref *value
);
```

These functions test the data type of the object at the specified index. If the object is not of the expected type, the function returns [`false`](../Swift/false.md). If the object is of the expected type, the function returns [`true`](../Swift/true.md), and the object is passed back in the `value` parameter.

This type is not derived from [`CFTypeRef`](../CoreFoundation/cftyperef.md) and therefore there are no functions for retaining and releasing it. [`CGPDFArrayRef`](./cgpdfarrayref.md) objects exist only as constituent parts of a [`CGPDFDocument`](./cgpdfdocument.md) object, and they are managed by their container.

## Topics

### Getting Data from a PDF Array
- [func CGPDFArrayGetArray(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](./cgpdfarraygetarray%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is another PDF array and, if so, retrieves that array.
- [func CGPDFArrayGetBoolean(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](./cgpdfarraygetboolean%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF Boolean and, if so, retrieves that Boolean.
- [func CGPDFArrayGetCount(CGPDFArrayRef) -> Int](./cgpdfarraygetcount%28_%29.md)
  Returns the number of items in a PDF array.
- [func CGPDFArrayGetDictionary(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](./cgpdfarraygetdictionary%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF dictionary and, if so, retrieves that dictionary.
- [func CGPDFArrayGetInteger(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](./cgpdfarraygetinteger%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF integer and, if so, retrieves that object.
- [func CGPDFArrayGetName(CGPDFArrayRef, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool](./cgpdfarraygetname%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.
- [func CGPDFArrayGetNull(CGPDFArrayRef, Int) -> Bool](./cgpdfarraygetnull%28_,_%29.md)
  Returns whether an object at a given index in a Quartz PDF array is a PDF null.
- [func CGPDFArrayGetNumber(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFReal>?) -> Bool](./cgpdfarraygetnumber%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF number and, if so, retrieves that object.
- [func CGPDFArrayGetObject(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](./cgpdfarraygetobject%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF object and, if so, retrieves that object.
- [func CGPDFArrayGetStream(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](./cgpdfarraygetstream%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF stream and, if so, retrieves that stream.
- [func CGPDFArrayGetString(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](./cgpdfarraygetstring%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF string and, if so, retrieves that string.
### Data Types
- [struct CGPDFArrayRef](./cgpdfarrayref.md)
  An opaque type that encapsulates a PDF array.

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
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfarray)*