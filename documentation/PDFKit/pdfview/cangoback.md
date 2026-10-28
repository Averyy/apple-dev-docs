# canGoBack

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether the user can navigate to the previous page in the page history.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var canGoBack: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canGoBack;
```

## Discussion

The page history gets built as your application calls navigation methods such as [`go(to:)`](./go%28to%29-5lh5d.md) and [`goToLastPage(_:)`](./gotolastpage%28_%29.md).

## See Also

### Related Documentation
- [func goBack(Any?)](./goback%28_%29.md)
  Navigates back one step in the page history.
### Determining Valid History Operations
- [var canGoForward: Bool](./cangoforward.md)
  Returns a Boolean value indicating whether the user can navigate to the next page in the page history.
- [var canGoToFirstPage: Bool](./cangotofirstpage.md)
  Returns a Boolean value indicating whether the user can navigate to the first page of the document.
- [var canGoToLastPage: Bool](./cangotolastpage.md)
  Returns a Boolean value indicating whether the user can navigate to the last page of the document.
- [var canGoToNextPage: Bool](./cangotonextpage.md)
  Returns a Boolean value indicating whether the user can navigate to the next page of the document.
- [var canGoToPreviousPage: Bool](./cangotopreviouspage.md)
  Returns a Boolean value indicating whether the user can navigate to the previous page of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/cangoback)*