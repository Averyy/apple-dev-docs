# updateStatus(_:)

**Framework**: Security Interface  
**Kind**: method

Manually updates the authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func updateStatus(_ inSender: Any!) -> Bool
```

#### Discussion

Calls to [`updateStatus(_:)`](sfauthorizationview/updatestatus(_:).md) return [`true`](https://developer.apple.com/documentation/swift/true) if in the unlocked state, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

If autoupdates have not been set, you must call [`updateStatus(_:)`](sfauthorizationview/updatestatus(_:).md) for the authorization view’s initial state to display correctly. The Security Framework calls this method for you when you change the state of the lock (by calling [`deauthorize(_:)`](sfauthorizationview/deauthorize(_:).md), for example).

## Parameters

- `inSender`: The authorization view to update.

## See Also

- [func setAutoupdate(Bool)](sfauthorizationview/setautoupdate(_:).md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](sfauthorizationview/setautoupdate(_:interval:).md)
  Sets the authorization view to update itself at a specific interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/updatestatus(_:))*