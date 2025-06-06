# setAuthorizationRights(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the authorization rights for this view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setAuthorizationRights(_ authorizationRights: UnsafePointer<AuthorizationRights>!)
```

#### Discussion

Either this method or the [`setString(_:)`](sfauthorizationview/setstring(_:).md) method must be called before the view displays correctly.

The authorization rights structures are defined in [`AuthorizationRights`](https://developer.apple.com/documentation/Security/AuthorizationRights) in [`Authorization Services`](https://developer.apple.com/documentation/Security/authorization-services).

## Parameters

- `authorizationRights`: An authorization rights structure specifying the authorization rights represented by the authorization view.

## See Also

- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](sfauthorizationview/authorizationrights.md)
  Returns the authorization rights for this view.
- [func setString(AuthorizationString!)](sfauthorizationview/setstring(_:).md)
  Sets the requested-right string to use with the default authorization rights set.
- [func setAutoupdate(Bool)](sfauthorizationview/setautoupdate(_:).md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](sfauthorizationview/setautoupdate(_:interval:).md)
  Sets the authorization view to update itself at a specific interval.
- [func setFlags(AuthorizationFlags)](sfauthorizationview/setflags(_:).md)
  Sets the current authorization flags for the view.
- [func setEnabled(Bool)](sfauthorizationview/setenabled(_:).md)
  Sets the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setauthorizationrights(_:))*