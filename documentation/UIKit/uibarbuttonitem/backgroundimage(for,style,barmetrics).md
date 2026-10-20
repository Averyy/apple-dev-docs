# backgroundImage(for:style:barMetrics:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the background image for the specified state, style, and metrics.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func backgroundImage(for state: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?
```

```objc
- (UIImage *) backgroundImageForState:(UIControlState) state style:(UIBarButtonItemStyle) style barMetrics:(UIBarMetrics) barMetrics;
```

#### Return Value

The background image associated with the specified state, style, and metrics.

## Parameters

- `state`: The bar button state.
- `style`: The bar button style.
- `barMetrics`: The bar button metrics.

## See Also

### Customizing the background
- [func backgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./backgroundverticalpositionadjustment%28for%29.md)
  Returns the background vertical position offset for specified bar metrics.
- [func setBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./setbackgroundverticalpositionadjustment%28_,for%29.md)
  Sets the background vertical position offset for specified bar metrics.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image for a specified state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image for a specified state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,style,barmetrics%29.md)
  Sets the background image for the specified state, style, and metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/backgroundimage(for:style:barmetrics:))*