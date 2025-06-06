# backgroundEffect

**Framework**: UIKit  
**Kind**: property

The blur effect to apply to the bar’s background.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var backgroundEffect: UIBlurEffect? { get set }
```

#### Discussion

The blur effect provides the base layer for the bar’s appearance, and it determines how much of the underlying content is visible. UIKit applies the [`backgroundColor`](uibarappearance/backgroundcolor.md) and [`backgroundImage`](uibarappearance/backgroundimage.md) on top of this effect.

## See Also

- [var backgroundColor: UIColor?](uibarappearance/backgroundcolor.md)
  The background color of the bar.
- [var backgroundImage: UIImage?](uibarappearance/backgroundimage.md)
  The image to display on top of the bar’s background color.
- [var backgroundImageContentMode: UIView.ContentMode](uibarappearance/backgroundimagecontentmode.md)
  The content mode to use when displaying the bar’s background image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/backgroundeffect)*