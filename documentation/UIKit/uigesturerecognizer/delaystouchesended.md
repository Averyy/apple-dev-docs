# delaysTouchesEnded

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var delaysTouchesEnded: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) (the default) and the gesture recognizer is analyzing touch events, the window suspends delivery of touch objects in the [`UITouch.Phase.ended`](uitouch/phase-swift.enum/ended.md) phase to the attached view. If the gesture recognizer subsequently recognizes its gesture, these touch objects are canceled (with a [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) message). If the gesture recognizer doesn’t recognize its gesture, the window delivers these objects in an invocation of the view’s [`touchesEnded(_:with:)`](uiresponder/touchesended(_:with:).md) method. Set this property to [`false`](https://developer.apple.com/documentation/swift/false) to have touch objects in the [`UITouch.Phase.ended`](uitouch/phase-swift.enum/ended.md) delivered to the view while the gesture recognizer is analyzing the same touches.

## See Also

- [var cancelsTouchesInView: Bool](uigesturerecognizer/cancelstouchesinview.md)
  A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.
- [var delaysTouchesBegan: Bool](uigesturerecognizer/delaystouchesbegan.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/delaystouchesended)*