# level

**Framework**: AppKit  
**Kind**: property

The window level of the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var level: NSWindow.Level { get set }
```

#### Discussion

See `Window Levels` for a list of possible values. Each level in the list groups windows within it in front of those in all preceding groups. Floating windows, for example, appear in front of all normal-level windows.

The constant `NSTornOffMenuWindowLevel` is preferable to its synonym, `NSSubmenuWindowLevel`.

## See Also

- [func orderOut(Any?)](nswindow/orderout(_:).md)
  Removes the window from the screen list, which hides the window.
- [func orderBack(Any?)](nswindow/orderback(_:).md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](nswindow/orderfront(_:).md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](nswindow/orderfrontregardless.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](nswindow/order(_:relativeto:).md)
  Repositions the window’s window device in the window server’s screen list.
- [NSWindow.Level](nswindow/level-swift.struct.md)
  The standard window levels in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/level-swift.property)*