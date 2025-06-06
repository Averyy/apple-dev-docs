# gestureRecognizerShouldBegin(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if a gesture recognizer should begin interpreting touches.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) (the default) to tell the gesture recognizer to proceed with interpreting touches, [`false`](https://developer.apple.com/documentation/swift/false) to prevent it from attempting to recognize its gesture.

#### Discussion

This method is called when a gesture recognizer attempts to transition out of the [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md) state. Returning [`false`](https://developer.apple.com/documentation/swift/false) causes the gesture recognizer to transition to the [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md) state.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class  . This gesture-recognizer object is about to begin processing touches to determine if its gesture is occurring.

## See Also

- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UITouch) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIPress) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu.md)
  Asks the delegate if a gesture recognizer should receive an object representing a press.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIEvent) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:))*