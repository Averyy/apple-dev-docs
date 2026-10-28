# CGPDFScanner

**Framework**: Core Graphics  
**Role**: API Collection

A parser object for handling content and operators in a PDF content stream.

## Overview

You can set up the PDF scanner object to invoke callbacks when it encounters specific PDF operators in the stream.

This object is not derived from `CFType`. In Objective-C, use [`CGPDFScannerRetain(_:)`](./cgpdfscannerretain%28_%29.md) and [`CGPDFScannerRelease(_:)`](./cgpdfscannerrelease%28_%29.md) to manage the retain count of [`CGPDFScannerRef`](./cgpdfscannerref.md) instances; do not use [`CFRetain`](../CoreFoundation/cfretain.md) and [`CFRelease`](../CoreFoundation/cfrelease.md).

## Topics

### Creating a PDF Scanner Object
- [func CGPDFScannerCreate(CGPDFContentStreamRef, CGPDFOperatorTableRef?, UnsafeMutableRawPointer?) -> CGPDFScannerRef](./cgpdfscannercreate%28_,_,_%29.md)
  Creates a PDF scanner.
### Retaining and Releasing PDF Scanner Objects
- [func CGPDFScannerRetain(CGPDFScannerRef) -> CGPDFScannerRef](./cgpdfscannerretain%28_%29.md)
  Increments the retain count of a scanner object.
- [func CGPDFScannerRelease(CGPDFScannerRef)](./cgpdfscannerrelease%28_%29.md)
  Decrements the retain count of a scanner object.
### Parsing Content
- [func CGPDFScannerScan(CGPDFScannerRef) -> Bool](./cgpdfscannerscan%28_%29.md)
  Parses the content stream of a PDF scanner object.
- [func CGPDFScannerGetContentStream(CGPDFScannerRef) -> CGPDFContentStreamRef](./cgpdfscannergetcontentstream%28_%29.md)
  Returns the content stream associated with a PDF scanner object.
### Getting PDF Objects from the Scanner Stack
- [func CGPDFScannerPopObject(CGPDFScannerRef, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](./cgpdfscannerpopobject%28_,_%29.md)
  Retrieves an object from the scanner stack.
- [func CGPDFScannerPopBoolean(CGPDFScannerRef, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](./cgpdfscannerpopboolean%28_,_%29.md)
  Retrieves a Boolean object from the scanner stack.
- [func CGPDFScannerPopInteger(CGPDFScannerRef, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](./cgpdfscannerpopinteger%28_,_%29.md)
  Retrieves an integer object from the scanner stack.
- [func CGPDFScannerPopNumber(CGPDFScannerRef, UnsafeMutablePointer<CGPDFReal>?) -> Bool](./cgpdfscannerpopnumber%28_,_%29.md)
  Retrieves a real value object from the scanner stack.
- [func CGPDFScannerPopName(CGPDFScannerRef, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool](./cgpdfscannerpopname%28_,_%29.md)
  Retrieves a character string from the scanner stack.
- [func CGPDFScannerPopString(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](./cgpdfscannerpopstring%28_,_%29.md)
  Retrieves a string object from the scanner stack.
- [func CGPDFScannerPopArray(CGPDFScannerRef, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](./cgpdfscannerpoparray%28_,_%29.md)
  Retrieves an array object from the scanner stack.
- [func CGPDFScannerPopDictionary(CGPDFScannerRef, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](./cgpdfscannerpopdictionary%28_,_%29.md)
  Retrieves a PDF dictionary object from the scanner stack.
- [func CGPDFScannerPopStream(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](./cgpdfscannerpopstream%28_,_%29.md)
  Retrieves a PDF stream object from the scanner stack.
### Data Types
- [typealias CGPDFScannerRef](./cgpdfscannerref.md)
  A type used to parse a PDF content stream.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscanner)*