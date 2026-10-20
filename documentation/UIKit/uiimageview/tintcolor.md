# tintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A color used to tint template images in the view hierarchy.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var tintColor: UIColor! { get set }
```

```objc
@property (nonatomic, strong, null_resettable) UIColor * tintColor;
```

#### Discussion

The default is `nil`. If a non-`nil` value is specified, the color is applied to any template images attached to the image view. For more information, see the [`renderingMode`](../uiimage/renderingmode-swift.property.md) property on the [`UIImage`](../uiimage.md) class.

## See Also

### Configuring the image view
- [var isUserInteractionEnabled: Bool](./isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that determines whether the image is highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/tintcolor)*