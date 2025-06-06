# drawPagePost(_:)

**Framework**: PDFKit  
**Kind**: method

Perform post-page rendering.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func drawPagePost(_ page: PDFPage)
```

#### Discussion

The default implementation of this method draws the text highlighting (if any) for the page. This method does not apply scaling or rotating to the current context to map to page space; instead, the context is in view-space coordinates (in which the origin is at the lower-left corner of the current PDF view).

## See Also

- [func draw(PDFPage)](pdfview/draw(_:).md)
  Draw and render a visible page.
- [func print(with: NSPrintInfo, autoRotate: Bool)](pdfview/print(with:autorotate:).md)
  Prints the document with the specified printer information.
- [func print(with: NSPrintInfo, autoRotate: Bool, pageScaling: PDFPrintScalingMode)](pdfview/print(with:autorotate:pagescaling:).md)
  Prints the document with the specified printer and page-scaling information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/drawpagepost(_:))*