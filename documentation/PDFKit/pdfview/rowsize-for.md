# rowSize(for:)

**Framework**: PDFKit  
**Kind**: method

Returns the size needed to display a row of the current document page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func rowSize(for page: PDFPage) -> CGSize
```

#### Discussion

The size is dependent on the current scale factor and display attributes.

## See Also

- [var scaleFactor: CGFloat](pdfview/scalefactor.md)
  The current scale factor for the view.
- [var scaleFactorForSizeToFit: CGFloat](pdfview/scalefactorforsizetofit.md)
  The “size to fit” scale factor that `autoScales` would use for scaling the current document and layout.
- [var maxScaleFactor: CGFloat](pdfview/maxscalefactor.md)
  The maximum scaling factor for the PDF document.
- [var minScaleFactor: CGFloat](pdfview/minscalefactor.md)
  The minimum scaling factor for the PDF document.
- [var autoScales: Bool](pdfview/autoscales.md)
  A Boolean value indicating whether autoscaling is set.
- [Zoom Operations](zoom-operations.md)
  Zoom operations for a PDF View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/rowsize(for:))*