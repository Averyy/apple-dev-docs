# Zoom Operations

**Framework**: PDFKit

Zoom operations for a PDF View.

## Topics

### Zooming in a PDF View
- [func zoomIn(Any?)](pdfview/zoomin(_:).md)
  Zooms in by increasing the scaling factor.
- [var canZoomIn: Bool](pdfview/canzoomin.md)
  Returns a Boolean value indicating whether the user can magnify the view and zoom in.
- [func zoomOut(Any?)](pdfview/zoomout(_:).md)
  Zooms out by decreasing the scaling factor.
- [var canZoomOut: Bool](pdfview/canzoomout.md)
  Returns a Boolean value indicating whether the user can view an expanded area and zoom out.

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
- [func rowSize(for: PDFPage) -> CGSize](pdfview/rowsize(for:).md)
  Returns the size needed to display a row of the current document page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/zoom-operations)*