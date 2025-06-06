# applicationWillBecomeActive(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app is about to become active.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillBecomeActive(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func applicationWillFinishLaunching(Notification)](nsapplicationdelegate/applicationwillfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is about to complete.
- [func applicationDidBecomeActive(Notification)](nsapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app is now active.
- [func applicationWillResignActive(Notification)](nsapplicationdelegate/applicationwillresignactive(_:).md)
  Tells the delegate that the app is about to become inactive and will lose focus.
- [func applicationDidResignActive(Notification)](nsapplicationdelegate/applicationdidresignactive(_:).md)
  Tells the delegate that the app is no longer active and doesn’t have focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillbecomeactive(_:))*