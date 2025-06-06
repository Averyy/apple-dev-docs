# isUsingPageViewController

**Framework**: PDFKit  
**Kind**: property

A Boolean value indicating whether the scroll view is using a `UIPageViewController`.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isUsingPageViewController: Bool { get }
```

## See Also

- [var displaysAsBook: Bool](pdfview/displaysasbook.md)
  A Boolean value indicating whether the view will display the first page as a book cover (meaningful only when the document is in two-up or two-up continuous display mode).
- [func usePageViewController(Bool, withViewOptions: [AnyHashable : Any]?)](pdfview/usepageviewcontroller(_:withviewoptions:).md)
  Changes the scroll view to use a `UIPageViewController` to layout and navigate pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/isusingpageviewcontroller)*