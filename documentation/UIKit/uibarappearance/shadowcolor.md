# shadowColor

**Framework**: UIKit  
**Kind**: property

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
@MainActor var shadowColor: UIColor? { get set }
```

#### Discussion

UIKit uses this property and the [`shadowImage`](uibarappearance/shadowimage.md) property to determine the shadow’s appearance. When [`shadowImage`](uibarappearance/shadowimage.md) is `nil`, the bar displays a default shadow tinted according to the value of this property. If this property is `nil` or contains the [`clear`](uicolor/clear.md) color, the bar displays no shadow.

If [`shadowImage`](uibarappearance/shadowimage.md) contains a template image, the bar uses the image for the shadow and tints it using the value in this property. If this property is `nil` or contains the [`clear`](uicolor/clear.md) color, the bar displays no shadow. However, if [`shadowImage`](uibarappearance/shadowimage.md) doesn’t contain a template image, the bar displays the image without applying the color in this property.

## See Also

- [var shadowImage: UIImage?](uibarappearance/shadowimage.md)
  The image to use for the bar’s shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/shadowcolor)*