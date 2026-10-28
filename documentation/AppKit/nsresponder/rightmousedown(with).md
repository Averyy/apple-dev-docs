# rightMouseDown(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that the user has pressed the right mouse button.

**Availability**:
- macOS

## Declaration

```swift
func rightMouseDown(with event: NSEvent)
```

```objc
- (void) rightMouseDown:(NSEvent *) event;
```

## Discussion

The default implementation simply passes this message to the next responder.

> **Note**:  Prior to OS X v10.7, [`NSView`](../nsview.md) did not pass unhandled [`rightMouseDown(with:)`](./rightmousedown%28with%29.md) events up the responder chain. In macOS 10.7 and later, [`NSView`](../nsview.md) passes [`rightMouseDown(with:)`](./rightmousedown%28with%29.md) events up the responder chain if AppKit doesn’t find an associated context menu to display for the view. To avoid binary compatibility issues, this new behavior is enabled only for applications linked on macOS 10.7 or later.

## Parameters

- `event`: An object encapsulating information about the mouse-down event.

## See Also

### Responding to Mouse Events
- [func mouseDown(with: NSEvent)](./mousedown%28with%29.md)
  Informs the receiver that the user has pressed the left mouse button.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/rightmousedown(with:))*