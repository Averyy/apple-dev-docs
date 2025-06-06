# PDFPrintScalingMode

**Framework**: PDFKit  
**Kind**: enum

The type of scaling to be used when printing a page (see [`PDFDocument`](pdfdocument.md)).

**Availability**:
- macOS 10.4+

## Declaration

```swift
enum PDFPrintScalingMode
```

## Topics

### Enumeration Cases
- [PDFPrintScalingMode.pageScaleDownToFit](pdfprintscalingmode/pagescaledowntofit.md)
  Scale large pages down to fit the paper size (smaller pages do not get scaled up).
- [PDFPrintScalingMode.pageScaleNone](pdfprintscalingmode/pagescalenone.md)
  Do not apply scaling to the page when printing.
- [PDFPrintScalingMode.pageScaleToFit](pdfprintscalingmode/pagescaletofit.md)
  Scale each page up or down to best fit the paper size.
### Initializers
- [init?(rawValue: Int)](pdfprintscalingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func printOperation(for: NSPrintInfo?, scalingMode: PDFPrintScalingMode, autoRotate: Bool) -> NSPrintOperation?](pdfdocument/printoperation(for:scalingmode:autorotate:).md)
  Returns a print operation suitable for printing the PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfprintscalingmode)*