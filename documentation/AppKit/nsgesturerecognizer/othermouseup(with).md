# otherMouseUp(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the gesture recognizer that the user released a mouse button other than the left or right one.

**Availability**:
- macOS

## Declaration

```swift
func otherMouseUp(with event: NSEvent)
```

```objc
- (void) otherMouseUp:(NSEvent *) event;
```

## Discussion

The default implementation of this method does nothing. Use this method to update the state of your gesture recognizer in whatever way is appropriate.

A gesture recognizer monitors events that occur in its view (and any subviews) but does not take part in the responder chain itself. The gesture recognizer receives events before any views do. Use the [`delaysOtherMouseButtonEvents`](./delaysothermousebuttonevents.md) property to control whether `event` is propagated to the view.

## Parameters

- `event`: An object encapsulating information about the mouse-up event.

## See Also

### Overriding methods for subclasses
- [func reset()](./reset%28%29.md)
  Overridden to reset the internal state of the gesture recognizer when an attempt completes.
- [func mouseDown(with: NSEvent)](./mousedown%28with%29.md)
  Informs the gesture recognizer that the user pressed the left mouse button.
- [func mouseDragged(with: NSEvent)](./mousedragged%28with%29.md)
  Informs the gesture recognizer that the user moved the mouse with the left button pressed.
- [func mouseUp(with: NSEvent)](./mouseup%28with%29.md)
  Informs the gesture recognizer that the user released the left mouse button.
- [func otherMouseDown(with: NSEvent)](./othermousedown%28with%29.md)
  Informs the gesture recognizer that the user pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](./othermousedragged%28with%29.md)
  Informs the gesture recognizer that the user moved the mouse with a button other than the left or right one pressed.
- [func rightMouseDown(with: NSEvent)](./rightmousedown%28with%29.md)
  Informs the gesture recognizer that the user pressed the right mouse button.
- [func rightMouseDragged(with: NSEvent)](./rightmousedragged%28with%29.md)
  Informs the gesture recognizer that the user moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](./rightmouseup%28with%29.md)
  Informs the gesture recognizer that the user released the right mouse button.
- [func magnify(with: NSEvent)](./magnify%28with%29.md)
  Informs the gesture recognizer that the user is performing a pinch gesture.
- [func rotate(with: NSEvent)](./rotate%28with%29.md)
  Informs the gesture recognizer that the user is performing a rotation gesture.
- [func canBePrevented(by: NSGestureRecognizer) -> Bool](./canbeprevented%28by%29.md)
  Overridden to indicate that the specified gesture recognizer can prevent the current object from recognizing a gesture.
- [func canPrevent(NSGestureRecognizer) -> Bool](./canprevent%28_%29.md)
  Overridden to indicate that the current object can prevent the specified gesture recognizer from recognizing its gesture.
- [func shouldBeRequiredToFail(by: NSGestureRecognizer) -> Bool](./shouldberequiredtofail%28by%29.md)
  Overridden to indicate that the current object must fail before the specified gesture recognizer begins recognizing its gesture.
- [func shouldRequireFailure(of: NSGestureRecognizer) -> Bool](./shouldrequirefailure%28of%29.md)
  Overridden to indicate that the specified gesture recognizer must fail before the current object begins recognizing its gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/othermouseup(with:))*