# isAnimating

**Framework**: UIKit  
**Kind**: property

Returns a Boolean value indicating whether the animation is running.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isAnimating: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the animation is running; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var animationImages: [UIImage]?](uiimageview/animationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation.
- [var highlightedAnimationImages: [UIImage]?](uiimageview/highlightedanimationimages.md)
  An array of [`UIImage`](uiimage.md) objects to use for an animation when the view is highlighted.
- [var animationDuration: TimeInterval](uiimageview/animationduration.md)
  The amount of time it takes to go through one cycle of the images.
- [var animationRepeatCount: Int](uiimageview/animationrepeatcount.md)
  Specifies the number of times to repeat the animation.
- [func startAnimating()](uiimageview/startanimating.md)
  Starts animating the images in the receiver.
- [func stopAnimating()](uiimageview/stopanimating.md)
  Stops animating the images in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/isanimating)*