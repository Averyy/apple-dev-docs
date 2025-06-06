# unhideWithoutActivation()

**Framework**: AppKit  
**Kind**: method

Restores hidden windows without activating their owner (the receiver).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func unhideWithoutActivation()
```

#### Discussion

When this method begins, it posts an [`willUnhideNotification`](nsapplication/willunhidenotification.md) to the default notification center. If it completes successfully, it posts an [`didUnhideNotification`](nsapplication/didunhidenotification.md).

## See Also

- [func activate(ignoringOtherApps: Bool)](nsapplication/activate(ignoringotherapps:).md)
  Makes the receiver the active app.
- [func applicationDidUnhide(Notification)](nsapplicationdelegate/applicationdidunhide(_:).md)
  Tells the delegate that the app is now visible.
- [func applicationWillUnhide(Notification)](nsapplicationdelegate/applicationwillunhide(_:).md)
  Tells the delegate that the app is about to become visible.
- [var isHidden: Bool](nsapplication/ishidden.md)
  A Boolean value indicating whether the app is hidden.
- [func hide(Any?)](nsapplication/hide(_:).md)
  Hides all the receiver’s windows, and the next app in line is activated.
- [func unhide(Any?)](nsapplication/unhide(_:).md)
  Restores hidden windows to the screen and makes the receiver active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unhidewithoutactivation())*