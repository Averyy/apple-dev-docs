# delaysTouchesBegan

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var delaysTouchesBegan: Bool { get set }
```

```objc
@property (nonatomic) BOOL delaysTouchesBegan;
```

#### Discussion

When the value of this property is [`false`](../../Swift/false.md) (the default), views analyze touch events in [`UITouch.Phase.began`](../uitouch/phase-swift.enum/began.md) and [`UITouch.Phase.moved`](../uitouch/phase-swift.enum/moved.md) in parallel with the gesture recognizer. When the value of the property is [`true`](../../Swift/true.md), the window suspends delivery of touch objects in the [`UITouch.Phase.began`](../uitouch/phase-swift.enum/began.md) phase to the view. If the gesture recognizer subsequently recognizes its gesture, these touch objects are discarded. If the gesture recognizer, however, doesn’t recognize its gesture, the window delivers these objects to the view in a [`touchesBegan(_:with:)`](../uiresponder/touchesbegan%28_,with%29.md) message (and possibly a follow-up [`touchesMoved(_:with:)`](../uiresponder/touchesmoved%28_,with%29.md) message to inform it of the touches’ current locations). Set this property to [`true`](../../Swift/true.md) to prevent views from processing any touches in the [`UITouch.Phase.began`](../uitouch/phase-swift.enum/began.md) phase that may be recognized as part of this gesture.

## See Also

### Canceling and delaying touches
- [var cancelsTouchesInView: Bool](./cancelstouchesinview.md)
  A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.
- [var delaysTouchesEnded: Bool](./delaystouchesended.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/delaystouchesbegan)*