# applicationDidResignActive(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app is no longer active and doesn’t have focus.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationDidResignActive(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func applicationWillBecomeActive(Notification)](nsapplicationdelegate/applicationwillbecomeactive(_:).md)
  Tells the delegate that the app is about to become active.
- [func applicationDidBecomeActive(Notification)](nsapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app is now active.
- [func applicationWillResignActive(Notification)](nsapplicationdelegate/applicationwillresignactive(_:).md)
  Tells the delegate that the app is about to become inactive and will lose focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidresignactive(_:))*