# willResignActiveNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when the app is no longer active and loses focus.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
nonisolated
class let willResignActiveNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIApplicationWillResignActiveNotification;
```

## Discussion

An app is active when it is receiving events. An active app can be said to have focus. It gains focus after being launched, loses focus when an overlay window pops up or when the device is locked, and gains focus when the device is unlocked.

## See Also

### Responding to app life-cycle events
- [func applicationDidEnterBackground(UIApplication)](../uiapplicationdelegate/applicationdidenterbackground%28_%29.md)
  Tells the delegate that the app is now in the background.
- [func applicationWillTerminate(UIApplication)](../uiapplicationdelegate/applicationwillterminate%28_%29.md)
  Tells the delegate when the app is about to terminate.
- [class let didBecomeActiveNotification: NSNotification.Name](./didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](./didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let willEnterForegroundNotification: NSNotification.Name](./willenterforegroundnotification.md)
  A notification that posts shortly before your app’s UI transitions to the foreground.
- [class let willTerminateNotification: NSNotification.Name](./willterminatenotification.md)
  A notification that posts when the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/willresignactivenotification)*