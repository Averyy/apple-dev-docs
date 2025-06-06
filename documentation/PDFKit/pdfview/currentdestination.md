# currentDestination

**Framework**: PDFKit  
**Kind**: property

Returns a `PDFDestination` object representing the current page and the current point in the view specified in page space.

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
var currentDestination: PDFDestination? { get }
```

#### Discussion

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

- [func go(to: PDFDestination)](pdfview/go(to:)-5lh5d.md)
  Navigates to the specified destination.
- [var currentPage: PDFPage?](pdfview/currentpage.md)
  Returns the current page.
- [var visiblePages: [PDFPage]](pdfview/visiblepages.md)
  Returns an array of `PDFPage` objects that represent the currently visible pages.
- [Navigation](navigation.md)
  Operations for moving through page history and seeking to a page in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/currentdestination)*