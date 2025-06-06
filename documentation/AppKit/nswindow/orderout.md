# orderOut(_:)

**Framework**: AppKit  
**Kind**: method

Removes the window from the screen list, which hides the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func orderOut(_ sender: Any?)
```

#### Discussion

If the window is the key or main window, the window object immediately behind it is made key or main in its place. Calling [`orderOut(_:)`](nswindow/orderout(_:).md) causes the window to be removed from the screen, but does not cause it to be released. See the [`close()`](nswindow/close().md) method for information on when a window is released. Calling [`orderOut(_:)`](nswindow/orderout(_:).md) on a child window causes the window to be removed from its parent window before being removed.

The default animation based on the window type will be used when the window is ordered out unless it has been modified by the [`animationBehavior`](nswindow/animationbehavior-swift.property.md) property.

## Parameters

- `sender`: The window to remove.

## See Also

- [var isReleasedWhenClosed: Bool](nswindow/isreleasedwhenclosed.md)
  A Boolean value that indicates whether the window is released when it receives the `close` message.
- [func orderBack(Any?)](nswindow/orderback(_:).md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](nswindow/orderfront(_:).md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](nswindow/orderfrontregardless.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](nswindow/order(_:relativeto:).md)
  Repositions the window’s window device in the window server’s screen list.
- [var level: NSWindow.Level](nswindow/level-swift.property.md)
  The window level of the window.
- [NSWindow.Level](nswindow/level-swift.struct.md)
  The standard window levels in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/orderout(_:))*