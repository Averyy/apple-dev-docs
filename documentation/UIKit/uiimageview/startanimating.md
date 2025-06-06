# startAnimating()

**Framework**: UIKit  
**Kind**: method

Starts animating the images in the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func startAnimating()
```

#### Discussion

This method always starts the animation from the first image in the list.

## See Also

- [var animationImages: [UIImage]?](uiimageview/animationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation.
- [var highlightedAnimationImages: [UIImage]?](uiimageview/highlightedanimationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation when the view is highlighted.
- [var animationDuration: TimeInterval](uiimageview/animationduration.md)
  The amount of time it takes to go through one cycle of the images.
- [var animationRepeatCount: Int](uiimageview/animationrepeatcount.md)
  Specifies the number of times to repeat the animation.
- [func stopAnimating()](uiimageview/stopanimating.md)
  Stops animating the images in the receiver.
- [var isAnimating: Bool](uiimageview/isanimating.md)
  Returns a Boolean value indicating whether the animation is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/startanimating())*