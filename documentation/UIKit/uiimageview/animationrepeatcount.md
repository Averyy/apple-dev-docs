# animationRepeatCount

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies the number of times to repeat the animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var animationRepeatCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger animationRepeatCount;
```

## Discussion

The default value is `0`, which specifies to repeat the animation indefinitely.

## See Also

### Animating a sequence of images
- [var animationImages: [UIImage]?](./animationimages.md)
  An array of [`UIImage`](../uiimage.md) objects to use for an animation.
- [var highlightedAnimationImages: [UIImage]?](./highlightedanimationimages.md)
  An array of [`UIImage`](../uiimage.md) objects to use for an animation when the view is highlighted.
- [var animationDuration: TimeInterval](./animationduration.md)
  The amount of time it takes to go through one cycle of the images.
- [func startAnimating()](./startanimating%28%29.md)
  Starts animating the images in the receiver.
- [func stopAnimating()](./stopanimating%28%29.md)
  Stops animating the images in the receiver.
- [var isAnimating: Bool](./isanimating.md)
  Returns a Boolean value indicating whether the animation is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/animationrepeatcount)*