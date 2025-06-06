# rightMouseDown(with:)

**Framework**: Appkit  
**Kind**: method

Informs the receiver that the user has pressed the right mouse button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rightMouseDown(with event: NSEvent)
```

#### Discussion

The default implementation simply passes this message to the next responder.

> **Note**:  Prior to OS X v10.7, [`NSView`](nsview.md) did not pass unhandled [`rightMouseDown(with:)`](nsresponder/rightmousedown(with:).md) events up the responder chain. In macOS 10.7 and later, [`NSView`](nsview.md) passes [`rightMouseDown(with:)`](nsresponder/rightmousedown(with:).md) events up the responder chain if AppKit doesn’t find an associated context menu to display for the view. To avoid binary compatibility issues, this new behavior is enabled only for applications linked on macOS 10.7 or later.

## Parameters

- `event`: An object encapsulating information about the mouse-down event.

## See Also

- [func mouseDown(with: NSEvent)](nsresponder/mousedown(with:).md)
  Informs the receiver that the user has pressed the left mouse button.
- [func mouseDragged(with: NSEvent)](nsresponder/mousedragged(with:).md)
  Informs the receiver that the user has moved the mouse with the left button pressed.
- [func mouseUp(with: NSEvent)](nsresponder/mouseup(with:).md)
  Informs the receiver that the user has released the left mouse button.
- [func mouseMoved(with: NSEvent)](nsresponder/mousemoved(with:).md)
  Informs the receiver that the mouse has moved.
- [func mouseEntered(with: NSEvent)](nsresponder/mouseentered(with:).md)
  Informs the receiver that the cursor has entered a tracking rectangle.
- [func mouseExited(with: NSEvent)](nsresponder/mouseexited(with:).md)
  Informs the receiver that the cursor has exited a tracking rectangle.
- [func rightMouseDragged(with: NSEvent)](nsresponder/rightmousedragged(with:).md)
  Informs the receiver that the user has moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](nsresponder/rightmouseup(with:).md)
  Informs the receiver that the user has released the right mouse button.
- [func otherMouseDown(with: NSEvent)](nsresponder/othermousedown(with:).md)
  Informs the receiver that the user has pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](nsresponder/othermousedragged(with:).md)
  Informs the receiver that the user has moved the mouse with a button other than the left or right button pressed.
- [func otherMouseUp(with: NSEvent)](nsresponder/othermouseup(with:).md)
  Informs the receiver that the user has released a mouse button other than the left or right button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/rightmousedown(with:))*