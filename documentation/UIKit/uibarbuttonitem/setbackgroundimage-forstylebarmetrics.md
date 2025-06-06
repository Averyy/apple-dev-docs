# setBackgroundImage(_:for:style:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Sets the background image for the specified state, style, and metrics.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)
```

#### Discussion

For good results, `backgroundImage` must be a stretchable image.

## Parameters

- `backgroundImage`: The background image to use for the specified state, style, and metrics.
- `state`: The bar button state.
- `style`: The bar button style.
- `barMetrics`: The bar button metrics.

## See Also

- [func backgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](uibarbuttonitem/backgroundverticalpositionadjustment(for:).md)
  Returns the background vertical position offset for specified bar metrics.
- [func setBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](uibarbuttonitem/setbackgroundverticalpositionadjustment(_:for:).md)
  Sets the background vertical position offset for specified bar metrics.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:barmetrics:).md)
  Returns the background image for a specified state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image for a specified state and bar metrics.
- [func backgroundImage(for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:style:barmetrics:).md)
  Returns the background image for the specified state, style, and metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/setbackgroundimage(_:for:style:barmetrics:))*