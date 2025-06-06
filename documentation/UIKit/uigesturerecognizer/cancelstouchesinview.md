# cancelsTouchesInView

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var cancelsTouchesInView: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/swift/true) (the default) and the gesture recognizer recognizes its gesture, the touches of that gesture that are pending aren’t delivered to the view and previously delivered touches are canceled through a [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) message sent to the view. If a gesture recognizer doesn’t recognize its gesture or if the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the view receives all touches in the multi-touch sequence.

## See Also

- [var delaysTouchesBegan: Bool](uigesturerecognizer/delaystouchesbegan.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.
- [var delaysTouchesEnded: Bool](uigesturerecognizer/delaystouchesended.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/cancelstouchesinview)*