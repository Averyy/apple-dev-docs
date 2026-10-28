# setAutoupdate(_:interval:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the authorization view to update itself at a specific interval.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setAutoupdate(_ autoupdate: Bool, interval: TimeInterval)
```

```objc
- (void) setAutoupdate:(BOOL) autoupdate interval:(NSTimeInterval) interval;
```

## Discussion

If autoupdates are enabled and the authorization times out (for example), the authorization view automatically relocks. If autoupdates are disabled, you have to call the [`updateStatus(_:)`](./updatestatus%28_%29.md) method to manually update the view if the status changes when the user has not clicked on the lock icon. Autoupdates are disabled by default. Because autoupdates poll, they can affect system performance. For that reason, you might want to set a time interval so that the polling does not take place as often.

## Parameters

- `autoupdate`: Specifies whether the authorization view should update itself automatically. Set to [`true`](../../Swift/true.md) to enable autoupdates.
- `interval`: If `autoupdate` is [`true`](../../Swift/true.md), sets the interval at which updates take place, in seconds.

## See Also

### Setting up the authorization view
- [func setString(AuthorizationString!)](./setstring%28_%29.md)
  Sets the requested-right string to use with the default authorization rights set.
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](./setauthorizationrights%28_%29.md)
  Sets the authorization rights for this view.
- [func setAutoupdate(Bool)](./setautoupdate%28_%29.md)
  Sets the authorization view to update itself automatically.
- [func setFlags(AuthorizationFlags)](./setflags%28_%29.md)
  Sets the current authorization flags for the view.
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Sets the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setautoupdate(_:interval:))*