# backButtonTitlePositionAdjustment(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the back button title offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func backButtonTitlePositionAdjustment(for barMetrics: UIBarMetrics) -> UIOffset
```

```objc
- (UIOffset) backButtonTitlePositionAdjustmentForBarMetrics:(UIBarMetrics) barMetrics;
```

## Return Value

The back button title offset for `barMetrics`.

## Discussion

This modifier applies only to navigation bar back buttons and is ignored by other buttons.

## Parameters

- `barMetrics`: Bar metrics.

## See Also

### Customizing the Back button
- [func backButtonBackgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](./backbuttonbackgroundimage%28for,barmetrics%29.md)
  Returns the back button background image for a specified control state and bar metrics.
- [func setBackButtonBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](./setbackbuttonbackgroundimage%28_,for,barmetrics%29.md)
  Sets the back button background image for a specified control state and bar metrics.
- [func setBackButtonTitlePositionAdjustment(UIOffset, for: UIBarMetrics)](./setbackbuttontitlepositionadjustment%28_,for%29.md)
  Sets the back button title offset for specified bar metrics.
- [func backButtonBackgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./backbuttonbackgroundverticalpositionadjustment%28for%29.md)
  Returns the back button vertical position offset for specified bar metrics.
- [func setBackButtonBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./setbackbuttonbackgroundverticalpositionadjustment%28_,for%29.md)
  Sets the back button vertical position offset for specified bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/backbuttontitlepositionadjustment(for:))*