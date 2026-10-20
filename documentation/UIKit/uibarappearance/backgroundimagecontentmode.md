# backgroundImageContentMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The content mode to use when displaying the bar’s background image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var backgroundImageContentMode: UIView.ContentMode { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIViewContentMode backgroundImageContentMode;
```

#### Discussion

Use this property to specify how to scale or fit the image in the [`backgroundImage`](./backgroundimage.md) property.

## See Also

### Configuring the background appearance
- [var backgroundEffect: UIBlurEffect?](./backgroundeffect.md)
  The blur effect to apply to the bar’s background.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The background color of the bar.
- [var backgroundImage: UIImage?](./backgroundimage.md)
  The image to display on top of the bar’s background color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/backgroundimagecontentmode)*