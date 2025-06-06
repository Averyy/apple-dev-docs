# animationDuration

**Framework**: UIKit  
**Kind**: property

The amount of time it takes to go through one cycle of the images.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var animationDuration: TimeInterval { get set }
```

#### Discussion

The time duration is measured in seconds. The default value of this property is `0.0`, which causes the image view to use a duration equal to the number of images multiplied by 1/30th of a second. Thus, if you had 30 images, the duration would be 1 second.

## See Also

- [var animationImages: [UIImage]?](uiimageview/animationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation.
- [var highlightedAnimationImages: [UIImage]?](uiimageview/highlightedanimationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation when the view is highlighted.
- [var animationRepeatCount: Int](uiimageview/animationrepeatcount.md)
  Specifies the number of times to repeat the animation.
- [func startAnimating()](uiimageview/startanimating.md)
  Starts animating the images in the receiver.
- [func stopAnimating()](uiimageview/stopanimating.md)
  Stops animating the images in the receiver.
- [var isAnimating: Bool](uiimageview/isanimating.md)
  Returns a Boolean value indicating whether the animation is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/animationduration)*