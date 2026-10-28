# backgroundImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image to display on top of the bar’s background color.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var backgroundImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) UIImage * backgroundImage;
```

## Discussion

The bar layers the specified image on top of the content in the [`backgroundEffect`](./backgroundeffect.md) and [`backgroundColor`](./backgroundcolor.md) properties. UIKit sizes the image according to the value in the [`backgroundImageContentMode`](./backgroundimagecontentmode.md) property.

## See Also

### Configuring the background appearance
- [var backgroundEffect: UIBlurEffect?](./backgroundeffect.md)
  The blur effect to apply to the bar’s background.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The background color of the bar.
- [var backgroundImageContentMode: UIView.ContentMode](./backgroundimagecontentmode.md)
  The content mode to use when displaying the bar’s background image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/backgroundimage)*