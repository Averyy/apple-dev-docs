# setBackgroundVerticalPositionAdjustment(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the background vertical position offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, for barMetrics: UIBarMetrics)
```

#### Discussion

This offset is used to adjust the vertical centering of bordered bar buttons within the bar.

## Parameters

- `adjustment`: The background vertical position offset for  .
- `barMetrics`: Bar metrics.

## See Also

- [func backgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](uibarbuttonitem/backgroundverticalpositionadjustment(for:).md)
  Returns the background vertical position offset for specified bar metrics.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:barmetrics:).md)
  Returns the background image for a specified state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image for a specified state and bar metrics.
- [func backgroundImage(for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:style:barmetrics:).md)
  Returns the background image for the specified state, style, and metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:style:barmetrics:).md)
  Sets the background image for the specified state, style, and metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/setbackgroundverticalpositionadjustment(_:for:))*