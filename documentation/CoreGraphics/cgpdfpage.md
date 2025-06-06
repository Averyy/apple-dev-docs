# CGPDFPage

**Framework**: Core Graphics  
**Kind**: class

A type that represents a page in a PDF document.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGPDFPage
```

## Topics

### Getting Page Information
- [func getBoxRect(CGPDFBox) -> CGRect](cgpdfpage/getboxrect(_:).md)
  Returns the rectangle that represents a type of box for a content region or page dimensions of a PDF page.
- [var dictionary: CGPDFDictionaryRef?](cgpdfpage/dictionary.md)
  Returns the dictionary of a PDF page.
- [var document: CGPDFDocument?](cgpdfpage/document.md)
  Returns the document for a page.
- [var pageNumber: Int](cgpdfpage/pagenumber.md)
  Returns the page number of the specified PDF page.
- [var rotationAngle: Int32](cgpdfpage/rotationangle.md)
  Returns the rotation angle of a PDF page, in degrees.
- [func getDrawingTransform(CGPDFBox, rect: CGRect, rotate: Int32, preserveAspectRatio: Bool) -> CGAffineTransform](cgpdfpage/getdrawingtransform(_:rect:rotate:preserveaspectratio:).md)
  Returns the affine transform that maps a box to a given rectangle on a PDF page.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgpdfpage/typeid.md)
  Returns the CFType ID for PDF page objects.
### Constants
- [enum CGPDFBox](cgpdfbox.md)
  Box types for a PDF page.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfpage)*