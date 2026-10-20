# animationImages

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of [`UIImage`](../uiimage.md) objects to use for an animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var animationImages: [UIImage]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<UIImage *> * animationImages;
```

#### Discussion

The array must contain [`UIImage`](../uiimage.md) objects. You may use the same image object more than once in the array. Setting this property to a value other than `nil` hides the image represented by the [`image`](./image.md) property. The value of this property is `nil` by default.

## See Also

### Related Documentation
- [var image: UIImage?](./image.md)
  The image displayed in the image view.
### Animating a sequence of images
- [var highlightedAnimationImages: [UIImage]?](./highlightedanimationimages.md)
  An array of [`UIImage`](../uiimage.md) objects to use for an animation when the view is highlighted.
- [var animationDuration: TimeInterval](./animationduration.md)
  The amount of time it takes to go through one cycle of the images.
- [var animationRepeatCount: Int](./animationrepeatcount.md)
  Specifies the number of times to repeat the animation.
- [func startAnimating()](./startanimating%28%29.md)
  Starts animating the images in the receiver.
- [func stopAnimating()](./stopanimating%28%29.md)
  Stops animating the images in the receiver.
- [var isAnimating: Bool](./isanimating.md)
  Returns a Boolean value indicating whether the animation is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/animationimages)*