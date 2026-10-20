# applicationWillBecomeActive(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is about to become active.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillBecomeActive(_ notification: Notification)
```

```objc
- (void) applicationWillBecomeActive:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`willBecomeActiveNotification`](../nsapplication/willbecomeactivenotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Related Documentation
- [func applicationWillFinishLaunching(Notification)](./applicationwillfinishlaunching%28_%29.md)
  Tells the delegate that the app’s initialization is about to complete.
### Managing Active Status
- [func applicationDidBecomeActive(Notification)](./applicationdidbecomeactive%28_%29.md)
  Tells the delegate that the app is now active.
- [func applicationWillResignActive(Notification)](./applicationwillresignactive%28_%29.md)
  Tells the delegate that the app is about to become inactive and will lose focus.
- [func applicationDidResignActive(Notification)](./applicationdidresignactive%28_%29.md)
  Tells the delegate that the app is no longer active and doesn’t have focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillbecomeactive(_:))*