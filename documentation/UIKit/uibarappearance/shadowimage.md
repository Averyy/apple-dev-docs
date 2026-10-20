# shadowImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image to use for the bar’s shadow.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var shadowImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) UIImage * shadowImage;
```

#### Discussion

UIKit uses this property and the [`shadowColor`](./shadowcolor.md) property to determine the shadow’s appearance. When this property is `nil`, the bar displays a default shadow tinted according to the value in the [`shadowColor`](./shadowcolor.md) property. If [`shadowColor`](./shadowcolor.md) is `nil` or contains the [`clear`](../uicolor/clear.md) color, the bar displays no shadow.

If this property contains a template image, the bar uses the image for the shadow and tints it using the value in [`shadowColor`](./shadowcolor.md). If [`shadowColor`](./shadowcolor.md) is `nil` or contains the [`clear`](../uicolor/clear.md) color, the bar displays no shadow. However, if this property doesn’t contain a template image, the bar displays the image without applying the shadow color.

## See Also

### Configuring the shadow appearance
- [var shadowColor: UIColor?](./shadowcolor.md)
  The color to apply to the bar’s custom or default shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/shadowimage)*