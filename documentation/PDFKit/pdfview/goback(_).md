# goBack(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

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
func goBack(_ sender: Any?)
```

```objc
- (void) goBack:(id) sender;
```

## Discussion

The page history gets built as your application calls navigation methods such as [`go(to:)`](./go%28to%29-5lh5d.md) and [`goToLastPage(_:)`](./gotolastpage%28_%29.md).

## See Also

### Related Documentation
- [var canGoBack: Bool](./cangoback.md)
  Returns a Boolean value indicating whether the user can navigate to the previous page in the page history.
### Navigating History for a Document
- [func goForward(Any?)](./goforward%28_%29.md)
  Navigates forward one step in the page history.
- [func goToFirstPage(Any?)](./gotofirstpage%28_%29.md)
  Navigates to the first page of the document.
- [func goToLastPage(Any?)](./gotolastpage%28_%29.md)
  Navigates to the last page of the document.
- [func goToNextPage(Any?)](./gotonextpage%28_%29.md)
  Navigates to the next page of the document.
- [func goToPreviousPage(Any?)](./gotopreviouspage%28_%29.md)
  Navigates to the previous page of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/goback(_:))*