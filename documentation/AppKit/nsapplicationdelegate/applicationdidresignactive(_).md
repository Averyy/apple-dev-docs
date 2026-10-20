# applicationDidResignActive(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is no longer active and doesn’t have focus.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationDidResignActive(_ notification: Notification)
```

```objc
- (void) applicationDidResignActive:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`didResignActiveNotification`](../nsapplication/didresignactivenotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Managing Active Status
- [func applicationWillBecomeActive(Notification)](./applicationwillbecomeactive%28_%29.md)
  Tells the delegate that the app is about to become active.
- [func applicationDidBecomeActive(Notification)](./applicationdidbecomeactive%28_%29.md)
  Tells the delegate that the app is now active.
- [func applicationWillResignActive(Notification)](./applicationwillresignactive%28_%29.md)
  Tells the delegate that the app is about to become inactive and will lose focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidresignactive(_:))*