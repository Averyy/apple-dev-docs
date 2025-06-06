# updateCurrentPageDisplay()

**Framework**: UIKit  
**Kind**: method

Updates the page indicator to the current page.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateCurrentPageDisplay()
```

#### Discussion

This method updates the page indicator so that the current page (the white dot) matches the value returned from [`currentPage`](uipagecontrol/currentpage.md). The class ignores this method if the value of [`defersCurrentPageDisplay`](uipagecontrol/deferscurrentpagedisplay.md) is [`false`](https://developer.apple.com/documentation/swift/false). Setting the [`currentPage`](uipagecontrol/currentpage.md) value directly updates the indicator immediately.

## See Also

- [var currentPage: Int](uipagecontrol/currentpage.md)
  The current page, shown by the page control as a white dot.
- [var numberOfPages: Int](uipagecontrol/numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var hidesForSinglePage: Bool](uipagecontrol/hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [var defersCurrentPageDisplay: Bool](uipagecontrol/deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/updatecurrentpagedisplay())*