# backgroundImage(for:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Returns the background image to use for a given bar position and set of metrics.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backgroundImage(for barPosition: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?
```

#### Return Value

The image to use for the specified location and metrics.

#### Discussion

Resizable images will be stretched vertically, if necessary, for a position of [`UIBarPosition.topAttached`](uibarposition/topattached.md).

## Parameters

- `barPosition`: The location of the navigation bar.
- `barMetrics`: The metrics of the navigation bar.

## See Also

- [var barTintColor: UIColor?](uinavigationbar/bartintcolor.md)
  The tint color to apply to the navigation bar background.
- [func backgroundImage(for: UIBarMetrics) -> UIImage?](uinavigationbar/backgroundimage(for:).md)
  Returns the background image for given bar metrics.
- [func setBackgroundImage(UIImage?, for: UIBarMetrics)](uinavigationbar/setbackgroundimage(_:for:).md)
  Sets the background image for given bar metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](uinavigationbar/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image to use for a given bar position and set of metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/backgroundimage(for:barmetrics:))*