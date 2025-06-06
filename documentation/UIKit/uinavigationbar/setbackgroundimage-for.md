# setBackgroundImage(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the background image for given bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBackgroundImage(_ backgroundImage: UIImage?, for barMetrics: UIBarMetrics)
```

#### Discussion

Equivalent to using [`setBackgroundImage(_:for:barMetrics:)`](uinavigationbar/setbackgroundimage(_:for:barmetrics:).md) with a position of [`UIBarPosition.any`](uibarposition/any.md).

## Parameters

- `backgroundImage`: The background image to use for  .
- `barMetrics`: A bar metrics constant.

## See Also

- [var barTintColor: UIColor?](uinavigationbar/bartintcolor.md)
  The tint color to apply to the navigation bar background.
- [func backgroundImage(for: UIBarMetrics) -> UIImage?](uinavigationbar/backgroundimage(for:).md)
  Returns the background image for given bar metrics.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](uinavigationbar/backgroundimage(for:barmetrics:).md)
  Returns the background image to use for a given bar position and set of metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](uinavigationbar/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image to use for a given bar position and set of metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/setbackgroundimage(_:for:))*