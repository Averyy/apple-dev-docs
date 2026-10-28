# print(with:autoRotate:pageScaling:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Prints the document with the specified printer and page-scaling information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func print(with printInfo: NSPrintInfo, autoRotate doRotate: Bool, pageScaling scale: PDFPrintScalingMode)
```

```objc
- (void) printWithInfo:(NSPrintInfo *) printInfo autoRotate:(BOOL) doRotate pageScaling:(PDFPrintScalingMode) scale;
```

## Discussion

If `pageScaling` is set to `kPDFPrintPageScaleToFit`, each page is scaled up or down to best fit the paper size. If `pageScaling` is set to `kPDFPrintPageScaleDownToFit`, only large pages are scaled down to fit; small pages are not scaled up to fit. Specifying `kPDFPrintPageScaleNone` for `pageScaling` is equivalent to calling [`print(with:autoRotate:)`](./print%28with,autorotate%29.md). See PDFDocument for more information on page-scaling types.

## See Also

### Rendering the View and Printing
- [func draw(PDFPage)](./draw%28_%29.md)
  Draw and render a visible page.
- [func drawPagePost(PDFPage)](./drawpagepost%28_%29.md)
  Perform post-page rendering.
- [func print(with: NSPrintInfo, autoRotate: Bool)](./print%28with,autorotate%29.md)
  Prints the document with the specified printer information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/print(with:autorotate:pagescaling:))*