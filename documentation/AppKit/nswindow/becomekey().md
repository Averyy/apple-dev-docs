# becomeKey()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the window that it has become the key window.

**Availability**:
- macOS

## Declaration

```swift
func becomeKey()
```

```objc
- (void) becomeKeyWindow;
```

#### Discussion

This method reestablishes the window’s first responder, sends the `becomeKeyWindow` message to that object if it responds, and posts [`didBecomeKeyNotification`](./didbecomekeynotification.md) to the default notification center.

Never invoke this method directly.

## See Also

### Managing Key Status
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](./makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func resignKey()](./resignkey%28%29.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/becomekey())*