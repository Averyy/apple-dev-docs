# isUsingPageViewController

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the scroll view is using a `UIPageViewController`.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isUsingPageViewController: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isUsingPageViewController;
```

## See Also

### Displaying as Book
- [var displaysAsBook: Bool](./displaysasbook.md)
  A Boolean value indicating whether the view will display the first page as a book cover (meaningful only when the document is in two-up or two-up continuous display mode).
- [func usePageViewController(Bool, withViewOptions: [AnyHashable : Any]?)](./usepageviewcontroller%28_,withviewoptions%29.md)
  Changes the scroll view to use a `UIPageViewController` to layout and navigate pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/isusingpageviewcontroller)*