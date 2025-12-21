# isEnabled()

**Framework**: Security Interface  
**Kind**: method

Indicates whether the authorization view is enabled ([`true`](https://developer.apple.com/documentation/Swift/true)) or disabled ([`false`](https://developer.apple.com/documentation/Swift/false)).

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func isEnabled() -> Bool
```

## See Also

- [func setEnabled(Bool)](sfauthorizationview/setenabled(_:).md)
  Sets the current state of the authorization view.
- [func authorization() -> SFAuthorization!](sfauthorizationview/authorization.md)
  Returns the authorization object associated with this view.
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](sfauthorizationview/authorizationrights.md)
  Returns the authorization rights for this view.
- [func authorizationState() -> SFAuthorizationViewState](sfauthorizationview/authorizationstate.md)
  Returns the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/isenabled())*