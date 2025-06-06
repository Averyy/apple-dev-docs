# transformContext(for:)

**Framework**: PDFKit  
**Kind**: method

Transforms the current context, given the specified box.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func transformContext(for box: PDFDisplayBox)
```

#### Discussion

When transforming the current context, this method takes into account the rotation of the page, as well as the origin of the box with respect to the page’s base coordinate system. This is a convenient method to call within the `PDFView` [`draw(_:)`](pdfview/draw(_:).md) method or from within a draw method of a `PDFAnnotation` subclass.

## See Also

- [class PDFPage](pdfpage.md)
  `PDFPage`, a subclass of `NSObject`, defines methods used to render PDF pages and work with annotations, text, and selections.
- [func draw(with: PDFDisplayBox)](pdfpage/draw(with:).md)
  Draws the page within the specified box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/transformcontext(for:))*