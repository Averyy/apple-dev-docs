# shadowColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color to apply to the bar’s custom or default shadow.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var shadowColor: UIColor? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UIColor * shadowColor;
```

#### Discussion

UIKit uses this property and the [`shadowImage`](./shadowimage.md) property to determine the shadow’s appearance. When [`shadowImage`](./shadowimage.md) is `nil`, the bar displays a default shadow tinted according to the value of this property. If this property is `nil` or contains the [`clear`](../uicolor/clear.md) color, the bar displays no shadow.

If [`shadowImage`](./shadowimage.md) contains a template image, the bar uses the image for the shadow and tints it using the value in this property. If this property is `nil` or contains the [`clear`](../uicolor/clear.md) color, the bar displays no shadow. However, if [`shadowImage`](./shadowimage.md) doesn’t contain a template image, the bar displays the image without applying the color in this property.

## See Also

### Configuring the shadow appearance
- [var shadowImage: UIImage?](./shadowimage.md)
  The image to use for the bar’s shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/shadowcolor)*