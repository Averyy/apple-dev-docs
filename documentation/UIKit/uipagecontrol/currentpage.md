# currentPage

**Framework**: UIKit  
**Kind**: property

The current page, shown by the page control as a white dot.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var currentPage: Int { get set }
```

#### Discussion

The property value is an integer specifying the current page shown minus one; thus a value of zero (the default) indicates the first page. A page control shows the current page as a white dot. Values outside the possible range are pinned to either 0 or [`numberOfPages`](uipagecontrol/numberofpages.md) minus 1.

## See Also

- [var numberOfPages: Int](uipagecontrol/numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var hidesForSinglePage: Bool](uipagecontrol/hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [var defersCurrentPageDisplay: Bool](uipagecontrol/deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.
- [func updateCurrentPageDisplay()](uipagecontrol/updatecurrentpagedisplay.md)
  Updates the page indicator to the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/currentpage)*