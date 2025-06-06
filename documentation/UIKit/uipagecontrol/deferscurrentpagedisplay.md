# defersCurrentPageDisplay

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls when the current page is displayed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var defersCurrentPageDisplay: Bool { get set }
```

#### Discussion

Set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) so that, when the user taps the control to go to a new page, the class defers updating the page control until it calls [`updateCurrentPageDisplay()`](uipagecontrol/updatecurrentpagedisplay().md). Set the value to [`false`](https://developer.apple.com/documentation/swift/false) (the default) to have the page control updated immediately.

## See Also

- [var currentPage: Int](uipagecontrol/currentpage.md)
  The current page, shown by the page control as a white dot.
- [var numberOfPages: Int](uipagecontrol/numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var hidesForSinglePage: Bool](uipagecontrol/hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [func updateCurrentPageDisplay()](uipagecontrol/updatecurrentpagedisplay.md)
  Updates the page indicator to the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/deferscurrentpagedisplay)*