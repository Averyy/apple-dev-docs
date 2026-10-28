# draw(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Draw and render a visible page.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func draw(_ page: PDFPage)
```

```objc
- (void) drawPage:(PDFPage *) page;
```

## Discussion

Do not invoke this method, except by invoking it on `super` from a subclass.

The `PDFView` class calls [`draw(_:)`](./draw%28_%29.md) as necessary for each visible page that requires rendering. In the `PDFView` class, this method erases `page` to white, calls `[page drawInRect: pageRect withBox: [self displayBox]]` , and then draws the selection, if any.

You can override this method to draw on top of a PDF page or to control how pages are drawn. In these cases, invoke this method on `super` and then perform custom drawing on top of the PDF page.

## See Also

### Rendering the View and Printing
- [func drawPagePost(PDFPage)](./drawpagepost%28_%29.md)
  Perform post-page rendering.
- [func print(with: NSPrintInfo, autoRotate: Bool)](./print%28with,autorotate%29.md)
  Prints the document with the specified printer information.
- [func print(with: NSPrintInfo, autoRotate: Bool, pageScaling: PDFPrintScalingMode)](./print%28with,autorotate,pagescaling%29.md)
  Prints the document with the specified printer and page-scaling information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/draw(_:))*