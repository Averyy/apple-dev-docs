# gestureRecognizer(_:shouldReceive:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if a gesture recognizer should receive an object representing a touch.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive touch: UITouch) -> Bool
```

```objc
- (BOOL) gestureRecognizer:(UIGestureRecognizer *) gestureRecognizer shouldReceiveTouch:(UITouch *) touch;
```

#### Return Value

[`true`](../../Swift/true.md) (the default) to allow the gesture recognizer to examine the touch object, [`false`](../../Swift/false.md) to prevent the gesture recognizer from seeing this touch object.

#### Discussion

UIKit calls this method before calling the [`touchesBegan(_:with:)`](../uigesturerecognizer/touchesbegan%28_,with%29.md) method of the gesture recognizer.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md).
- `touch`: A [`UITouch`](../uitouch.md) object from the current multi-touch sequence.

## See Also

### Regulating gesture recognition
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](./gesturerecognizershouldbegin%28_%29.md)
  Asks the delegate if a gesture recognizer should begin interpreting touches.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIPress) -> Bool](./gesturerecognizer%28_,shouldreceive%29-73vzu.md)
  Asks the delegate if a gesture recognizer should receive an object representing a press.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIEvent) -> Bool](./gesturerecognizer%28_,shouldreceive%29-evxd.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh)*