# shouldRequireFailure(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden to indicate that the specified gesture recognizer must fail before the current object begins recognizing its gesture.

**Availability**:
- macOS

## Declaration

```swift
func shouldRequireFailure(of otherGestureRecognizer: NSGestureRecognizer) -> Bool
```

```objc
- (BOOL) shouldRequireFailureOfGestureRecognizer:(NSGestureRecognizer *) otherGestureRecognizer;
```

#### Return Value

[`true`](../../Swift/true.md) to cause the current object to wait to recognize its own gesture until the object in otherGestureRecognizer fails.

#### Discussion

Using this method lets you define rules that apply to all instances of your custom gesture recognizer class.

## Parameters

- `otherGestureRecognizer`: The gesture recognizer that must fail before the current object is allowed to recognize its gesture.

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
- [func otherMouseUp(with: NSEvent)](./othermouseup%28with%29.md)
  Informs the gesture recognizer that the user released a mouse button other than the left or right one.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/shouldrequirefailure(of:))*