# maxScaleFactor

**Framework**: PDFKit  
**Kind**: property

The maximum scaling factor for the PDF document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var maxScaleFactor: CGFloat { get set }
```

## See Also

- [var scaleFactor: CGFloat](pdfview/scalefactor.md)
  The current scale factor for the view.
- [var scaleFactorForSizeToFit: CGFloat](pdfview/scalefactorforsizetofit.md)
  The “size to fit” scale factor that `autoScales` would use for scaling the current document and layout.
- [var minScaleFactor: CGFloat](pdfview/minscalefactor.md)
  The minimum scaling factor for the PDF document.
- [var autoScales: Bool](pdfview/autoscales.md)
  A Boolean value indicating whether autoscaling is set.
- [func rowSize(for: PDFPage) -> CGSize](pdfview/rowsize(for:).md)
  Returns the size needed to display a row of the current document page.
- [Zoom Operations](zoom-operations.md)
  Zoom operations for a PDF View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/maxscalefactor)*