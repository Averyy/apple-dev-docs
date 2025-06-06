# canGoToFirstPage

**Framework**: PDFKit  
**Kind**: property

Returns a Boolean value indicating whether the user can navigate to the first page of the document.

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
var canGoToFirstPage: Bool { get }
```

#### Discussion

The return value will be [`true`](https://developer.apple.com/documentation/swift/true) unless the view is already displaying the first page.

## See Also

- [func goToFirstPage(Any?)](pdfview/gotofirstpage(_:).md)
  Navigates to the first page of the document.
- [var canGoBack: Bool](pdfview/cangoback.md)
  Returns a Boolean value indicating whether the user can navigate to the previous page in the page history.
- [var canGoForward: Bool](pdfview/cangoforward.md)
  Returns a Boolean value indicating whether the user can navigate to the next page in the page history.
- [var canGoToLastPage: Bool](pdfview/cangotolastpage.md)
  Returns a Boolean value indicating whether the user can navigate to the last page of the document.
- [var canGoToNextPage: Bool](pdfview/cangotonextpage.md)
  Returns a Boolean value indicating whether the user can navigate to the next page of the document.
- [var canGoToPreviousPage: Bool](pdfview/cangotopreviouspage.md)
  Returns a Boolean value indicating whether the user can navigate to the previous page of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/cangotofirstpage)*