# drawPagePost(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Perform post-page rendering.

**Availability**:
- macOS 10.5+ - Deprecated in 10.12

## Declaration

```swift
func drawPagePost(_ page: PDFPage)
```

```objc
- (void) drawPagePost:(PDFPage *) page;
```

## Discussion

The default implementation of this method draws the text highlighting (if any) for the page. This method does not apply scaling or rotating to the current context to map to page space; instead, the context is in view-space coordinates (in which the origin is at the lower-left corner of the current PDF view).

## See Also

### Rendering the View and Printing
- [func draw(PDFPage)](./draw%28_%29.md)
  Draw and render a visible page.
- [func print(with: NSPrintInfo, autoRotate: Bool)](./print%28with,autorotate%29.md)
  Prints the document with the specified printer information.
- [func print(with: NSPrintInfo, autoRotate: Bool, pageScaling: PDFPrintScalingMode)](./print%28with,autorotate,pagescaling%29.md)
  Prints the document with the specified printer and page-scaling information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/drawpagepost(_:))*