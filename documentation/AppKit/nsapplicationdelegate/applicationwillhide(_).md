# applicationWillHide(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is about to be hidden.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillHide(_ notification: Notification)
```

```objc
- (void) applicationWillHide:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`willHideNotification`](../nsapplication/willhidenotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Related Documentation
- [func hide(Any?)](../nsapplication/hide%28_%29.md)
  Hides all the receiver’s windows, and the next app in line is activated.
### Hiding Applications
- [func applicationDidHide(Notification)](./applicationdidhide%28_%29.md)
  Tells the delegate that the app is now hidden.
- [func applicationWillUnhide(Notification)](./applicationwillunhide%28_%29.md)
  Tells the delegate that the app is about to become visible.
- [func applicationDidUnhide(Notification)](./applicationdidunhide%28_%29.md)
  Tells the delegate that the app is now visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillhide(_:))*