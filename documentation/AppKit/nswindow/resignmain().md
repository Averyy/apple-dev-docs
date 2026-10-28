# resignMain()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Resigns the window’s main window status.

**Availability**:
- macOS

## Declaration

```swift
func resignMain()
```

```objc
- (void) resignMainWindow;
```

## Discussion

This method sends [`windowDidResignMain(_:)`](../nswindowdelegate/windowdidresignmain%28_%29.md) to the window’s delegate and posts [`didResignMainNotification`](./didresignmainnotification.md) to the default notification center.

Never invoke this method directly.

## See Also

### Related Documentation
- [func resignKey()](./resignkey%28%29.md)
  Resigns the window’s key window status.
### Managing Main Status
- [var isMainWindow: Bool](./ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [var canBecomeMain: Bool](./canbecomemain.md)
  A Boolean value that indicates whether the window can become the application’s main window.
- [func makeMain()](./makemain%28%29.md)
  Makes the window the main window.
- [func becomeMain()](./becomemain%28%29.md)
  Informs the window that it has become the main window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/resignmain())*