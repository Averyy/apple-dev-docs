# isMovable

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window can be dragged by clicking in its title bar or background.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var isMovable: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the window can be moved by the user; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

When a window’s [`isMovable`](nswindow/ismovable.md) property is [`false`](https://developer.apple.com/documentation/swift/false), the value of the [`isMovableByWindowBackground`](nswindow/ismovablebywindowbackground.md) property is ignored. When the value of [`isMovable`](nswindow/ismovable.md) is [`false`](https://developer.apple.com/documentation/swift/false), the window can only be dragged between spaces in F8 mode, and its relative screen position is always preserved. Note that a resizable window may still be resized, and the window frame may be changed programmatically. A nonmovable window will not be moved or resized by the system in response to a display reconfiguration. Applications may choose to enable application-controlled window dragging after disabling user-initiating dragging by handling the [`mouseDown(with:)`](nsresponder/mousedown(with:).md)/[`mouseDragged(with:)`](nsresponder/mousedragged(with:).md)/[`mouseUp(with:)`](nsresponder/mouseup(with:).md) sequence in [`sendEvent(_:)`](nswindow/sendevent(_:).md) in an `NSWindow` subclass.

## See Also

- [var isMovableByWindowBackground: Bool](nswindow/ismovablebywindowbackground.md)
  A Boolean value that indicates whether the window is movable by clicking and dragging anywhere in its background.
- [func center()](nswindow/center.md)
  Sets the window’s location to the center of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/ismovable)*