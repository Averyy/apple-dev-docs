# applicationWillUnhide(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is about to become visible.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillUnhide(_ notification: Notification)
```

```objc
- (void) applicationWillUnhide:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`willUnhideNotification`](../nsapplication/willunhidenotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Related Documentation
- [func unhide(Any?)](../nsapplication/unhide%28_%29.md)
  Restores hidden windows to the screen and makes the receiver active.
### Hiding Applications
- [func applicationWillHide(Notification)](./applicationwillhide%28_%29.md)
  Tells the delegate that the app is about to be hidden.
- [func applicationDidHide(Notification)](./applicationdidhide%28_%29.md)
  Tells the delegate that the app is now hidden.
- [func applicationDidUnhide(Notification)](./applicationdidunhide%28_%29.md)
  Tells the delegate that the app is now visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillunhide(_:))*