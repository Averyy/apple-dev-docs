# order(_:relativeTo:)

**Framework**: AppKit  
**Kind**: method

Repositions the window’s window device in the window server’s screen list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func order(_ place: NSWindow.OrderingMode, relativeTo otherWin: Int)
```

## Parameters

- `place`: -  : The window is removed from the screen list and   is ignored.
- `otherWin`: The number of the window the window is to be placed in front of or behind. Pass   to place the window in front of (when   is  ) or behind (when   is  ) all other windows in its level.

## See Also

- [var windowNumber: Int](nswindow/windownumber.md)
  The window number of the window’s window device.
- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func orderOut(Any?)](nswindow/orderout(_:).md)
  Removes the window from the screen list, which hides the window.
- [func orderBack(Any?)](nswindow/orderback(_:).md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](nswindow/orderfront(_:).md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](nswindow/orderfrontregardless.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [var level: NSWindow.Level](nswindow/level-swift.property.md)
  The window level of the window.
- [NSWindow.Level](nswindow/level-swift.struct.md)
  The standard window levels in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/order(_:relativeto:))*