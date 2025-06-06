# currentPage

**Framework**: PDFKit  
**Kind**: property

Returns the current page.

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
var currentPage: PDFPage? { get }
```

#### Discussion

When there are two pages in the view in a two-up mode, “current page” is the left page. For continuous modes, returns the page crossing a horizontal line halfway between the view’s top and bottom bounds.

## See Also

- [func go(to: PDFDestination)](pdfview/go(to:)-5lh5d.md)
  Navigates to the specified destination.
- [var currentDestination: PDFDestination?](pdfview/currentdestination.md)
  Returns a `PDFDestination` object representing the current page and the current point in the view specified in page space.
- [var visiblePages: [PDFPage]](pdfview/visiblepages.md)
  Returns an array of `PDFPage` objects that represent the currently visible pages.
- [Navigation](navigation.md)
  Operations for moving through page history and seeking to a page in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/currentpage)*