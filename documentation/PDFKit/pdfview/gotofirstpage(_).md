# goToFirstPage(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Navigates to the first page of the document.

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
func goToFirstPage(_ sender: Any?)
```

```objc
- (void) goToFirstPage:(id) sender;
```

## Discussion

PDF Kit records the move in its page history.

## See Also

### Related Documentation
- [var canGoToFirstPage: Bool](./cangotofirstpage.md)
  Returns a Boolean value indicating whether the user can navigate to the first page of the document.
### Navigating History for a Document
- [func goBack(Any?)](./goback%28_%29.md)
  Navigates back one step in the page history.
- [func goForward(Any?)](./goforward%28_%29.md)
  Navigates forward one step in the page history.
- [func goToLastPage(Any?)](./gotolastpage%28_%29.md)
  Navigates to the last page of the document.
- [func goToNextPage(Any?)](./gotonextpage%28_%29.md)
  Navigates to the next page of the document.
- [func goToPreviousPage(Any?)](./gotopreviouspage%28_%29.md)
  Navigates to the previous page of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/gotofirstpage(_:))*