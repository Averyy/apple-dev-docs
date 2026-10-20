# setBackButtonBackgroundImage(_:for:barMetrics:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the back button background image for a specified control state and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setBackButtonBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State, barMetrics: UIBarMetrics)
```

```objc
- (void) setBackButtonBackgroundImage:(UIImage *) backgroundImage forState:(UIControlState) state barMetrics:(UIBarMetrics) barMetrics;
```

#### Discussion

This modifier applies only to navigation bar back buttons and is ignored by other buttons.

For good results, `backgroundImage` must be a stretchable image.

## Parameters

- `backgroundImage`: The image to use for the back button’s background.
- `state`: A control state.
- `barMetrics`: Bar metrics.

## See Also

### Customizing the Back button
- [func backButtonBackgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](./backbuttonbackgroundimage%28for,barmetrics%29.md)
  Returns the back button background image for a specified control state and bar metrics.
- [func backButtonTitlePositionAdjustment(for: UIBarMetrics) -> UIOffset](./backbuttontitlepositionadjustment%28for%29.md)
  Returns the back button title offset for specified bar metrics.
- [func setBackButtonTitlePositionAdjustment(UIOffset, for: UIBarMetrics)](./setbackbuttontitlepositionadjustment%28_,for%29.md)
  Sets the back button title offset for specified bar metrics.
- [func backButtonBackgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./backbuttonbackgroundverticalpositionadjustment%28for%29.md)
  Returns the back button vertical position offset for specified bar metrics.
- [func setBackButtonBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./setbackbuttonbackgroundverticalpositionadjustment%28_,for%29.md)
  Sets the back button vertical position offset for specified bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/setbackbuttonbackgroundimage(_:for:barmetrics:))*