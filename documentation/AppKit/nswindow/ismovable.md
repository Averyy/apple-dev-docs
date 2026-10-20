# isMovable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window can be dragged by clicking in its title bar or background.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isMovable: Bool { get set }
```

```objc
@property (getter=isMovable) BOOL movable;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the window can be moved by the user; otherwise, [`false`](../../Swift/false.md).

When a window’s [`isMovable`](./ismovable.md) property is [`false`](../../Swift/false.md), the value of the [`isMovableByWindowBackground`](./ismovablebywindowbackground.md) property is ignored. When the value of [`isMovable`](./ismovable.md) is [`false`](../../Swift/false.md), the window can only be dragged between spaces in F8 mode, and its relative screen position is always preserved. Note that a resizable window may still be resized, and the window frame may be changed programmatically. A nonmovable window will not be moved or resized by the system in response to a display reconfiguration. Applications may choose to enable application-controlled window dragging after disabling user-initiating dragging by handling the [`mouseDown(with:)`](../nsresponder/mousedown%28with%29.md)/[`mouseDragged(with:)`](../nsresponder/mousedragged%28with%29.md)/[`mouseUp(with:)`](../nsresponder/mouseup%28with%29.md) sequence in [`sendEvent(_:)`](./sendevent%28_%29.md) in an `NSWindow` subclass.

## See Also

### Moving Windows
- [var isMovableByWindowBackground: Bool](./ismovablebywindowbackground.md)
  A Boolean value that indicates whether the window is movable by clicking and dragging anywhere in its background.
- [func center()](./center%28%29.md)
  Sets the window’s location to the center of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/ismovable)*