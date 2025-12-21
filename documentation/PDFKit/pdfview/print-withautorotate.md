# print(with:autoRotate:)

**Framework**: PDFKit  
**Kind**: method

Prints the document with the specified printer information.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func print(with printInfo: NSPrintInfo, autoRotate doRotate: Bool)
```

#### Discussion

If `autoRotate` is set to [`true`](https://developer.apple.com/documentation/Swift/true), then ths method ignores the orientation attribute in the `NSPrintInfo` object and instead chooses the orientation that best fits the page to the paper size. This orientation occurs on a page-by-page basis.

## See Also

- [func draw(PDFPage)](pdfview/draw(_:).md)
  Draw and render a visible page.
- [func drawPagePost(PDFPage)](pdfview/drawpagepost(_:).md)
  Perform post-page rendering.
- [func print(with: NSPrintInfo, autoRotate: Bool, pageScaling: PDFPrintScalingMode)](pdfview/print(with:autorotate:pagescaling:).md)
  Prints the document with the specified printer and page-scaling information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/print(with:autorotate:))*