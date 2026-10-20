# becomeMain()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the window that it has become the main window.

**Availability**:
- macOS

## Declaration

```swift
func becomeMain()
```

```objc
- (void) becomeMainWindow;
```

#### Discussion

This method posts an [`didBecomeMainNotification`](./didbecomemainnotification.md) to the default notification center.

Never invoke this method directly.

## See Also

### Related Documentation
- [func becomeKey()](./becomekey%28%29.md)
  Informs the window that it has become the key window.
### Managing Main Status
- [var isMainWindow: Bool](./ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [var canBecomeMain: Bool](./canbecomemain.md)
  A Boolean value that indicates whether the window can become the application’s main window.
- [func makeMain()](./makemain%28%29.md)
  Makes the window the main window.
- [func resignMain()](./resignmain%28%29.md)
  Resigns the window’s main window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/becomemain())*