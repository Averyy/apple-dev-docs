# visiblePages

**Framework**: PDFKit  
**Kind**: property

Returns an array of `PDFPage` objects that represent the currently visible pages.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var visiblePages: [PDFPage] { get }
```

## See Also

- [var currentPage: PDFPage?](pdfview/currentpage.md)
  Returns the current page.
- [var currentDestination: PDFDestination?](pdfview/currentdestination.md)
  Returns a `PDFDestination` object representing the current page and the current point in the view specified in page space.
- [Navigation](navigation.md)
  Operations for moving through page history and seeking to a page in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/visiblepages)*