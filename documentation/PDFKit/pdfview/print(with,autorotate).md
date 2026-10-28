# print(with:autoRotate:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Prints the document with the specified printer information.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func print(with printInfo: NSPrintInfo, autoRotate doRotate: Bool)
```

```objc
- (void) printWithInfo:(NSPrintInfo *) printInfo autoRotate:(BOOL) doRotate;
```

## Discussion

If `autoRotate` is set to [`true`](../../Swift/true.md), then ths method ignores the orientation attribute in the `NSPrintInfo` object and instead chooses the orientation that best fits the page to the paper size. This orientation occurs on a page-by-page basis.

## See Also

### Rendering the View and Printing
- [func draw(PDFPage)](./draw%28_%29.md)
  Draw and render a visible page.
- [func drawPagePost(PDFPage)](./drawpagepost%28_%29.md)
  Perform post-page rendering.
- [func print(with: NSPrintInfo, autoRotate: Bool, pageScaling: PDFPrintScalingMode)](./print%28with,autorotate,pagescaling%29.md)
  Prints the document with the specified printer and page-scaling information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/print(with:autorotate:))*