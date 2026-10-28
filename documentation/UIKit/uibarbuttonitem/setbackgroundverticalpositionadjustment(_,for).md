# setBackgroundVerticalPositionAdjustment(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the background vertical position offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, for barMetrics: UIBarMetrics)
```

```objc
- (void) setBackgroundVerticalPositionAdjustment:(CGFloat) adjustment forBarMetrics:(UIBarMetrics) barMetrics;
```

## Discussion

This offset is used to adjust the vertical centering of bordered bar buttons within the bar.

## Parameters

- `adjustment`: The background vertical position offset for `barMetrics`.
- `barMetrics`: Bar metrics.

## See Also

### Customizing the background
- [func backgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./backgroundverticalpositionadjustment%28for%29.md)
  Returns the background vertical position offset for specified bar metrics.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image for a specified state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image for a specified state and bar metrics.
- [func backgroundImage(for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,style,barmetrics%29.md)
  Returns the background image for the specified state, style, and metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,style,barmetrics%29.md)
  Sets the background image for the specified state, style, and metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/setbackgroundverticalpositionadjustment(_:for:))*