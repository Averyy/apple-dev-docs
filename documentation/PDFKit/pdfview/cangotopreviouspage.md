# canGoToPreviousPage

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether the user can navigate to the previous page of the document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var canGoToPreviousPage: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canGoToPreviousPage;
```

#### Discussion

The return value will be [`true`](../../Swift/true.md) unless the view is displaying the first page.

## See Also

### Determining Valid History Operations
- [var canGoBack: Bool](./cangoback.md)
  Returns a Boolean value indicating whether the user can navigate to the previous page in the page history.
- [var canGoForward: Bool](./cangoforward.md)
  Returns a Boolean value indicating whether the user can navigate to the next page in the page history.
- [var canGoToFirstPage: Bool](./cangotofirstpage.md)
  Returns a Boolean value indicating whether the user can navigate to the first page of the document.
- [var canGoToLastPage: Bool](./cangotolastpage.md)
  Returns a Boolean value indicating whether the user can navigate to the last page of the document.
- [var canGoToNextPage: Bool](./cangotonextpage.md)
  Returns a Boolean value indicating whether the user can navigate to the next page of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/cangotopreviouspage)*