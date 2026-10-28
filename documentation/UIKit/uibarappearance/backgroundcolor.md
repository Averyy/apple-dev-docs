# backgroundColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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
var backgroundColor: UIColor? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UIColor * backgroundColor;
```

## Discussion

The bar layers the specified color on top of any blur effects you specified in the [`backgroundEffect`](./backgroundeffect.md) property, and below the image in the [`backgroundImage`](./backgroundimage.md) property.

## See Also

### Configuring the background appearance
- [var backgroundEffect: UIBlurEffect?](./backgroundeffect.md)
  The blur effect to apply to the bar’s background.
- [var backgroundImage: UIImage?](./backgroundimage.md)
  The image to display on top of the bar’s background color.
- [var backgroundImageContentMode: UIView.ContentMode](./backgroundimagecontentmode.md)
  The content mode to use when displaying the bar’s background image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/backgroundcolor)*