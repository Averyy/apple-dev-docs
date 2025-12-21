# showWindow(_:)

**Framework**: AppKit  
**Kind**: method

Displays the window associated with the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func showWindow(_ sender: Any?)
```

#### Discussion

If the window is an [`NSPanel`](nspanel.md) object and has its [`becomesKeyOnlyIfNeeded`](nspanel/becomeskeyonlyifneeded.md) flag set to [`true`](https://developer.apple.com/documentation/Swift/true), the window is displayed in front of all other windows but is not made key; otherwise it is displayed in front and is made key. This method is useful for menu actions.

## Parameters

- `sender`: The control sending the message; can be  .

## See Also

- [func orderFront(Any?)](nswindow/orderfront(_:).md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func loadWindow()](nswindowcontroller/loadwindow.md)
  Loads the receiver’s window from the nib file.
- [var isWindowLoaded: Bool](nswindowcontroller/iswindowloaded.md)
  A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.
- [var window: NSWindow?](nswindowcontroller/window.md)
  The window owned by the receiver.
- [func windowDidLoad()](nswindowcontroller/windowdidload.md)
  Sent after the window owned by the receiver has been loaded.
- [func windowWillLoad()](nswindowcontroller/windowwillload.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/showwindow(_:))*