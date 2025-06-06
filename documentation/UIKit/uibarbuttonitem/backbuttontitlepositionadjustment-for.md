# backButtonTitlePositionAdjustment(for:)

**Framework**: UIKit  
**Kind**: method

Returns the back button title offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backButtonTitlePositionAdjustment(for barMetrics: UIBarMetrics) -> UIOffset
```

#### Return Value

The back button title offset for `barMetrics`.

#### Discussion

This modifier applies only to navigation bar back buttons and is ignored by other buttons.

## Parameters

- `barMetrics`: Bar metrics.

## See Also

- [func backButtonBackgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backbuttonbackgroundimage(for:barmetrics:).md)
  Returns the back button background image for a specified control state and bar metrics.
- [func setBackButtonBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackbuttonbackgroundimage(_:for:barmetrics:).md)
  Sets the back button background image for a specified control state and bar metrics.
- [func setBackButtonTitlePositionAdjustment(UIOffset, for: UIBarMetrics)](uibarbuttonitem/setbackbuttontitlepositionadjustment(_:for:).md)
  Sets the back button title offset for specified bar metrics.
- [func backButtonBackgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](uibarbuttonitem/backbuttonbackgroundverticalpositionadjustment(for:).md)
  Returns the back button vertical position offset for specified bar metrics.
- [func setBackButtonBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](uibarbuttonitem/setbackbuttonbackgroundverticalpositionadjustment(_:for:).md)
  Sets the back button vertical position offset for specified bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/backbuttontitlepositionadjustment(for:))*