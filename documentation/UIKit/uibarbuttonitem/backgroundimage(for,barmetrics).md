# backgroundImage(for:barMetrics:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the background image for a specified state and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func backgroundImage(for state: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?
```

```objc
- (UIImage *) backgroundImageForState:(UIControlState) state barMetrics:(UIBarMetrics) barMetrics;
```

#### Return Value

The background image for the button given state and metrics.

## Parameters

- `state`: A control state.
- `barMetrics`: Bar metrics.

## See Also

### Customizing the background
- [func backgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./backgroundverticalpositionadjustment%28for%29.md)
  Returns the background vertical position offset for specified bar metrics.
- [func setBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./setbackgroundverticalpositionadjustment%28_,for%29.md)
  Sets the background vertical position offset for specified bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image for a specified state and bar metrics.
- [func backgroundImage(for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,style,barmetrics%29.md)
  Returns the background image for the specified state, style, and metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,style,barmetrics%29.md)
  Sets the background image for the specified state, style, and metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/backgroundimage(for:barmetrics:))*