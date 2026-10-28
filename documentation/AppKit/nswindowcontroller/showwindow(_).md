# showWindow(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the window associated with the receiver.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func showWindow(_ sender: Any?)
```

```objc
- (void) showWindow:(id) sender;
```

## Discussion

If the window is an [`NSPanel`](../nspanel.md) object and has its [`becomesKeyOnlyIfNeeded`](../nspanel/becomeskeyonlyifneeded.md) flag set to [`true`](../../Swift/true.md), the window is displayed in front of all other windows but is not made key; otherwise it is displayed in front and is made key. This method is useful for menu actions.

## Parameters

- `sender`: The control sending the message; can be `nil`.

## See Also

### Related Documentation
- [func orderFront(Any?)](../nswindow/orderfront%28_%29.md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func makeKeyAndOrderFront(Any?)](../nswindow/makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
### Loading and Displaying the Window
- [func loadWindow()](./loadwindow%28%29.md)
  Loads the receiver’s window from the nib file.
- [var isWindowLoaded: Bool](./iswindowloaded.md)
  A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.
- [var window: NSWindow?](./window.md)
  The window owned by the receiver.
- [func windowDidLoad()](./windowdidload%28%29.md)
  Sent after the window owned by the receiver has been loaded.
- [func windowWillLoad()](./windowwillload%28%29.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/showwindow(_:))*