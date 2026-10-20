# PDFPrintScalingMode

**Framework**: PDFKit  
**Kind**: enum  
**Role**: Enumeration

The type of scaling to be used when printing a page (see [`PDFDocument`](./pdfdocument.md)).

**Availability**:
- macOS 10.4+

## Declaration

```swift
enum PDFPrintScalingMode
```

```c
enum PDFPrintScalingMode : NSInteger;
```

## Topics

### Enumeration Cases
- [PDFPrintScalingMode.pageScaleDownToFit](./pdfprintscalingmode/pagescaledowntofit.md)
  Scale large pages down to fit the paper size (smaller pages do not get scaled up).
- [PDFPrintScalingMode.pageScaleNone](./pdfprintscalingmode/pagescalenone.md)
  Do not apply scaling to the page when printing.
- [PDFPrintScalingMode.pageScaleToFit](./pdfprintscalingmode/pagescaletofit.md)
  Scale each page up or down to best fit the paper size.
### Initializers
- [init?(rawValue: Int)](./pdfprintscalingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Printing Documents for macOS
- [func printOperation(for: NSPrintInfo?, scalingMode: PDFPrintScalingMode, autoRotate: Bool) -> NSPrintOperation?](./pdfdocument/printoperation%28for,scalingmode,autorotate%29.md)
  Returns a print operation suitable for printing the PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfprintscalingmode)*