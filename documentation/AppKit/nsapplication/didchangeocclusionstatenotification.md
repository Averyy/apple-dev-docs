# didChangeOcclusionStateNotification

**Framework**: AppKit  
**Kind**: property

Posted when the app’s occlusion state changes.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class let didChangeOcclusionStateNotification: NSNotification.Name
```

#### Discussion

The system posts this notification on the main actor.  Upon receiving this notification, you can query the app for its occlusion state. Note that this only notifies about changes in the state of the occlusion, not when the occlusion region changes. You can use this notification to increase responsiveness and save power by halting any expensive calculations that the user can’t see.

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
- [class let didFinishRestoringWindowsNotification: NSNotification.Name](nsapplication/didfinishrestoringwindowsnotification.md)
  Posted when the app has finished restoring windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/didchangeocclusionstatenotification)*