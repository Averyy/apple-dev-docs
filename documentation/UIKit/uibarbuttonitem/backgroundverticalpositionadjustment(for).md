# backgroundVerticalPositionAdjustment(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the background vertical position offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func backgroundVerticalPositionAdjustment(for barMetrics: UIBarMetrics) -> CGFloat
```

```objc
- (CGFloat) backgroundVerticalPositionAdjustmentForBarMetrics:(UIBarMetrics) barMetrics;
```

#### Return Value

The background vertical position offset for `barMetrics`.

#### Discussion

This offset is used to adjust the vertical centering of bordered bar buttons within the bar.

## Parameters

- `barMetrics`: Bar metrics.

## See Also

### Customizing the background
- [func setBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./setbackgroundverticalpositionadjustment%28_,for%29.md)
  Sets the background vertical position offset for specified bar metrics.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image for a specified state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image for a specified state and bar metrics.
- [func backgroundImage(for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,style,barmetrics%29.md)
  Returns the background image for the specified state, style, and metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,style,barmetrics%29.md)
  Sets the background image for the specified state, style, and metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/backgroundverticalpositionadjustment(for:))*