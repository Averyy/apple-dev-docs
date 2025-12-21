# allowedScrollTypesMask

**Framework**: UIKit  
**Kind**: property

A scroll type mask that enables recognition of scroll events.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowedScrollTypesMask: UIScrollTypeMask { get set }
```

#### Discussion

Setting this mask enables the pan gesture to recognize scroll events, like a mouse scroll movement or a two-finger scroll on a track pad. See [`UIScrollType`](uiscrolltype.md).

> **Note**:  Setting this property doesn’t disable scrolling through touches. To disable touch scrolling, return [`false`](https://developer.apple.com/documentation/Swift/false) from [`gestureRecognizer(_:shouldReceive:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh.md) or set the [`allowedTouchTypes`](uigesturerecognizer/allowedtouchtypes.md) to an empty array.

## See Also

- [struct UIScrollTypeMask](uiscrolltypemask.md)
  A bit mask identifying the scroll type of a pan gesture.
- [enum UIScrollType](uiscrolltype.md)
  Constants that define the type of the scroll.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/allowedscrolltypesmask)*