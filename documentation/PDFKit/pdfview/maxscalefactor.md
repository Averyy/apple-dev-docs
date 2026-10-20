# maxScaleFactor

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

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
var maxScaleFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat maxScaleFactor;
```

## See Also

### Scaling the View
- [var scaleFactor: CGFloat](./scalefactor.md)
  The current scale factor for the view.
- [var scaleFactorForSizeToFit: CGFloat](./scalefactorforsizetofit.md)
  The “size to fit” scale factor that `autoScales` would use for scaling the current document and layout.
- [var minScaleFactor: CGFloat](./minscalefactor.md)
  The minimum scaling factor for the PDF document.
- [var autoScales: Bool](./autoscales.md)
  A Boolean value indicating whether autoscaling is set.
- [func rowSize(for: PDFPage) -> CGSize](./rowsize%28for%29.md)
  Returns the size needed to display a row of the current document page.
- [Zoom Operations](../zoom-operations.md)
  Zoom operations for a PDF View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/maxscalefactor)*