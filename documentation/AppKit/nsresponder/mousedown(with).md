# mouseDown(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that the user has pressed the left mouse button.

**Availability**:
- macOS

## Declaration

```swift
func mouseDown(with event: NSEvent)
```

```objc
- (void) mouseDown:(NSEvent *) event;
```

## Mentions

- [Supporting Continuity Camera in Your Mac App](../supporting-continuity-camera-in-your-mac-app.md)

## Discussion

The default implementation simply passes this message to the next responder.

## Parameters

- `event`: An object encapsulating information about the mouse-down event.

## See Also

### Responding to Mouse Events
- [func mouseDragged(with: NSEvent)](./mousedragged%28with%29.md)
  Informs the receiver that the user has moved the mouse with the left button pressed.
- [func mouseUp(with: NSEvent)](./mouseup%28with%29.md)
  Informs the receiver that the user has released the left mouse button.
- [func mouseMoved(with: NSEvent)](./mousemoved%28with%29.md)
  Informs the receiver that the mouse has moved.
- [func mouseEntered(with: NSEvent)](./mouseentered%28with%29.md)
  Informs the receiver that the cursor has entered a tracking rectangle.
- [func mouseExited(with: NSEvent)](./mouseexited%28with%29.md)
  Informs the receiver that the cursor has exited a tracking rectangle.
- [func rightMouseDown(with: NSEvent)](./rightmousedown%28with%29.md)
  Informs the receiver that the user has pressed the right mouse button.
- [func rightMouseDragged(with: NSEvent)](./rightmousedragged%28with%29.md)
  Informs the receiver that the user has moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](./rightmouseup%28with%29.md)
  Informs the receiver that the user has released the right mouse button.
- [func otherMouseDown(with: NSEvent)](./othermousedown%28with%29.md)
  Informs the receiver that the user has pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](./othermousedragged%28with%29.md)
  Informs the receiver that the user has moved the mouse with a button other than the left or right button pressed.
- [func otherMouseUp(with: NSEvent)](./othermouseup%28with%29.md)
  Informs the receiver that the user has released a mouse button other than the left or right button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/mousedown(with:))*