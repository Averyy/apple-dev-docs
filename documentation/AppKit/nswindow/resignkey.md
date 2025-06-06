# resignKey()

**Framework**: AppKit  
**Kind**: method

Resigns the window’s key window status.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resignKey()
```

#### Discussion

This method sends [`resignKey()`](nswindow/resignkey().md) to the window’s first responder, sends [`windowDidResignKey(_:)`](nswindowdelegate/windowdidresignkey(_:).md) to the window’s delegate, and posts [`didResignKeyNotification`](nswindow/didresignkeynotification.md) to the default notification center.

Never invoke this method directly.

## See Also

- [func resignMain()](nswindow/resignmain.md)
  Resigns the window’s main window status.
- [var isKeyWindow: Bool](nswindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeKey: Bool](nswindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](nswindow/makekey.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func becomeKey()](nswindow/becomekey.md)
  Informs the window that it has become the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/resignkey())*