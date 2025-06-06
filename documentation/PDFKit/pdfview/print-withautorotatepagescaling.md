# print(with:autoRotate:pageScaling:)

**Framework**: PDFKit  
**Kind**: method

Prints the document with the specified printer and page-scaling information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func print(with printInfo: NSPrintInfo, autoRotate doRotate: Bool, pageScaling scale: PDFPrintScalingMode)
```

#### Discussion

If `pageScaling` is set to `kPDFPrintPageScaleToFit`, each page is scaled up or down to best fit the paper size. If `pageScaling` is set to `kPDFPrintPageScaleDownToFit`, only large pages are scaled down to fit; small pages are not scaled up to fit. Specifying `kPDFPrintPageScaleNone` for `pageScaling` is equivalent to calling [`print(with:autoRotate:)`](pdfview/print(with:autorotate:).md). See PDFDocument for more information on page-scaling types.

## See Also

- [func draw(PDFPage)](pdfview/draw(_:).md)
  Draw and render a visible page.
- [func drawPagePost(PDFPage)](pdfview/drawpagepost(_:).md)
  Perform post-page rendering.
- [func print(with: NSPrintInfo, autoRotate: Bool)](pdfview/print(with:autorotate:).md)
  Prints the document with the specified printer information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/print(with:autorotate:pagescaling:))*