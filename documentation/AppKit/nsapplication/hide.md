# hide(_:)

**Framework**: AppKit  
**Kind**: method

Hides all the receiver’s windows, and the next app in line is activated.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func hide(_ sender: Any?)
```

#### Discussion

This method is usually invoked when the user chooses Hide in the app’s main menu. When this method begins, it posts an [`willHideNotification`](nsapplication/willhidenotification.md) to the default notification center. When it completes successfully, it posts an [`didHideNotification`](nsapplication/didhidenotification.md).

## Parameters

- `sender`: The object that sent the command.

## See Also

- [func miniaturizeAll(Any?)](nsapplication/miniaturizeall(_:).md)
  Miniaturizes all the receiver’s windows.
- [func applicationDidHide(Notification)](nsapplicationdelegate/applicationdidhide(_:).md)
  Tells the delegate that the app is now hidden.
- [func applicationWillHide(Notification)](nsapplicationdelegate/applicationwillhide(_:).md)
  Tells the delegate that the app is about to be hidden.
- [var isHidden: Bool](nsapplication/ishidden.md)
  A Boolean value indicating whether the app is hidden.
- [func unhide(Any?)](nsapplication/unhide(_:).md)
  Restores hidden windows to the screen and makes the receiver active.
- [func unhideWithoutActivation()](nsapplication/unhidewithoutactivation.md)
  Restores hidden windows without activating their owner (the receiver).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/hide(_:))*