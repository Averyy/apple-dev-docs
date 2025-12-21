# highlightedImage

**Framework**: UIKit  
**Kind**: property

The highlighted image displayed in the image view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var highlightedImage: UIImage? { get set }
```

#### Discussion

The image in this property is displayed when the image view’s [`isHighlighted`](uiimageview/ishighlighted.md) property is [`true`](https://developer.apple.com/documentation/Swift/true). If the [`highlightedAnimationImages`](uiimageview/highlightedanimationimages.md) property contains a valid set of images, those image are used instead.

This property is set to the image (if any) you specified at initialization time. If you did not use the [`init(image:highlightedImage:)`](uiimageview/init(image:highlightedimage:).md) method to initialize your image view, the initial value of this property is `nil`.

## See Also

- [var highlightedAnimationImages: [UIImage]?](uiimageview/highlightedanimationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation when the view is highlighted.
- [var image: UIImage?](uiimageview/image.md)
  The image displayed in the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/highlightedimage)*