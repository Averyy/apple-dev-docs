# Configurations

**Framework**: PDFKit

Define display modes, scaling, rendering, printing and graphics properties.

## Topics

### Working with Display Modes and Characteristics
- [var displayMode: PDFDisplayMode](pdfview/displaymode.md)
  The current display mode.
- [enum PDFDisplayMode](pdfdisplaymode.md)
  A wrapper for the chosen display mode constant.
- [Additional Display Configurations](additional-display-configurations.md)
  Operations for setting up page breaks, a display box, and display direction.
- [Book Display](book-display.md)
  Operations to setup a book display for a PDF view.
- [Graphics Properties](graphics-properties.md)
  Operations to define the background color, antialiasing, and greeking for a PDF view.
### Scaling the View
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
- [Zoom Operations](zoom-operations.md)
  Zoom operations for a PDF View.
### Rendering the View and Printing
- [func draw(PDFPage)](pdfview/draw(_:).md)
  Draw and render a visible page.
- [func drawPagePost(PDFPage)](pdfview/drawpagepost(_:).md)
  Perform post-page rendering.
- [func print(with: NSPrintInfo, autoRotate: Bool)](pdfview/print(with:autorotate:).md)
  Prints the document with the specified printer information.
- [func print(with: NSPrintInfo, autoRotate: Bool, pageScaling: PDFPrintScalingMode)](pdfview/print(with:autorotate:pagescaling:).md)
  Prints the document with the specified printer and page-scaling information.
### Specializing the View
- [var documentView: UIView?](pdfview/documentview.md)
  The innermost view used by `PDFView` or by your `PDFView` subclass.
- [func layoutDocumentView()](pdfview/layoutdocumentview.md)
  Performs layout of the inner views.
- [Draw Operations](draw-operations.md)
  Draw in a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/configurations)*