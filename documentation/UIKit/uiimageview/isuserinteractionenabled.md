# isUserInteractionEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether user events are ignored and removed from the event queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isUserInteractionEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isUserInteractionEnabled) BOOL userInteractionEnabled;
```

## Discussion

This property is inherited from the [`UIView`](../uiview.md) parent class. This class changes the default value of this property to [`false`](../../Swift/false.md).

## See Also

### Configuring the image view
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that determines whether the image is highlighted.
- [var tintColor: UIColor!](./tintcolor.md)
  A color used to tint template images in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/isuserinteractionenabled)*