# barTintColor

**Framework**: UIKit  
**Kind**: property

The tint color to apply to the navigation bar background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var barTintColor: UIColor? { get set }
```

#### Discussion

This color is made translucent by default unless you set the [`isTranslucent`](uinavigationbar/istranslucent.md) property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func backgroundImage(for: UIBarMetrics) -> UIImage?](uinavigationbar/backgroundimage(for:).md)
  Returns the background image for given bar metrics.
- [func setBackgroundImage(UIImage?, for: UIBarMetrics)](uinavigationbar/setbackgroundimage(_:for:).md)
  Sets the background image for given bar metrics.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](uinavigationbar/backgroundimage(for:barmetrics:).md)
  Returns the background image to use for a given bar position and set of metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](uinavigationbar/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image to use for a given bar position and set of metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/bartintcolor)*