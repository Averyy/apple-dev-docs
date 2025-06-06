# document

**Framework**: Core Graphics  
**Kind**: property

Returns the document for a page.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var document: CGPDFDocument? { get }
```

## See Also

- [func getBoxRect(CGPDFBox) -> CGRect](cgpdfpage/getboxrect(_:).md)
  Returns the rectangle that represents a type of box for a content region or page dimensions of a PDF page.
- [var dictionary: CGPDFDictionaryRef?](cgpdfpage/dictionary.md)
  Returns the dictionary of a PDF page.
- [var pageNumber: Int](cgpdfpage/pagenumber.md)
  Returns the page number of the specified PDF page.
- [var rotationAngle: Int32](cgpdfpage/rotationangle.md)
  Returns the rotation angle of a PDF page, in degrees.
- [func getDrawingTransform(CGPDFBox, rect: CGRect, rotate: Int32, preserveAspectRatio: Bool) -> CGAffineTransform](cgpdfpage/getdrawingtransform(_:rect:rotate:preserveaspectratio:).md)
  Returns the affine transform that maps a box to a given rectangle on a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfpage/document)*