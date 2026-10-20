# setAuthorizationRights(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the authorization rights for this view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setAuthorizationRights(_ authorizationRights: UnsafePointer<AuthorizationRights>!)
```

```objc
- (void) setAuthorizationRights:(const AuthorizationRights *) authorizationRights;
```

#### Discussion

Either this method or the [`setString(_:)`](./setstring%28_%29.md) method must be called before the view displays correctly.

The authorization rights structures are defined in [`AuthorizationRights`](../../Security/authorizationrights.md) in [Authorization Services](../../Security/authorization-services.md).

## Parameters

- `authorizationRights`: An authorization rights structure specifying the authorization rights represented by the authorization view.

## See Also

### Related Documentation
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](./authorizationrights%28%29.md)
  Returns the authorization rights for this view.
### Setting up the authorization view
- [func setString(AuthorizationString!)](./setstring%28_%29.md)
  Sets the requested-right string to use with the default authorization rights set.
- [func setAutoupdate(Bool)](./setautoupdate%28_%29.md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](./setautoupdate%28_,interval%29.md)
  Sets the authorization view to update itself at a specific interval.
- [func setFlags(AuthorizationFlags)](./setflags%28_%29.md)
  Sets the current authorization flags for the view.
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Sets the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setauthorizationrights(_:))*