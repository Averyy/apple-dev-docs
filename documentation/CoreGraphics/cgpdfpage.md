# CGPDFPage

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A type that represents a page in a PDF document.

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
class CGPDFPage
```

```c
typedef struct CGPDFPage * CGPDFPageRef;
```

## Topics

### Getting Page Information
- [func getBoxRect(CGPDFBox) -> CGRect](./cgpdfpage/getboxrect%28_%29.md)
  Returns the rectangle that represents a type of box for a content region or page dimensions of a PDF page.
- [var dictionary: CGPDFDictionaryRef?](./cgpdfpage/dictionary.md)
  Returns the dictionary of a PDF page.
- [var document: CGPDFDocument?](./cgpdfpage/document.md)
  Returns the document for a page.
- [var pageNumber: Int](./cgpdfpage/pagenumber.md)
  Returns the page number of the specified PDF page.
- [var rotationAngle: Int32](./cgpdfpage/rotationangle.md)
  Returns the rotation angle of a PDF page, in degrees.
- [func getDrawingTransform(CGPDFBox, rect: CGRect, rotate: Int32, preserveAspectRatio: Bool) -> CGAffineTransform](./cgpdfpage/getdrawingtransform%28_,rect,rotate,preserveaspectratio%29.md)
  Returns the affine transform that maps a box to a given rectangle on a PDF page.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgpdfpage/typeid.md)
  Returns the CFType ID for PDF page objects.
### Constants
- [enum CGPDFBox](./cgpdfbox.md)
  Box types for a PDF page.
### Retaining and Releasing a PDF Page
- [CGPDFPageRetain](./cgpdfpageretain.md)
  Increments the retain count of a PDF page.
- [CGPDFPageRelease](./cgpdfpagerelease.md)
  Decrements the retain count of a PDF page.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfpage)*