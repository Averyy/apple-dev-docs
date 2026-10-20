# barTintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The tint color to apply to the navigation bar background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var barTintColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * barTintColor;
```

#### Discussion

This color is made translucent by default unless you set the [`isTranslucent`](./istranslucent.md) property to [`false`](../../Swift/false.md).

## See Also

### Changing the background
- [func backgroundImage(for: UIBarMetrics) -> UIImage?](./backgroundimage%28for%29.md)
  Returns the background image for given bar metrics.
- [func setBackgroundImage(UIImage?, for: UIBarMetrics)](./setbackgroundimage%28_,for%29.md)
  Sets the background image for given bar metrics.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image to use for a given bar position and set of metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image to use for a given bar position and set of metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/bartintcolor)*