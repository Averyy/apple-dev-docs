# updateWindows()

**Framework**: AppKit  
**Kind**: method

Sends an [`update()`](nswindow/update().md) message to each onscreen window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func updateWindows()
```

#### Discussion

This method is invoked automatically in the main event loop after each event when running in `NSDefaultRunLoopMode` or `NSModalRunLoopMode`. This method is not invoked automatically when running in `NSEventTrackingRunLoopMode`.

When this method begins, it posts an [`willUpdateNotification`](nsapplication/willupdatenotification.md) to the default notification center. When it successfully completes, it posts an [`didUpdateNotification`](nsapplication/didupdatenotification.md).

## See Also

- [func applicationDidUpdate(Notification)](nsapplicationdelegate/applicationdidupdate(_:).md)
  Tells the delegate that the app’s windows did update.
- [func applicationWillUpdate(Notification)](nsapplicationdelegate/applicationwillupdate(_:).md)
  Tells the delegate that the app is about to update its windows.
- [func update()](nswindow/update.md)
  Updates the window.
- [func setWindowsNeedUpdate(Bool)](nsapplication/setwindowsneedupdate(_:).md)
  Sets whether the receiver’s windows need updating when the receiver has finished processing the current event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/updatewindows())*