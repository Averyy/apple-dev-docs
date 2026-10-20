# applicationDidBecomeActive(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is now active.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationDidBecomeActive(_ notification: Notification)
```

```objc
- (void) applicationDidBecomeActive:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`didBecomeActiveNotification`](../nsapplication/didbecomeactivenotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Related Documentation
- [func applicationDidFinishLaunching(Notification)](./applicationdidfinishlaunching%28_%29.md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
### Managing Active Status
- [func applicationWillBecomeActive(Notification)](./applicationwillbecomeactive%28_%29.md)
  Tells the delegate that the app is about to become active.
- [func applicationWillResignActive(Notification)](./applicationwillresignactive%28_%29.md)
  Tells the delegate that the app is about to become inactive and will lose focus.
- [func applicationDidResignActive(Notification)](./applicationdidresignactive%28_%29.md)
  Tells the delegate that the app is no longer active and doesn’t have focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidbecomeactive(_:))*