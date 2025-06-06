# gestureRecognizer(_:shouldReceive:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive event: UIEvent) -> Bool
```

#### Return Value

Return [`false`](https://developer.apple.com/documentation/swift/false) to prevent the gesture recognizer from seeing this event.

#### Discussion

UIKit calls this method once before either the [`gestureRecognizer(_:shouldReceive:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu.md) method or the [`gestureRecognizer(_:shouldReceive:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh.md) method of the gesture recognizer.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class  .
- `event`: A   object from the current press or touch sequence.

## See Also

- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:).md)
  Asks the delegate if a gesture recognizer should begin interpreting touches.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UITouch) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIPress) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu.md)
  Asks the delegate if a gesture recognizer should receive an object representing a press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd)*