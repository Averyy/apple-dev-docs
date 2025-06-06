# backButtonBackgroundImage(for:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Returns the back button background image for a specified control state and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backButtonBackgroundImage(for state: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?
```

#### Return Value

The back button background image for `state` and `barMetrics`.

#### Discussion

This modifier applies only to navigation bar back buttons and is ignored by other buttons.

## Parameters

- `state`: A control state.
- `barMetrics`: Bar metrics.

## See Also

- [func setBackButtonBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackbuttonbackgroundimage(_:for:barmetrics:).md)
  Sets the back button background image for a specified control state and bar metrics.
- [func backButtonTitlePositionAdjustment(for: UIBarMetrics) -> UIOffset](uibarbuttonitem/backbuttontitlepositionadjustment(for:).md)
  Returns the back button title offset for specified bar metrics.
- [func setBackButtonTitlePositionAdjustment(UIOffset, for: UIBarMetrics)](uibarbuttonitem/setbackbuttontitlepositionadjustment(_:for:).md)
  Sets the back button title offset for specified bar metrics.
- [func backButtonBackgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](uibarbuttonitem/backbuttonbackgroundverticalpositionadjustment(for:).md)
  Returns the back button vertical position offset for specified bar metrics.
- [func setBackButtonBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](uibarbuttonitem/setbackbuttonbackgroundverticalpositionadjustment(_:for:).md)
  Sets the back button vertical position offset for specified bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/backbuttonbackgroundimage(for:barmetrics:))*