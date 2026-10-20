# numberOfPages

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number of pages the receiver shows (as dots).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var numberOfPages: Int { get set }
```

```objc
@property (nonatomic, assign) NSInteger numberOfPages;
```

#### Discussion

The value of the property is the number of pages for the page control to show as dots. The default value is 0.

## See Also

### Managing pages
- [var currentPage: Int](./currentpage.md)
  The current page, shown by the page control as a white dot.
- [var hidesForSinglePage: Bool](./hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [var defersCurrentPageDisplay: Bool](./deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.
- [func updateCurrentPageDisplay()](./updatecurrentpagedisplay%28%29.md)
  Updates the page indicator to the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/numberofpages)*