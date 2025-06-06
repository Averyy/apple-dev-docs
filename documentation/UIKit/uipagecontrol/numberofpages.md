# numberOfPages

**Framework**: UIKit  
**Kind**: property

The number of pages the receiver shows (as dots).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var numberOfPages: Int { get set }
```

#### Discussion

The value of the property is the number of pages for the page control to show as dots. The default value is 0.

## See Also

- [var currentPage: Int](uipagecontrol/currentpage.md)
  The current page, shown by the page control as a white dot.
- [var hidesForSinglePage: Bool](uipagecontrol/hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [var defersCurrentPageDisplay: Bool](uipagecontrol/deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.
- [func updateCurrentPageDisplay()](uipagecontrol/updatecurrentpagedisplay.md)
  Updates the page indicator to the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/numberofpages)*