# setBackgroundImage(_:for:barMetrics:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the background image to use for a given bar position and set of metrics.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, for barPosition: UIBarPosition, barMetrics: UIBarMetrics)
```

```objc
- (void) setBackgroundImage:(UIImage *) backgroundImage forBarPosition:(UIBarPosition) barPosition barMetrics:(UIBarMetrics) barMetrics;
```

## Discussion

Resizable images will be stretched vertically, if necessary, for a position of [`UIBarPosition.topAttached`](../uibarposition/topattached.md).

## Parameters

- `backgroundImage`: The image to use for the specified location and metrics.
- `barPosition`: The location of the navigation bar.
- `barMetrics`: The metrics of the navigation bar.

## See Also

### Changing the background
- [var barTintColor: UIColor?](./bartintcolor.md)
  The tint color to apply to the navigation bar background.
- [func backgroundImage(for: UIBarMetrics) -> UIImage?](./backgroundimage%28for%29.md)
  Returns the background image for given bar metrics.
- [func setBackgroundImage(UIImage?, for: UIBarMetrics)](./setbackgroundimage%28_,for%29.md)
  Sets the background image for given bar metrics.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image to use for a given bar position and set of metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/setbackgroundimage(_:for:barmetrics:))*