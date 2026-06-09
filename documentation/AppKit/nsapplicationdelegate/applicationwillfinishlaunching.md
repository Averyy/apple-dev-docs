# applicationWillFinishLaunching(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app’s initialization is about to complete.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillFinishLaunching(_ notification: Notification)
```

## Mentions

- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)

## Parameters

- `notification`: A notification named [`willFinishLaunchingNotification`](nsapplication/willfinishlaunchingnotification.md). Calling the [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) method of this notification returns the `NSApplication` object itself.

## See Also

- [func applicationWillBecomeActive(Notification)](nsapplicationdelegate/applicationwillbecomeactive(_:).md)
  Tells the delegate that the app is about to become active.
- [func finishLaunching()](nsapplication/finishlaunching.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [class NSApplication](nsapplication.md)
  An object that manages an app’s main event loop and resources used by all of that app’s objects.
- [func applicationDidFinishLaunching(Notification)](nsapplicationdelegate/applicationdidfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
- [NSApplicationDidFinishLaunching User Info Keys](nsapplicationdidfinishlaunching-user-info-keys.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillfinishlaunching(_:))*