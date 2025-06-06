# Graphics Properties

**Framework**: PDFKit

Operations to define the background color, antialiasing, and greeking for a PDF view.

## Topics

### Setting Background Color
- [func takeBackgroundColorFrom(Any)](pdfview/takebackgroundcolorfrom(_:).md)
  Sets the view’s background color to the specified color.
- [var backgroundColor: UIColor](pdfview/backgroundcolor.md)
  The view’s background color.
### Antialiasing
- [var shouldAntiAlias: Bool](pdfview/shouldantialias.md)
  A Boolean value indicating whether the view is antialiased.
- [var interpolationQuality: PDFInterpolationQuality](pdfview/interpolationquality.md)
  The interpolation quality for images drawn into the `PDFView` context.
- [enum PDFInterpolationQuality](pdfinterpolationquality.md)
  A wrapper for the specified interpolation quality.
### Greeking
- [var greekingThreshold: CGFloat](pdfview/greekingthreshold.md)
  Returns the current greeking threshold for the view.

## See Also

- [var displayMode: PDFDisplayMode](pdfview/displaymode.md)
  The current display mode.
- [enum PDFDisplayMode](pdfdisplaymode.md)
  A wrapper for the chosen display mode constant.
- [Additional Display Configurations](additional-display-configurations.md)
  Operations for setting up page breaks, a display box, and display direction.
- [Book Display](book-display.md)
  Operations to setup a book display for a PDF view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/graphics-properties)*