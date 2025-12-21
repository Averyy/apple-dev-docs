# hidesForSinglePage

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether the page control is hidden when there is only one page.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hidesForSinglePage: Bool { get set }
```

#### Discussion

Assign a value of [`true`](https://developer.apple.com/documentation/Swift/true) to hide the page control when there is only one page; assign [`false`](https://developer.apple.com/documentation/Swift/false) (the default) to show the page control if there is only one page.

## See Also

- [var currentPage: Int](uipagecontrol/currentpage.md)
  The current page, shown by the page control as a white dot.
- [var numberOfPages: Int](uipagecontrol/numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var defersCurrentPageDisplay: Bool](uipagecontrol/deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.
- [func updateCurrentPageDisplay()](uipagecontrol/updatecurrentpagedisplay.md)
  Updates the page indicator to the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/hidesforsinglepage)*