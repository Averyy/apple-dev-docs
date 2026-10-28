# gestureRecognizer(_:shouldReceive:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if a gesture recognizer should receive an object representing a press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive press: UIPress) -> Bool
```

```objc
- (BOOL) gestureRecognizer:(UIGestureRecognizer *) gestureRecognizer shouldReceivePress:(UIPress *) press;
```

## Return Value

[`true`](../../Swift/true.md) (the default) to allow the gesture recognizer to examine the press object, or [`false`](../../Swift/false.md) to prevent the gesture recognizer from seeing this press object.

## Discussion

UIKit calls this method before the [`pressesBegan(_:with:)`](../uigesturerecognizer/pressesbegan%28_,with%29.md) method of the gesture recognizer.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md).
- `press`: A [`UIPress`](../uipress.md) object from the current press sequence.

## See Also

### Regulating gesture recognition
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](./gesturerecognizershouldbegin%28_%29.md)
  Asks the delegate if a gesture recognizer should begin interpreting touches.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UITouch) -> Bool](./gesturerecognizer%28_,shouldreceive%29-16fuh.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIEvent) -> Bool](./gesturerecognizer%28_,shouldreceive%29-evxd.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu)*