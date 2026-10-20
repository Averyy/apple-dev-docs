# delaysTouchesEnded

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var delaysTouchesEnded: Bool { get set }
```

```objc
@property (nonatomic) BOOL delaysTouchesEnded;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md) (the default) and the gesture recognizer is analyzing touch events, the window suspends delivery of touch objects in the [`UITouch.Phase.ended`](../uitouch/phase-swift.enum/ended.md) phase to the attached view. If the gesture recognizer subsequently recognizes its gesture, these touch objects are canceled (with a [`touchesCancelled(_:with:)`](../uiresponder/touchescancelled%28_,with%29.md) message). If the gesture recognizer doesn’t recognize its gesture, the window delivers these objects in an invocation of the view’s [`touchesEnded(_:with:)`](../uiresponder/touchesended%28_,with%29.md) method. Set this property to [`false`](../../Swift/false.md) to have touch objects in the [`UITouch.Phase.ended`](../uitouch/phase-swift.enum/ended.md) delivered to the view while the gesture recognizer is analyzing the same touches.

## See Also

### Canceling and delaying touches
- [var cancelsTouchesInView: Bool](./cancelstouchesinview.md)
  A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.
- [var delaysTouchesBegan: Bool](./delaystouchesbegan.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/delaystouchesended)*