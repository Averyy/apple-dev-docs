# updateCurrentPageDisplay()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the page indicator to the current page.

**Availability**:
- iOS 2.0+ - Deprecated in 14.0
- iPadOS 2.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- tvOS - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: The system no longer supports this method.

## Declaration

```swift
func updateCurrentPageDisplay()
```

```objc
- (void) updateCurrentPageDisplay;
```

## Discussion

This method updates the page indicator so that the current page (the white dot) matches the value returned from [`currentPage`](./currentpage.md). The class ignores this method if the value of [`defersCurrentPageDisplay`](./deferscurrentpagedisplay.md) is [`false`](../../Swift/false.md). Setting the [`currentPage`](./currentpage.md) value directly updates the indicator immediately.

## See Also

### Managing pages
- [var currentPage: Int](./currentpage.md)
  The current page, shown by the page control as a white dot.
- [var numberOfPages: Int](./numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var hidesForSinglePage: Bool](./hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [var defersCurrentPageDisplay: Bool](./deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/updatecurrentpagedisplay())*