# applicationWillHide(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app is about to be hidden.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillHide(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func hide(Any?)](nsapplication/hide(_:).md)
  Hides all the receiver’s windows, and the next app in line is activated.
- [func applicationDidHide(Notification)](nsapplicationdelegate/applicationdidhide(_:).md)
  Tells the delegate that the app is now hidden.
- [func applicationWillUnhide(Notification)](nsapplicationdelegate/applicationwillunhide(_:).md)
  Tells the delegate that the app is about to become visible.
- [func applicationDidUnhide(Notification)](nsapplicationdelegate/applicationdidunhide(_:).md)
  Tells the delegate that the app is now visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillhide(_:))*