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

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func applicationWillBecomeActive(Notification)](nsapplicationdelegate/applicationwillbecomeactive(_:).md)
  Tells the delegate that the app is about to become active.
- [Sheet Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Sheets.html#//apple_ref/doc/uid/10000002i)
- [func finishLaunching()](nsapplication/finishlaunching.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [Services Implementation Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/introduction.html#//apple_ref/doc/uid/10000101i)
- [Mac App Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/MOSXAppProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010543)
- [Local and Remote Notification Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)
- [Notification Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)
- [func applicationDidFinishLaunching(Notification)](nsapplicationdelegate/applicationdidfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
- [NSApplicationDidFinishLaunching User Info Keys](nsapplicationdidfinishlaunching-user-info-keys.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillfinishlaunching(_:))*