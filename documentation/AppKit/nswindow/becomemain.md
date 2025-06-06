# becomeMain()

**Framework**: AppKit  
**Kind**: method

Informs the window that it has become the main window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func becomeMain()
```

#### Discussion

This method posts an [`didBecomeMainNotification`](nswindow/didbecomemainnotification.md) to the default notification center.

Never invoke this method directly.

## See Also

- [func becomeKey()](nswindow/becomekey.md)
  Informs the window that it has become the key window.
- [var isMainWindow: Bool](nswindow/ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [var canBecomeMain: Bool](nswindow/canbecomemain.md)
  A Boolean value that indicates whether the window can become the application’s main window.
- [func makeMain()](nswindow/makemain.md)
  Makes the window the main window.
- [func resignMain()](nswindow/resignmain.md)
  Resigns the window’s main window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/becomemain())*