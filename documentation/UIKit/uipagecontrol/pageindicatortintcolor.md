# pageIndicatorTintColor

**Framework**: UIKit  
**Kind**: property

The tint color to apply to the page indicator.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var pageIndicatorTintColor: UIColor? { get set }
```

#### Discussion

The default color is a translucent white for the page indicator dot. The page indicator dot is used for all of the pages not visible on the screen. Assigning a new value to this property does not automatically change the color in the [`currentPageIndicatorTintColor`](uipagecontrol/currentpageindicatortintcolor.md) property because the value for these two properties is not automatically derived from the other. Both properties must be specified independently. Similarly, no alpha is applied to this property for you. It is recommended (but not required) that the color you specify for this parameter contains some transparency–i.e. the alpha value should be less than 1.0.

## See Also

- [var currentPageIndicatorTintColor: UIColor?](uipagecontrol/currentpageindicatortintcolor.md)
  The tint color to apply to the current page indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/pageindicatortintcolor)*