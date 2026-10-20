# hidesForSinglePage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the page control is hidden when there is only one page.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var hidesForSinglePage: Bool { get set }
```

```objc
@property (nonatomic) BOOL hidesForSinglePage;
```

#### Discussion

Assign a value of [`true`](../../Swift/true.md) to hide the page control when there is only one page; assign [`false`](../../Swift/false.md) (the default) to show the page control if there is only one page.

## See Also

### Managing pages
- [var currentPage: Int](./currentpage.md)
  The current page, shown by the page control as a white dot.
- [var numberOfPages: Int](./numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var defersCurrentPageDisplay: Bool](./deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.
- [func updateCurrentPageDisplay()](./updatecurrentpagedisplay%28%29.md)
  Updates the page indicator to the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/hidesforsinglepage)*