# highlightedAnimationImages

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of [`UIImage`](../uiimage.md) objects to use for an animation when the view is highlighted.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var highlightedAnimationImages: [UIImage]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<UIImage *> * highlightedAnimationImages;
```

#### Discussion

The array must contain [`UIImage`](../uiimage.md) objects. You may use the same image object more than once in the array. Setting this property to a value other than `nil` hides the image represented by the [`highlightedImage`](./highlightedimage.md) property. The value of this property is `nil` by default.

## See Also

### Related Documentation
- [var highlightedImage: UIImage?](./highlightedimage.md)
  The highlighted image displayed in the image view.
### Animating a sequence of images
- [var animationImages: [UIImage]?](./animationimages.md)
  An array of [`UIImage`](../uiimage.md) objects to use for an animation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/highlightedanimationimages)*