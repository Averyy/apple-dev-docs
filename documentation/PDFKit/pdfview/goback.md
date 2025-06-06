# goBack(_:)

**Framework**: PDFKit  
**Kind**: method

Navigates back one step in the page history.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@IBAction
@MainActor func goBack(_ sender: Any?)
```

#### Discussion

The page history gets built as your application calls navigation methods such as [`go(to:)`](pdfview/go(to:)-5lh5d.md) and [`goToLastPage(_:)`](pdfview/gotolastpage(_:).md).

## See Also

- [var canGoBack: Bool](pdfview/cangoback.md)
  Returns a Boolean value indicating whether the user can navigate to the previous page in the page history.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/goback(_:))*