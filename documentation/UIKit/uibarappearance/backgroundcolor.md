# backgroundColor

**Framework**: UIKit  
**Kind**: property

The background color of the bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: UIColor? { get set }
```

#### Discussion

The bar layers the specified color on top of any blur effects you specified in the [`backgroundEffect`](uibarappearance/backgroundeffect.md) property, and below the image in the [`backgroundImage`](uibarappearance/backgroundimage.md) property.

## See Also

- [var backgroundEffect: UIBlurEffect?](uibarappearance/backgroundeffect.md)
  The blur effect to apply to the bar’s background.
- [var backgroundImage: UIImage?](uibarappearance/backgroundimage.md)
  The image to display on top of the bar’s background color.
- [var backgroundImageContentMode: UIView.ContentMode](uibarappearance/backgroundimagecontentmode.md)
  The content mode to use when displaying the bar’s background image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/backgroundcolor)*