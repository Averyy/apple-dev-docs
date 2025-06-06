# usePageViewController(_:withViewOptions:)

**Framework**: PDFKit  
**Kind**: method

Changes the scroll view to use a `UIPageViewController` to layout and navigate pages.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func usePageViewController(_ enable: Bool, withViewOptions viewOptions: [AnyHashable : Any]? = nil)
```

## See Also

- [var displaysAsBook: Bool](pdfview/displaysasbook.md)
  A Boolean value indicating whether the view will display the first page as a book cover (meaningful only when the document is in two-up or two-up continuous display mode).
- [var isUsingPageViewController: Bool](pdfview/isusingpageviewcontroller.md)
  A Boolean value indicating whether the scroll view is using a `UIPageViewController`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/usepageviewcontroller(_:withviewoptions:))*