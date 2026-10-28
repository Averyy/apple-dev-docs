# setBackgroundImage(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the background image for given bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, for barMetrics: UIBarMetrics)
```

```objc
- (void) setBackgroundImage:(UIImage *) backgroundImage forBarMetrics:(UIBarMetrics) barMetrics;
```

## Discussion

Equivalent to using [`setBackgroundImage(_:for:barMetrics:)`](./setbackgroundimage%28_,for,barmetrics%29.md) with a position of [`UIBarPosition.any`](../uibarposition/any.md).

## Parameters

- `backgroundImage`: The background image to use for `barMetrics`.
- `barMetrics`: A bar metrics constant.

## See Also

### Changing the background
- [var barTintColor: UIColor?](./bartintcolor.md)
  The tint color to apply to the navigation bar background.
- [func backgroundImage(for: UIBarMetrics) -> UIImage?](./backgroundimage%28for%29.md)
  Returns the background image for given bar metrics.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image to use for a given bar position and set of metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image to use for a given bar position and set of metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/setbackgroundimage(_:for:))*