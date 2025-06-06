# Navigation

**Framework**: PDFKit

Operations for moving through page history and seeking to a page in a document.

## Topics

### Determining Valid History Operations
- [var canGoBack: Bool](pdfview/cangoback.md)
  Returns a Boolean value indicating whether the user can navigate to the previous page in the page history.
- [var canGoForward: Bool](pdfview/cangoforward.md)
  Returns a Boolean value indicating whether the user can navigate to the next page in the page history.
- [var canGoToFirstPage: Bool](pdfview/cangotofirstpage.md)
  Returns a Boolean value indicating whether the user can navigate to the first page of the document.
- [var canGoToLastPage: Bool](pdfview/cangotolastpage.md)
  Returns a Boolean value indicating whether the user can navigate to the last page of the document.
- [var canGoToNextPage: Bool](pdfview/cangotonextpage.md)
  Returns a Boolean value indicating whether the user can navigate to the next page of the document.
- [var canGoToPreviousPage: Bool](pdfview/cangotopreviouspage.md)
  Returns a Boolean value indicating whether the user can navigate to the previous page of the document.
### Navigating History for a Document
- [func goBack(Any?)](pdfview/goback(_:).md)
  Navigates back one step in the page history.
- [func goForward(Any?)](pdfview/goforward(_:).md)
  Navigates forward one step in the page history.
- [func goToFirstPage(Any?)](pdfview/gotofirstpage(_:).md)
  Navigates to the first page of the document.
- [func goToLastPage(Any?)](pdfview/gotolastpage(_:).md)
  Navigates to the last page of the document.
- [func goToNextPage(Any?)](pdfview/gotonextpage(_:).md)
  Navigates to the next page of the document.
- [func goToPreviousPage(Any?)](pdfview/gotopreviouspage(_:).md)
  Navigates to the previous page of the document.
### Using Seek in a Document
- [func go(to: PDFPage)](pdfview/go(to:)-6x8y2.md)
  Scrolls to the specified page.
- [func go(to: PDFDestination)](pdfview/go(to:)-5lh5d.md)
  Navigates to the specified destination.
- [func go(to: PDFSelection)](pdfview/go(to:)-3t5go.md)
  Scrolls to the first character of the specified selection.
- [func go(to: CGRect, on: PDFPage)](pdfview/go(to:on:).md)
  Navigates to the specified rectangle on the specified page.

## See Also

- [var currentPage: PDFPage?](pdfview/currentpage.md)
  Returns the current page.
- [var currentDestination: PDFDestination?](pdfview/currentdestination.md)
  Returns a `PDFDestination` object representing the current page and the current point in the view specified in page space.
- [var visiblePages: [PDFPage]](pdfview/visiblepages.md)
  Returns an array of `PDFPage` objects that represent the currently visible pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/navigation)*