# backgroundImage

**Framework**: UIKit  
**Kind**: property

The image to display on top of the bar’s background color.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backgroundImage: UIImage? { get set }
```

#### Discussion

The bar layers the specified image on top of the content in the [`backgroundEffect`](uibarappearance/backgroundeffect.md) and [`backgroundColor`](uibarappearance/backgroundcolor.md) properties. UIKit sizes the image according to the value in the [`backgroundImageContentMode`](uibarappearance/backgroundimagecontentmode.md) property.

## See Also

- [var backgroundEffect: UIBlurEffect?](uibarappearance/backgroundeffect.md)
  The blur effect to apply to the bar’s background.
- [var backgroundColor: UIColor?](uibarappearance/backgroundcolor.md)
  The background color of the bar.
- [var backgroundImageContentMode: UIView.ContentMode](uibarappearance/backgroundimagecontentmode.md)
  The content mode to use when displaying the bar’s background image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/backgroundimage)*