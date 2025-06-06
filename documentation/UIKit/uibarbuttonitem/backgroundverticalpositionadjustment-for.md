# backgroundVerticalPositionAdjustment(for:)

**Framework**: UIKit  
**Kind**: method

Returns the background vertical position offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backgroundVerticalPositionAdjustment(for barMetrics: UIBarMetrics) -> CGFloat
```

#### Return Value

The background vertical position offset for `barMetrics`.

#### Discussion

This offset is used to adjust the vertical centering of bordered bar buttons within the bar.

## Parameters

- `barMetrics`: Bar metrics.

## See Also

- [func setBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](uibarbuttonitem/setbackgroundverticalpositionadjustment(_:for:).md)
  Sets the background vertical position offset for specified bar metrics.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:barmetrics:).md)
  Returns the background image for a specified state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image for a specified state and bar metrics.
- [func backgroundImage(for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:style:barmetrics:).md)
  Returns the background image for the specified state, style, and metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:style:barmetrics:).md)
  Sets the background image for the specified state, style, and metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/backgroundverticalpositionadjustment(for:))*