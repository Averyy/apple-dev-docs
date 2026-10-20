# updateStatus(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Manually updates the authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func updateStatus(_ inSender: Any!) -> Bool
```

```objc
- (BOOL) updateStatus:(id) inSender;
```

#### Discussion

Calls to [`updateStatus(_:)`](./updatestatus%28_%29.md) return [`true`](../../Swift/true.md) if in the unlocked state, [`false`](../../Swift/false.md) otherwise.

If autoupdates have not been set, you must call [`updateStatus(_:)`](./updatestatus%28_%29.md) for the authorization view’s initial state to display correctly. The Security Framework calls this method for you when you change the state of the lock (by calling [`deauthorize(_:)`](./deauthorize%28_%29.md), for example).

## Parameters

- `inSender`: The authorization view to update.

## See Also

### Related Documentation
- [func setAutoupdate(Bool)](./setautoupdate%28_%29.md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](./setautoupdate%28_,interval%29.md)
  Sets the authorization view to update itself at a specific interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/updatestatus(_:))*