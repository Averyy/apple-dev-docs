# mouseUp(with:)

**Framework**: RealityKit  
**Kind**: method

Informs the view that the user has released the left mouse button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func mouseUp(with event: NSEvent)
```

#### Discussion

The view handles the event instead of passing it to the next responder. See [`NSResponder`](https://developer.apple.com/documentation/AppKit/NSResponder) for more information about the responder chain.

## Parameters

- `event`: An object encapsulating information about the mouse event.

## See Also

- [func mouseDown(with: NSEvent)](arview/mousedown(with:).md)
  Informs the view that the user has pressed the left mouse button.
- [func mouseDragged(with: NSEvent)](arview/mousedragged(with:).md)
  Informs the view that the user has moved the mouse with the left button pressed.
- [func mouseMoved(with: NSEvent)](arview/mousemoved(with:).md)
  Informs the view that the mouse has moved.
- [func rightMouseDown(with: NSEvent)](arview/rightmousedown(with:).md)
  Informs the view that the user has pressed the right mouse button.
- [func rightMouseDragged(with: NSEvent)](arview/rightmousedragged(with:).md)
  Informs the view that the user has moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](arview/rightmouseup(with:).md)
  Informs the view that the user has released the right mouse button.
- [func otherMouseDown(with: NSEvent)](arview/othermousedown(with:).md)
  Informs the view that the user has pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](arview/othermousedragged(with:).md)
  Informs the view that the user has moved the mouse with a button other than the left or right button pressed.
- [func otherMouseUp(with: NSEvent)](arview/othermouseup(with:).md)
  Informs the view that the user has released a mouse button other than the left or right button.
- [func scrollWheel(with: NSEvent)](arview/scrollwheel(with:).md)
  Informs the view that the mouse’s scroll wheel has moved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/mouseup(with:))*