# scaleFactor

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The current scale factor for the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var scaleFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat scaleFactor;
```

## See Also

### Scaling the View
- [var scaleFactorForSizeToFit: CGFloat](./scalefactorforsizetofit.md)
  The “size to fit” scale factor that `autoScales` would use for scaling the current document and layout.
- [var maxScaleFactor: CGFloat](./maxscalefactor.md)
  The maximum scaling factor for the PDF document.
- [var minScaleFactor: CGFloat](./minscalefactor.md)
  The minimum scaling factor for the PDF document.
- [var autoScales: Bool](./autoscales.md)
  A Boolean value indicating whether autoscaling is set.
- [func rowSize(for: PDFPage) -> CGSize](./rowsize%28for%29.md)
  Returns the size needed to display a row of the current document page.
- [Zoom Operations](../zoom-operations.md)
  Zoom operations for a PDF View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/scalefactor)*