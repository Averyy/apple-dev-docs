# applicationWillUnhide(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app is about to become visible.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillUnhide(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func unhide(Any?)](nsapplication/unhide(_:).md)
  Restores hidden windows to the screen and makes the receiver active.
- [func applicationWillHide(Notification)](nsapplicationdelegate/applicationwillhide(_:).md)
  Tells the delegate that the app is about to be hidden.
- [func applicationDidHide(Notification)](nsapplicationdelegate/applicationdidhide(_:).md)
  Tells the delegate that the app is now hidden.
- [func applicationDidUnhide(Notification)](nsapplicationdelegate/applicationdidunhide(_:).md)
  Tells the delegate that the app is now visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillunhide(_:))*