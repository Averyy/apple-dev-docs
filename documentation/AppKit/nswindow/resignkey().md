# resignKey()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Resigns the window’s key window status.

**Availability**:
- macOS

## Declaration

```swift
func resignKey()
```

```objc
- (void) resignKeyWindow;
```

## Discussion

This method sends [`resignKey()`](./resignkey%28%29.md) to the window’s first responder, sends [`windowDidResignKey(_:)`](../nswindowdelegate/windowdidresignkey%28_%29.md) to the window’s delegate, and posts [`didResignKeyNotification`](./didresignkeynotification.md) to the default notification center.

Never invoke this method directly.

## See Also

### Related Documentation
- [func resignMain()](./resignmain%28%29.md)
  Resigns the window’s main window status.
### Managing Key Status
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](./makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func becomeKey()](./becomekey%28%29.md)
  Informs the window that it has become the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/resignkey())*