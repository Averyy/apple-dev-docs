# authorizationRights()

**Framework**: Security Interface  
**Kind**: method

Returns the authorization rights for this view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!
```

## See Also

- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](sfauthorizationview/setauthorizationrights(_:).md)
  Sets the authorization rights for this view.
- [func authorization() -> SFAuthorization!](sfauthorizationview/authorization.md)
  Returns the authorization object associated with this view.
- [func authorizationState() -> SFAuthorizationViewState](sfauthorizationview/authorizationstate.md)
  Returns the current state of the authorization view.
- [func isEnabled() -> Bool](sfauthorizationview/isenabled.md)
  Indicates whether the authorization view is enabled ([`true`](https://developer.apple.com/documentation/Swift/true)) or disabled ([`false`](https://developer.apple.com/documentation/Swift/false)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/authorizationrights())*