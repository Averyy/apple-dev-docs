# canPrevent(_:)

**Framework**: AppKit  
**Kind**: method

Overridden to indicate that the current object can prevent the specified gesture recognizer from recognizing its gesture.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func canPrevent(_ preventedGestureRecognizer: NSGestureRecognizer) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to indicate that `preventedGestureRecognizer` should be blocked from recognizing its gesture, or [`false`](https://developer.apple.com/documentation/Swift/false) if both gesture recognizers can operate simultaneously.

#### Discussion

This method enables similar behavior as the [`gestureRecognizerShouldBegin(_:)`](nsgesturerecognizerdelegate/gesturerecognizershouldbegin(_:).md) and [`gestureRecognizer(_:shouldRequireFailureOf:)`](nsgesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md) methods of the gesture recognizer’s delegate. Using this method lets you define rules that apply to all instances of your custom gesture recognizer class. For example, an [`NSClickGestureRecognizer`](nsclickgesturerecognizer.md) object does not prevent another [`NSClickGestureRecognizer`](nsclickgesturerecognizer.md) object with a higher click count from recognizing its gesture.

## Parameters

- `preventedGestureRecognizer`: The gesture recognizer to be prevented from recognizing its gesture.

## See Also

- [func reset()](nsgesturerecognizer/reset.md)
  Overridden to reset the internal state of the gesture recognizer when an attempt completes.
- [func mouseDown(with: NSEvent)](nsgesturerecognizer/mousedown(with:).md)
  Informs the gesture recognizer that the user pressed the left mouse button.
- [func mouseDragged(with: NSEvent)](nsgesturerecognizer/mousedragged(with:).md)
  Informs the gesture recognizer that the user moved the mouse with the left button pressed.
- [func mouseUp(with: NSEvent)](nsgesturerecognizer/mouseup(with:).md)
  Informs the gesture recognizer that the user released the left mouse button.
- [func otherMouseDown(with: NSEvent)](nsgesturerecognizer/othermousedown(with:).md)
  Informs the gesture recognizer that the user pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](nsgesturerecognizer/othermousedragged(with:).md)
  Informs the gesture recognizer that the user moved the mouse with a button other than the left or right one pressed.
- [func otherMouseUp(with: NSEvent)](nsgesturerecognizer/othermouseup(with:).md)
  Informs the gesture recognizer that the user released a mouse button other than the left or right one.
- [func rightMouseDown(with: NSEvent)](nsgesturerecognizer/rightmousedown(with:).md)
  Informs the gesture recognizer that the user pressed the right mouse button.
- [func rightMouseDragged(with: NSEvent)](nsgesturerecognizer/rightmousedragged(with:).md)
  Informs the gesture recognizer that the user moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](nsgesturerecognizer/rightmouseup(with:).md)
  Informs the gesture recognizer that the user released the right mouse button.
- [func magnify(with: NSEvent)](nsgesturerecognizer/magnify(with:).md)
  Informs the gesture recognizer that the user is performing a pinch gesture.
- [func rotate(with: NSEvent)](nsgesturerecognizer/rotate(with:).md)
  Informs the gesture recognizer that the user is performing a rotation gesture.
- [func canBePrevented(by: NSGestureRecognizer) -> Bool](nsgesturerecognizer/canbeprevented(by:).md)
  Overridden to indicate that the specified gesture recognizer can prevent the current object from recognizing a gesture.
- [func shouldBeRequiredToFail(by: NSGestureRecognizer) -> Bool](nsgesturerecognizer/shouldberequiredtofail(by:).md)
  Overridden to indicate that the current object must fail before the specified gesture recognizer begins recognizing its gesture.
- [func shouldRequireFailure(of: NSGestureRecognizer) -> Bool](nsgesturerecognizer/shouldrequirefailure(of:).md)
  Overridden to indicate that the specified gesture recognizer must fail before the current object begins recognizing its gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/canprevent(_:))*