# gestureRecognizerShouldBegin(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if a gesture recognizer should begin interpreting touches.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool
```

```objc
- (BOOL) gestureRecognizerShouldBegin:(UIGestureRecognizer *) gestureRecognizer;
```

## Return Value

[`true`](../../Swift/true.md) (the default) to tell the gesture recognizer to proceed with interpreting touches, [`false`](../../Swift/false.md) to prevent it from attempting to recognize its gesture.

## Discussion

This method is called when a gesture recognizer attempts to transition out of the [`UIGestureRecognizer.State.possible`](../uigesturerecognizer/state-swift.enum/possible.md) state. Returning [`false`](../../Swift/false.md) causes the gesture recognizer to transition to the [`UIGestureRecognizer.State.failed`](../uigesturerecognizer/state-swift.enum/failed.md) state.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md). This gesture-recognizer object is about to begin processing touches to determine if its gesture is occurring.

## See Also

### Regulating gesture recognition
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UITouch) -> Bool](./gesturerecognizer%28_,shouldreceive%29-16fuh.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIPress) -> Bool](./gesturerecognizer%28_,shouldreceive%29-73vzu.md)
  Asks the delegate if a gesture recognizer should receive an object representing a press.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIEvent) -> Bool](./gesturerecognizer%28_,shouldreceive%29-evxd.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:))*