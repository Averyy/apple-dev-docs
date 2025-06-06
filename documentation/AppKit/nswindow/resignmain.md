# resignMain()

**Framework**: AppKit  
**Kind**: method

Resigns the window’s main window status.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resignMain()
```

#### Discussion

This method sends [`windowDidResignMain(_:)`](nswindowdelegate/windowdidresignmain(_:).md) to the window’s delegate and posts [`didResignMainNotification`](nswindow/didresignmainnotification.md) to the default notification center.

Never invoke this method directly.

## See Also

- [func resignKey()](nswindow/resignkey.md)
  Resigns the window’s key window status.
- [var isMainWindow: Bool](nswindow/ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [var canBecomeMain: Bool](nswindow/canbecomemain.md)
  A Boolean value that indicates whether the window can become the application’s main window.
- [func makeMain()](nswindow/makemain.md)
  Makes the window the main window.
- [func becomeMain()](nswindow/becomemain.md)
  Informs the window that it has become the main window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/resignmain())*