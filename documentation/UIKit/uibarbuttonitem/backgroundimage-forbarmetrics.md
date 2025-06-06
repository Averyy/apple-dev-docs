# backgroundImage(for:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Returns the background image for a specified state and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backgroundImage(for state: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?
```

#### Return Value

The background image for the button given state and metrics.

## Parameters

- `state`: A control state.
- `barMetrics`: Bar metrics.

## See Also

- [func backgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](uibarbuttonitem/backgroundverticalpositionadjustment(for:).md)
  Returns the background vertical position offset for specified bar metrics.
- [func setBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](uibarbuttonitem/setbackgroundverticalpositionadjustment(_:for:).md)
  Sets the background vertical position offset for specified bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image for a specified state and bar metrics.
- [func backgroundImage(for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:style:barmetrics:).md)
  Returns the background image for the specified state, style, and metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:style:barmetrics:).md)
  Sets the background image for the specified state, style, and metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/backgroundimage(for:barmetrics:))*