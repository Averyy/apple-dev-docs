# isHighlighted

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the image is highlighted.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isHighlighted: Bool { get set }
```

#### Discussion

This property determines whether the regular or highlighted images are used. When [`isHighlighted`](uiimageview/ishighlighted.md) is set to [`true`](https://developer.apple.com/documentation/Swift/true), a non-animated image will use the [`highlightedImage`](uiimageview/highlightedimage.md) property and an animated image will use the [`highlightedAnimationImages`](uiimageview/highlightedanimationimages.md). If both of those properties are set to `nil` or if [`isHighlighted`](uiimageview/ishighlighted.md) is set to [`false`](https://developer.apple.com/documentation/Swift/false), it will use the [`image`](uiimageview/image.md) and [`animationImages`](uiimageview/animationimages.md) properties.

## See Also

- [var isUserInteractionEnabled: Bool](uiimageview/isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var tintColor: UIColor!](uiimageview/tintcolor.md)
  A color used to tint template images in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/ishighlighted)*