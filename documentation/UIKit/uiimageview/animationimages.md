# animationImages

**Framework**: UIKit  
**Kind**: property

An array of [`UIImage`](uiimage.md) objects to use for an animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var animationImages: [UIImage]? { get set }
```

#### Discussion

The array must contain [`UIImage`](uiimage.md) objects. You may use the same image object more than once in the array. Setting this property to a value other than `nil` hides the image represented by the [`image`](uiimageview/image.md) property. The value of this property is `nil` by default.

## See Also

- [var image: UIImage?](uiimageview/image.md)
  The image displayed in the image view.
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
- [var isAnimating: Bool](uiimageview/isanimating.md)
  Returns a Boolean value indicating whether the animation is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/animationimages)*