# didFinishRestoringWindowsNotification

**Framework**: AppKit  
**Kind**: property

Posted when the app has finished restoring windows.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didFinishRestoringWindowsNotification: NSNotification.Name
```

#### Discussion

The notification is posted on the main actor when the app is finished restoring windows, that is, when all the completion handlers from [`restoreWindow(withIdentifier:state:completionHandler:)`](nswindowrestoration/restorewindow(withidentifier:state:completionhandler:).md) have been called. This is always posted after [`willFinishLaunchingNotification`](nsapplication/willfinishlaunchingnotification.md), but may be posted before or after [`didFinishLaunchingNotification`](nsapplication/didfinishlaunchingnotification.md), depending on whether clients copy the completion handlers and invoke them later. If there were no windows to restore, then this notification is still posted at the corresponding point in app launch (between [`willFinishLaunchingNotification`](nsapplication/willfinishlaunchingnotification.md) and [`didFinishLaunchingNotification`](nsapplication/didfinishlaunchingnotification.md)).

The notification object is [`shared`](nsapplication/shared.md). This notification doesn’t contain a `userInfo` dictionary.

## See Also

- [class let didBecomeActiveNotification: NSNotification.Name](nsapplication/didbecomeactivenotification.md)
  Posted immediately after the app becomes active.
- [class let didChangeScreenParametersNotification: NSNotification.Name](nsapplication/didchangescreenparametersnotification.md)
  Posted when the configuration of the displays attached to the computer is changed.
- [class let didFinishLaunchingNotification: NSNotification.Name](nsapplication/didfinishlaunchingnotification.md)
  Posted at the end of the [`finishLaunching()`](nsapplication/finishlaunching().md) method to indicate that the app has completed launching and is ready to run.
- [class let didHideNotification: NSNotification.Name](nsapplication/didhidenotification.md)
  Posted at the end of the [`hide(_:)`](nsapplication/hide(_:).md) method to indicate that the app is now hidden.
- [class let didResignActiveNotification: NSNotification.Name](nsapplication/didresignactivenotification.md)
  Posted immediately after the app gives up its active status to another app.
- [class let didUnhideNotification: NSNotification.Name](nsapplication/didunhidenotification.md)
  Posted at the end of the [`unhideWithoutActivation()`](nsapplication/unhidewithoutactivation().md) method to indicate that the app is now visible.
- [class let didUpdateNotification: NSNotification.Name](nsapplication/didupdatenotification.md)
  Posted at the end of the [`updateWindows()`](nsapplication/updatewindows().md) method to indicate that the app has finished updating its windows.
- [class let willBecomeActiveNotification: NSNotification.Name](nsapplication/willbecomeactivenotification.md)
  Posted immediately before the app becomes active.
- [class let willFinishLaunchingNotification: NSNotification.Name](nsapplication/willfinishlaunchingnotification.md)
  Posted at the start of the [`finishLaunching()`](nsapplication/finishlaunching().md) method to indicate that the app has completed its initialization process and is about to finish launching.
- [class let willHideNotification: NSNotification.Name](nsapplication/willhidenotification.md)
  Posted at the start of the [`hide(_:)`](nsapplication/hide(_:).md) method to indicate that the app is about to be hidden.
- [class let willResignActiveNotification: NSNotification.Name](nsapplication/willresignactivenotification.md)
  Posted immediately before the app gives up its active status to another app.
- [class let willTerminateNotification: NSNotification.Name](nsapplication/willterminatenotification.md)
  Sends a notification to terminate the app.
- [class let willUnhideNotification: NSNotification.Name](nsapplication/willunhidenotification.md)
  Posted at the start of the [`unhideWithoutActivation()`](nsapplication/unhidewithoutactivation().md) method to indicate that the app is about to become visible.
- [class let willUpdateNotification: NSNotification.Name](nsapplication/willupdatenotification.md)
  Posted at the start of the [`updateWindows()`](nsapplication/updatewindows().md) method to indicate that the app is about to update its windows.
- [class let didChangeOcclusionStateNotification: NSNotification.Name](nsapplication/didchangeocclusionstatenotification.md)
  Posted when the app’s occlusion state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/didfinishrestoringwindowsnotification)*