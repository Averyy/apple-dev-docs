# mouseDown(with:)

**Framework**: AppKit  
**Kind**: method

Informs the gesture recognizer that the user pressed the left mouse button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func mouseDown(with event: NSEvent)
```

#### Discussion

The default implementation of this method does nothing. Use this method to start tracking the gesture in whatever way is appropriate.

A gesture recognizer monitors events that occur in its view (and any subviews) but does not take part in the responder chain itself. The gesture recognizer receives events before any views do. Use the [`delaysPrimaryMouseButtonEvents`](nsgesturerecognizer/delaysprimarymousebuttonevents.md) property to control whether `event` is propagated to the view.

## Parameters

- `event`: An object encapsulating information about the mouse-down event.

## See Also

- [func reset()](nsgesturerecognizer/reset.md)
  Overridden to reset the internal state of the gesture recognizer when an attempt completes.
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
- [func canPrevent(NSGestureRecognizer) -> Bool](nsgesturerecognizer/canprevent(_:).md)
  Overridden to indicate that the current object can prevent the specified gesture recognizer from recognizing its gesture.
- [func shouldBeRequiredToFail(by: NSGestureRecognizer) -> Bool](nsgesturerecognizer/shouldberequiredtofail(by:).md)
  Overridden to indicate that the current object must fail before the specified gesture recognizer begins recognizing its gesture.
- [func shouldRequireFailure(of: NSGestureRecognizer) -> Bool](nsgesturerecognizer/shouldrequirefailure(of:).md)
  Overridden to indicate that the specified gesture recognizer must fail before the current object begins recognizing its gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/mousedown(with:))*