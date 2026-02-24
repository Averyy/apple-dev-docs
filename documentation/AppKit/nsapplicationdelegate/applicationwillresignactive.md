# applicationWillResignActive(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app is about to become inactive and will lose focus.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillResignActive(_ notification: Notification)
```

## Parameters

- `notification`: A notification named [`willResignActiveNotification`](nsapplication/willresignactivenotification.md). Calling the [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) method of this notification returns the `NSApplication` object itself.

## See Also

- [func applicationWillBecomeActive(Notification)](nsapplicationdelegate/applicationwillbecomeactive(_:).md)
  Tells the delegate that the app is about to become active.
- [func applicationDidBecomeActive(Notification)](nsapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app is now active.
- [func applicationDidResignActive(Notification)](nsapplicationdelegate/applicationdidresignactive(_:).md)
  Tells the delegate that the app is no longer active and doesn’t have focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillresignactive(_:))*