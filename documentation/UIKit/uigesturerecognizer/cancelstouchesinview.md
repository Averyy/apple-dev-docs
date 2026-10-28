# cancelsTouchesInView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var cancelsTouchesInView: Bool { get set }
```

```objc
@property (nonatomic) BOOL cancelsTouchesInView;
```

## Discussion

When this property is [`true`](../../Swift/true.md) (the default) and the gesture recognizer recognizes its gesture, the touches of that gesture that are pending aren’t delivered to the view and previously delivered touches are canceled through a [`touchesCancelled(_:with:)`](../uiresponder/touchescancelled%28_,with%29.md) message sent to the view. If a gesture recognizer doesn’t recognize its gesture or if the value of this property is [`false`](../../Swift/false.md), the view receives all touches in the multi-touch sequence.

## See Also

### Canceling and delaying touches
- [var delaysTouchesBegan: Bool](./delaystouchesbegan.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.
- [var delaysTouchesEnded: Bool](./delaystouchesended.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/cancelstouchesinview)*