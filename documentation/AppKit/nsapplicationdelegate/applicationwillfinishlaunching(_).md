# applicationWillFinishLaunching(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app’s initialization is about to complete.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillFinishLaunching(_ notification: Notification)
```

```objc
- (void) applicationWillFinishLaunching:(NSNotification *) notification;
```

## Mentions

- [Supporting Continuity Camera in Your Mac App](../supporting-continuity-camera-in-your-mac-app.md)

## Parameters

- `notification`: A notification named [`willFinishLaunchingNotification`](../nsapplication/willfinishlaunchingnotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Related Documentation
- [func applicationWillBecomeActive(Notification)](./applicationwillbecomeactive%28_%29.md)
  Tells the delegate that the app is about to become active.
- [func finishLaunching()](../nsapplication/finishlaunching%28%29.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [class NSApplication](../nsapplication.md)
  An object that manages an app’s main event loop and resources used by all of that app’s objects.
### Launching Applications
- [func applicationDidFinishLaunching(Notification)](./applicationdidfinishlaunching%28_%29.md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
- [NSApplicationDidFinishLaunching User Info Keys](../nsapplicationdidfinishlaunching-user-info-keys.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillfinishlaunching(_:))*