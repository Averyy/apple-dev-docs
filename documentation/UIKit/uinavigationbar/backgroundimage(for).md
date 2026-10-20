# backgroundImage(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the background image for given bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func backgroundImage(for barMetrics: UIBarMetrics) -> UIImage?
```

```objc
- (UIImage *) backgroundImageForBarMetrics:(UIBarMetrics) barMetrics;
```

#### Return Value

The background image for `barMetrics`.

#### Discussion

Equivalent to using [`backgroundImage(for:barMetrics:)`](./backgroundimage%28for,barmetrics%29.md) with a position of [`UIBarPosition.any`](../uibarposition/any.md).

## Parameters

- `barMetrics`: A bar metrics constant.

## See Also

### Changing the background
- [var barTintColor: UIColor?](./bartintcolor.md)
  The tint color to apply to the navigation bar background.
- [func setBackgroundImage(UIImage?, for: UIBarMetrics)](./setbackgroundimage%28_,for%29.md)
  Sets the background image for given bar metrics.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image to use for a given bar position and set of metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image to use for a given bar position and set of metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/backgroundimage(for:))*