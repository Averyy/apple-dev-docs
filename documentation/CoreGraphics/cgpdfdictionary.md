# CGPDFDictionary

**Framework**: Core Graphics  
**Role**: API Collection

A dictionary structure within a PDF document.

## Overview

Dictionary objects are the main building blocks of a PDF document. A key-value pair within a dictionary is called an entry. In a PDF dictionary, the key must be an array of characters. Within a given dictionary, the keys are unique—that is, no two keys in a single dictionary are equal (as determined by `strcmp`). The value associated with a key can be any kind of PDF object, including another dictionary. Dictionary objects are the main building blocks of a PDF document.

Many functions that retrieve values from a PDF dictionary take the form:

```objc
bool CGPDFDictionaryGet<DataType> (
 CGPDFDictionaryRef dictionary,
 const char *key,
 <DataType>Ref *value
);
```

These functions test whether there is an object associated with the specified key. If there is an object associated with the specified key, they test its data type. If there is no associated object, or if there is but it is not of the expected type, the function returns [`false`](../Swift/false.md). If there is an object associated with the specified key and it is of the expected type, the function returns [`true`](../Swift/true.md) and the object is passed back in the `value` parameter.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it. CGPDFDictionary objects exist only as constituent parts of a CGPDFDocument object, and they are managed by their container.

## Topics

### Applying a Function to All Entries
- [func CGPDFDictionaryApplyFunction(CGPDFDictionaryRef, CGPDFDictionaryApplierFunction, UnsafeMutableRawPointer?)](./cgpdfdictionaryapplyfunction%28_,_,_%29.md)
  Applies a function to each entry in a dictionary.
### Getting Data from a Dictionary
- [func CGPDFDictionaryGetArray(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](./cgpdfdictionarygetarray%28_,_,_%29.md)
  Returns whether there is a PDF array associated with a specified key in a PDF dictionary and, if so, retrieves that array.
- [func CGPDFDictionaryGetBoolean(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](./cgpdfdictionarygetboolean%28_,_,_%29.md)
  Returns whether there is a PDF Boolean value associated with a specified key in a PDF dictionary and, if so, retrieves the Boolean value.
- [func CGPDFDictionaryGetCount(CGPDFDictionaryRef) -> Int](./cgpdfdictionarygetcount%28_%29.md)
  Returns the number of entries in a PDF dictionary.
- [func CGPDFDictionaryGetDictionary(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](./cgpdfdictionarygetdictionary%28_,_,_%29.md)
  Returns whether there is another PDF dictionary associated with a specified key in a PDF dictionary and, if so, retrieves that dictionary.
- [func CGPDFDictionaryGetInteger(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](./cgpdfdictionarygetinteger%28_,_,_%29.md)
  Returns whether there is a PDF integer associated with a specified key in a PDF dictionary and, if so, retrieves that integer.
- [func CGPDFDictionaryGetName(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool](./cgpdfdictionarygetname%28_,_,_%29.md)
  Returns whether an object with a specified key in a PDF dictionary is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.
- [func CGPDFDictionaryGetNumber(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFReal>?) -> Bool](./cgpdfdictionarygetnumber%28_,_,_%29.md)
  Returns whether there is a PDF number associated with a specified key in a PDF dictionary and, if so, retrieves that number.
- [func CGPDFDictionaryGetObject(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](./cgpdfdictionarygetobject%28_,_,_%29.md)
  Returns whether there is a PDF object associated with a specified key in a PDF dictionary and, if so, retrieves that object.
- [func CGPDFDictionaryGetStream(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](./cgpdfdictionarygetstream%28_,_,_%29.md)
  Returns whether there is a PDF stream associated with a specified key in a PDF dictionary and, if so, retrieves that stream.
- [func CGPDFDictionaryGetString(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](./cgpdfdictionarygetstring%28_,_,_%29.md)
  Returns whether there is a PDF string associated with a specified key in a PDF dictionary and, if so, retrieves that string.
### Callbacks
- [typealias CGPDFDictionaryApplierFunction](./cgpdfdictionaryapplierfunction.md)
  Performs custom processing on a key-value pair from a PDF dictionary, using optional contextual information.
### Data Types
- [struct CGPDFDictionaryRef](./cgpdfdictionaryref.md)
  A type that encapsulates a PDF dictionary.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdictionary)*