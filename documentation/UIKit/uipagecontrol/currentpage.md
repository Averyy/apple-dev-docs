# currentPage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current page, shown by the page control as a white dot.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var currentPage: Int { get set }
```

```objc
@property (nonatomic, assign) NSInteger currentPage;
```

#### Discussion

The property value is an integer specifying the current page shown minus one; thus a value of zero (the default) indicates the first page. A page control shows the current page as a white dot. Values outside the possible range are pinned to either 0 or [`numberOfPages`](./numberofpages.md) minus 1.

## See Also

### Managing pages
- [var numberOfPages: Int](./numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var hidesForSinglePage: Bool](./hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [var defersCurrentPageDisplay: Bool](./deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.
- [func updateCurrentPageDisplay()](./updatecurrentpagedisplay%28%29.md)
  Updates the page indicator to the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/currentpage)*