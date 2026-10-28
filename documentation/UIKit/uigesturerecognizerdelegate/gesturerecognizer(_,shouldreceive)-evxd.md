# gestureRecognizer(_:shouldReceive:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive event: UIEvent) -> Bool
```

```objc
- (BOOL) gestureRecognizer:(UIGestureRecognizer *) gestureRecognizer shouldReceiveEvent:(UIEvent *) event;
```

## Return Value

Return [`false`](../../Swift/false.md) to prevent the gesture recognizer from seeing this event.

## Discussion

UIKit calls this method once before either the [`gestureRecognizer(_:shouldReceive:)`](./gesturerecognizer%28_,shouldreceive%29-73vzu.md) method or the [`gestureRecognizer(_:shouldReceive:)`](./gesturerecognizer%28_,shouldreceive%29-16fuh.md) method of the gesture recognizer.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md).
- `event`: A [`UIEvent`](../uievent.md) object from the current press or touch sequence.

## See Also

### Regulating gesture recognition
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](./gesturerecognizershouldbegin%28_%29.md)
  Asks the delegate if a gesture recognizer should begin interpreting touches.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UITouch) -> Bool](./gesturerecognizer%28_,shouldreceive%29-16fuh.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIPress) -> Bool](./gesturerecognizer%28_,shouldreceive%29-73vzu.md)
  Asks the delegate if a gesture recognizer should receive an object representing a press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd)*