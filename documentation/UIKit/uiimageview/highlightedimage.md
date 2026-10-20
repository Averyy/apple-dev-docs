# highlightedImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The highlighted image displayed in the image view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var highlightedImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * highlightedImage;
```

#### Discussion

The image in this property is displayed when the image view’s [`isHighlighted`](./ishighlighted.md) property is [`true`](../../Swift/true.md). If the [`highlightedAnimationImages`](./highlightedanimationimages.md) property contains a valid set of images, those image are used instead.

This property is set to the image (if any) you specified at initialization time. If you did not use the [`init(image:highlightedImage:)`](./init%28image,highlightedimage%29.md) method to initialize your image view, the initial value of this property is `nil`.

## See Also

### Related Documentation
- [var highlightedAnimationImages: [UIImage]?](./highlightedanimationimages.md)
  An array of [`UIImage`](../uiimage.md) objects to use for an animation when the view is highlighted.
### Accessing the displayed images
- [var image: UIImage?](./image.md)
  The image displayed in the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/highlightedimage)*