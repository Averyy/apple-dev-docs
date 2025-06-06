# backgroundImage(for:)

**Framework**: UIKit  
**Kind**: method

Returns the background image for given bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backgroundImage(for barMetrics: UIBarMetrics) -> UIImage?
```

#### Return Value

The background image for `barMetrics`.

#### Discussion

Equivalent to using [`backgroundImage(for:barMetrics:)`](uinavigationbar/backgroundimage(for:barmetrics:).md) with a position of [`UIBarPosition.any`](uibarposition/any.md).

## Parameters

- `barMetrics`: A bar metrics constant.

## See Also

- [var barTintColor: UIColor?](uinavigationbar/bartintcolor.md)
  The tint color to apply to the navigation bar background.
- [func setBackgroundImage(UIImage?, for: UIBarMetrics)](uinavigationbar/setbackgroundimage(_:for:).md)
  Sets the background image for given bar metrics.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](uinavigationbar/backgroundimage(for:barmetrics:).md)
  Returns the background image to use for a given bar position and set of metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](uinavigationbar/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image to use for a given bar position and set of metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/backgroundimage(for:))*