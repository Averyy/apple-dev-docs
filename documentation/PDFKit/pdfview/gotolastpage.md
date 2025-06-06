# goToLastPage(_:)

**Framework**: PDFKit  
**Kind**: method

Navigates to the last page of the document.

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
@MainActor func goToLastPage(_ sender: Any?)
```

#### Discussion

PDF Kit records the move in its page history.

## See Also

- [var canGoToLastPage: Bool](pdfview/cangotolastpage.md)
  Returns a Boolean value indicating whether the user can navigate to the last page of the document.
- [func goBack(Any?)](pdfview/goback(_:).md)
  Navigates back one step in the page history.
- [func goForward(Any?)](pdfview/goforward(_:).md)
  Navigates forward one step in the page history.
- [func goToFirstPage(Any?)](pdfview/gotofirstpage(_:).md)
  Navigates to the first page of the document.
- [func goToNextPage(Any?)](pdfview/gotonextpage(_:).md)
  Navigates to the next page of the document.
- [func goToPreviousPage(Any?)](pdfview/gotopreviouspage(_:).md)
  Navigates to the previous page of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/gotolastpage(_:))*