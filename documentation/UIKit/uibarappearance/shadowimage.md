# shadowImage

**Framework**: UIKit  
**Kind**: property

The image to use for the bar’s shadow.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shadowImage: UIImage? { get set }
```

#### Discussion

UIKit uses this property and the [`shadowColor`](uibarappearance/shadowcolor.md) property to determine the shadow’s appearance. When this property is `nil`, the bar displays a default shadow tinted according to the value in the [`shadowColor`](uibarappearance/shadowcolor.md) property. If [`shadowColor`](uibarappearance/shadowcolor.md) is `nil` or contains the [`clear`](uicolor/clear.md) color, the bar displays no shadow.

If this property contains a template image, the bar uses the image for the shadow and tints it using the value in [`shadowColor`](uibarappearance/shadowcolor.md). If [`shadowColor`](uibarappearance/shadowcolor.md) is `nil` or contains the [`clear`](uicolor/clear.md) color, the bar displays no shadow. However, if this property doesn’t contain a template image, the bar displays the image without applying the shadow color.

## See Also

- [var shadowColor: UIColor?](uibarappearance/shadowcolor.md)
  The color to apply to the bar’s custom or default shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/shadowimage)*