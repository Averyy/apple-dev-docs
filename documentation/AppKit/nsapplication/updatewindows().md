# updateWindows()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sends an [`update()`](../nswindow/update%28%29.md) message to each onscreen window.

**Availability**:
- macOS

## Declaration

```swift
func updateWindows()
```

```objc
- (void) updateWindows;
```

#### Discussion

This method is invoked automatically in the main event loop after each event when running in `NSDefaultRunLoopMode` or `NSModalRunLoopMode`. This method is not invoked automatically when running in `NSEventTrackingRunLoopMode`.

When this method begins, it posts an [`willUpdateNotification`](./willupdatenotification.md) to the default notification center. When it successfully completes, it posts an [`didUpdateNotification`](./didupdatenotification.md).

## See Also

### Related Documentation
- [func applicationDidUpdate(Notification)](../nsapplicationdelegate/applicationdidupdate%28_%29.md)
  Tells the delegate that the app’s windows did update.
- [func applicationWillUpdate(Notification)](../nsapplicationdelegate/applicationwillupdate%28_%29.md)
  Tells the delegate that the app is about to update its windows.
- [func update()](../nswindow/update%28%29.md)
  Updates the window.
### Updating Windows
- [func setWindowsNeedUpdate(Bool)](./setwindowsneedupdate%28_%29.md)
  Sets whether the receiver’s windows need updating when the receiver has finished processing the current event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/updatewindows())*