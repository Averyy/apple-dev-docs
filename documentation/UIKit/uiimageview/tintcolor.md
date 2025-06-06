# tintColor

**Framework**: UIKit  
**Kind**: property

A color used to tint template images in the view hierarchy.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tintColor: UIColor! { get set }
```

#### Discussion

The default is `nil`. If a non-`nil` value is specified, the color is applied to any template images attached to the image view. For more information, see the [`renderingMode`](uiimage/renderingmode-swift.property.md) property on the [`UIImage`](uiimage.md) class.

## See Also

- [var isUserInteractionEnabled: Bool](uiimageview/isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var isHighlighted: Bool](uiimageview/ishighlighted.md)
  A Boolean value that determines whether the image is highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/tintcolor)*