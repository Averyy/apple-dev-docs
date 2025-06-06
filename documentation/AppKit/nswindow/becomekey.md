# becomeKey()

**Framework**: AppKit  
**Kind**: method

Informs the window that it has become the key window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func becomeKey()
```

#### Discussion

This method reestablishes the window’s first responder, sends the `becomeKeyWindow` message to that object if it responds, and posts [`didBecomeKeyNotification`](nswindow/didbecomekeynotification.md) to the default notification center.

Never invoke this method directly.

## See Also

- [var isKeyWindow: Bool](nswindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeKey: Bool](nswindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](nswindow/makekey.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func resignKey()](nswindow/resignkey.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/becomekey())*