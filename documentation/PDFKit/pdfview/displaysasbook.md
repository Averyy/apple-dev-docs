# displaysAsBook

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view will display the first page as a book cover (meaningful only when the document is in two-up or two-up continuous display mode).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var displaysAsBook: Bool { get set }
```

```objc
@property (nonatomic) BOOL displaysAsBook;
```

## See Also

### Displaying as Book
- [var isUsingPageViewController: Bool](./isusingpageviewcontroller.md)
  A Boolean value indicating whether the scroll view is using a `UIPageViewController`.
- [func usePageViewController(Bool, withViewOptions: [AnyHashable : Any]?)](./usepageviewcontroller%28_,withviewoptions%29.md)
  Changes the scroll view to use a `UIPageViewController` to layout and navigate pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/displaysasbook)*