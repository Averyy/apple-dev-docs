# isHighlighted

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the image is highlighted.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isHighlighted: Bool { get set }
```

```objc
@property (nonatomic, getter=isHighlighted) BOOL highlighted;
```

## Discussion

This property determines whether the regular or highlighted images are used. When [`isHighlighted`](./ishighlighted.md) is set to [`true`](../../Swift/true.md), a non-animated image will use the [`highlightedImage`](./highlightedimage.md) property and an animated image will use the [`highlightedAnimationImages`](./highlightedanimationimages.md). If both of those properties are set to `nil` or if [`isHighlighted`](./ishighlighted.md) is set to [`false`](../../Swift/false.md), it will use the [`image`](./image.md) and [`animationImages`](./animationimages.md) properties.

## See Also

### Configuring the image view
- [var isUserInteractionEnabled: Bool](./isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var tintColor: UIColor!](./tintcolor.md)
  A color used to tint template images in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/ishighlighted)*