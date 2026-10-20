# mouseDown(with:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Informs the view that the user has pressed the left mouse button.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func mouseDown(with event: NSEvent)
```

#### Discussion

The view handles the event instead of passing it to the next responder. See [`NSResponder`](../../AppKit/nsresponder.md) for more information about the responder chain.

## Parameters

- `event`: An object encapsulating information about the mouse event.

## See Also

### Handling mouse input
- [func mouseDragged(with: NSEvent)](./mousedragged%28with%29.md)
  Informs the view that the user has moved the mouse with the left button pressed.
- [func mouseUp(with: NSEvent)](./mouseup%28with%29.md)
  Informs the view that the user has released the left mouse button.
- [func mouseMoved(with: NSEvent)](./mousemoved%28with%29.md)
  Informs the view that the mouse has moved.
- [func rightMouseDown(with: NSEvent)](./rightmousedown%28with%29.md)
  Informs the view that the user has pressed the right mouse button.
- [func rightMouseDragged(with: NSEvent)](./rightmousedragged%28with%29.md)
  Informs the view that the user has moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](./rightmouseup%28with%29.md)
  Informs the view that the user has released the right mouse button.
- [func otherMouseDown(with: NSEvent)](./othermousedown%28with%29.md)
  Informs the view that the user has pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](./othermousedragged%28with%29.md)
  Informs the view that the user has moved the mouse with a button other than the left or right button pressed.
- [func otherMouseUp(with: NSEvent)](./othermouseup%28with%29.md)
  Informs the view that the user has released a mouse button other than the left or right button.
- [func scrollWheel(with: NSEvent)](./scrollwheel%28with%29.md)
  Informs the view that the mouse’s scroll wheel has moved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/mousedown(with:))*