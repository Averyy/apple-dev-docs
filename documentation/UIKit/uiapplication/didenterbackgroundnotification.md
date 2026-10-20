# didEnterBackgroundNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when the app enters the background.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let didEnterBackgroundNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIApplicationDidEnterBackgroundNotification;
```

#### Discussion

The `object` of the notification is the [`UIApplication`](../uiapplication.md) object. There is no `userInfo` dictionary.

## See Also

### Responding to app life-cycle events
- [func applicationDidEnterBackground(UIApplication)](../uiapplicationdelegate/applicationdidenterbackground%28_%29.md)
  Tells the delegate that the app is now in the background.
- [func applicationWillTerminate(UIApplication)](../uiapplicationdelegate/applicationwillterminate%28_%29.md)
  Tells the delegate when the app is about to terminate.
- [class let didBecomeActiveNotification: NSNotification.Name](./didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let willEnterForegroundNotification: NSNotification.Name](./willenterforegroundnotification.md)
  A notification that posts shortly before your app’s UI transitions to the foreground.
- [class let willResignActiveNotification: NSNotification.Name](./willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](./willterminatenotification.md)
  A notification that posts when the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/didenterbackgroundnotification)*