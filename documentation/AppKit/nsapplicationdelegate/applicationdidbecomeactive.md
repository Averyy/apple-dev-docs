# applicationDidBecomeActive(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app is now active.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationDidBecomeActive(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func applicationDidFinishLaunching(Notification)](nsapplicationdelegate/applicationdidfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
- [func applicationWillBecomeActive(Notification)](nsapplicationdelegate/applicationwillbecomeactive(_:).md)
  Tells the delegate that the app is about to become active.
- [func applicationWillResignActive(Notification)](nsapplicationdelegate/applicationwillresignactive(_:).md)
  Tells the delegate that the app is about to become inactive and will lose focus.
- [func applicationDidResignActive(Notification)](nsapplicationdelegate/applicationdidresignactive(_:).md)
  Tells the delegate that the app is no longer active and doesn’t have focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidbecomeactive(_:))*