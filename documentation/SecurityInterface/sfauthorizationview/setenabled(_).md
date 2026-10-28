# setEnabled(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the current state of the authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setEnabled(_ enabled: Bool)
```

```objc
- (void) setEnabled:(BOOL) enabled;
```

## Discussion

A disabled view is visible but dimmed.

## Parameters

- `enabled`: Specifies whether the authorization view should be enabled ([`true`](../../Swift/true.md)) or disabled ([`false`](../../Swift/false.md)).

## See Also

### Related Documentation
- [func authorizationState() -> SFAuthorizationViewState](./authorizationstate%28%29.md)
  Returns the current state of the authorization view.
### Setting up the authorization view
- [func setString(AuthorizationString!)](./setstring%28_%29.md)
  Sets the requested-right string to use with the default authorization rights set.
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](./setauthorizationrights%28_%29.md)
  Sets the authorization rights for this view.
- [func setAutoupdate(Bool)](./setautoupdate%28_%29.md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](./setautoupdate%28_,interval%29.md)
  Sets the authorization view to update itself at a specific interval.
- [func setFlags(AuthorizationFlags)](./setflags%28_%29.md)
  Sets the current authorization flags for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setenabled(_:))*