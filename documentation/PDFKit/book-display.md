# Book Display

**Framework**: PDFKit

Operations to setup a book display for a PDF view.

## Topics

### Displaying as Book
- [var displaysAsBook: Bool](pdfview/displaysasbook.md)
  A Boolean value indicating whether the view will display the first page as a book cover (meaningful only when the document is in two-up or two-up continuous display mode).
- [var isUsingPageViewController: Bool](pdfview/isusingpageviewcontroller.md)
  A Boolean value indicating whether the scroll view is using a `UIPageViewController`.
- [func usePageViewController(Bool, withViewOptions: [AnyHashable : Any]?)](pdfview/usepageviewcontroller(_:withviewoptions:).md)
  Changes the scroll view to use a `UIPageViewController` to layout and navigate pages.

## See Also

- [var displayMode: PDFDisplayMode](pdfview/displaymode.md)
  The current display mode.
- [enum PDFDisplayMode](pdfdisplaymode.md)
  A wrapper for the chosen display mode constant.
- [Additional Display Configurations](additional-display-configurations.md)
  Operations for setting up page breaks, a display box, and display direction.
- [Graphics Properties](graphics-properties.md)
  Operations to define the background color, antialiasing, and greeking for a PDF view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/book-display)*