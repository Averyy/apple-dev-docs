# orderBack(_:)

**Framework**: AppKit  
**Kind**: method

Moves the window to the back of its level in the screen list, without changing either the key window or the main window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func orderBack(_ sender: Any?)
```

## Parameters

- `sender`: Message originator.

## See Also

- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func orderOut(Any?)](nswindow/orderout(_:).md)
  Removes the window from the screen list, which hides the window.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/orderback(_:))*