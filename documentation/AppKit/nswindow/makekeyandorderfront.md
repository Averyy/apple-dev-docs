# makeKeyAndOrderFront(_:)

**Framework**: AppKit  
**Kind**: method

Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func makeKeyAndOrderFront(_ sender: Any?)
```

## Parameters

- `sender`: The message’s sender.

## See Also

- [func orderBack(Any?)](nswindow/orderback(_:).md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](nswindow/orderfront(_:).md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [var level: NSWindow.Level](nswindow/level-swift.property.md)
  The window level of the window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](nswindow/order(_:relativeto:).md)
  Repositions the window’s window device in the window server’s screen list.
- [func orderOut(Any?)](nswindow/orderout(_:).md)
  Removes the window from the screen list, which hides the window.
- [var isKeyWindow: Bool](nswindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeKey: Bool](nswindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](nswindow/makekey.md)
  Makes the window the key window.
- [func becomeKey()](nswindow/becomekey.md)
  Informs the window that it has become the key window.
- [func resignKey()](nswindow/resignkey.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/makekeyandorderfront(_:))*