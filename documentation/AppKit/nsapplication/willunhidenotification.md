# willUnhideNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted at the start of the [`unhideWithoutActivation()`](./unhidewithoutactivation%28%29.md) method to indicate that the app is about to become visible.

**Availability**:
- macOS

## Declaration

```swift
class let willUnhideNotification: NSNotification.Name
```

```c
extern NSNotificationName NSApplicationWillUnhideNotification;
```

#### Discussion

The notification object is [`shared`](./shared.md). This notification doesn’t contain a `userInfo` dictionary.  The system posts this notification on the main actor.

To observe this notification using Swift concurrency, use [`NSApplication.WillUnhideMessage`](./willunhidemessage.md).

## See Also

### Notifications
- [class let didBecomeActiveNotification: NSNotification.Name](./didbecomeactivenotification.md)
  Posted immediately after the app becomes active.
- [class let didChangeScreenParametersNotification: NSNotification.Name](./didchangescreenparametersnotification.md)
  Posted when the configuration of the displays attached to the computer is changed.
- [class let didFinishLaunchingNotification: NSNotification.Name](./didfinishlaunchingnotification.md)
  Posted at the end of the [`finishLaunching()`](./finishlaunching%28%29.md) method to indicate that the app has completed launching and is ready to run.
- [class let didHideNotification: NSNotification.Name](./didhidenotification.md)
  Posted at the end of the [`hide(_:)`](./hide%28_%29.md) method to indicate that the app is now hidden.
- [class let didResignActiveNotification: NSNotification.Name](./didresignactivenotification.md)
  Posted immediately after the app gives up its active status to another app.
- [class let didUnhideNotification: NSNotification.Name](./didunhidenotification.md)
  Posted at the end of the [`unhideWithoutActivation()`](./unhidewithoutactivation%28%29.md) method to indicate that the app is now visible.
- [class let didUpdateNotification: NSNotification.Name](./didupdatenotification.md)
  Posted at the end of the [`updateWindows()`](./updatewindows%28%29.md) method to indicate that the app has finished updating its windows.
- [class let willBecomeActiveNotification: NSNotification.Name](./willbecomeactivenotification.md)
  Posted immediately before the app becomes active.
- [class let willFinishLaunchingNotification: NSNotification.Name](./willfinishlaunchingnotification.md)
  Posted at the start of the [`finishLaunching()`](./finishlaunching%28%29.md) method to indicate that the app has completed its initialization process and is about to finish launching.
- [class let willHideNotification: NSNotification.Name](./willhidenotification.md)
  Posted at the start of the [`hide(_:)`](./hide%28_%29.md) method to indicate that the app is about to be hidden.
- [class let willResignActiveNotification: NSNotification.Name](./willresignactivenotification.md)
  Posted immediately before the app gives up its active status to another app.
- [class let willTerminateNotification: NSNotification.Name](./willterminatenotification.md)
  Sends a notification to terminate the app.
- [class let willUpdateNotification: NSNotification.Name](./willupdatenotification.md)
  Posted at the start of the [`updateWindows()`](./updatewindows%28%29.md) method to indicate that the app is about to update its windows.
- [class let didFinishRestoringWindowsNotification: NSNotification.Name](./didfinishrestoringwindowsnotification.md)
  Posted when the app has finished restoring windows.
- [class let didChangeOcclusionStateNotification: NSNotification.Name](./didchangeocclusionstatenotification.md)
  Posted when the app’s occlusion state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/willunhidenotification)*