# gestureRecognizer(_:shouldReceive:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if a gesture recognizer should receive an object representing a press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive press: UIPress) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) (the default) to allow the gesture recognizer to examine the press object, or [`false`](https://developer.apple.com/documentation/swift/false) to prevent the gesture recognizer from seeing this press object.

#### Discussion

UIKit calls this method before the [`pressesBegan(_:with:)`](uigesturerecognizer/pressesbegan(_:with:).md) method of the gesture recognizer.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class  .
- `press`: A   object from the current press sequence.

## See Also

- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:).md)
  Asks the delegate if a gesture recognizer should begin interpreting touches.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UITouch) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIEvent) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu)*