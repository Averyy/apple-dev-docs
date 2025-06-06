# currentPageIndicatorTintColor

**Framework**: UIKit  
**Kind**: property

The tint color to apply to the current page indicator.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var currentPageIndicatorTintColor: UIColor? { get set }
```

#### Discussion

The default color is an opaque white for the current page indicator dot. The current page indicator dot is used to indicate the currently visible page. Assigning a new value to this property does not automatically change the color in the [`pageIndicatorTintColor`](uipagecontrol/pageindicatortintcolor.md) property because the value for these two properties is not automatically derived from the other. Both properties must be specified independently.

## See Also

- [var pageIndicatorTintColor: UIColor?](uipagecontrol/pageindicatortintcolor.md)
  The tint color to apply to the page indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/currentpageindicatortintcolor)*