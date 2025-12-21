# gestureRecognizer(_:shouldReceive:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if a gesture recognizer should receive an object representing a touch.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive touch: UITouch) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) (the default) to allow the gesture recognizer to examine the touch object, [`false`](https://developer.apple.com/documentation/Swift/false) to prevent the gesture recognizer from seeing this touch object.

#### Discussion

UIKit calls this method before calling the [`touchesBegan(_:with:)`](uigesturerecognizer/touchesbegan(_:with:).md) method of the gesture recognizer.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class  .
- `touch`: A   object from the current multi-touch sequence.

## See Also

- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:).md)
  Asks the delegate if a gesture recognizer should begin interpreting touches.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIPress) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu.md)
  Asks the delegate if a gesture recognizer should receive an object representing a press.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIEvent) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh)*