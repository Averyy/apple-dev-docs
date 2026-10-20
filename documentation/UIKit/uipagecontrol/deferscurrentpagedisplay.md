# defersCurrentPageDisplay

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls when the current page is displayed.

**Availability**:
- iOS 2.0+ - Deprecated in 14.0
- iPadOS 2.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- tvOS - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: The system no longer supports this property.

## Declaration

```swift
var defersCurrentPageDisplay: Bool { get set }
```

```objc
@property (nonatomic) BOOL defersCurrentPageDisplay;
```

#### Discussion

Set the value of this property to [`true`](../../Swift/true.md) so that, when the user taps the control to go to a new page, the class defers updating the page control until it calls [`updateCurrentPageDisplay()`](./updatecurrentpagedisplay%28%29.md). Set the value to [`false`](../../Swift/false.md) (the default) to have the page control updated immediately.

## See Also

### Managing pages
- [var currentPage: Int](./currentpage.md)
  The current page, shown by the page control as a white dot.
- [var numberOfPages: Int](./numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var hidesForSinglePage: Bool](./hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [func updateCurrentPageDisplay()](./updatecurrentpagedisplay%28%29.md)
  Updates the page indicator to the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/deferscurrentpagedisplay)*