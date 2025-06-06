# authorization()

**Framework**: Security Interface  
**Kind**: method

Returns the authorization object associated with this view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func authorization() -> SFAuthorization!
```

#### Discussion

The authorization object is defined in [`Security Foundation`](https://developer.apple.com/documentation/SecurityFoundation).

## See Also

- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](sfauthorizationview/authorizationrights.md)
  Returns the authorization rights for this view.
- [func authorizationState() -> SFAuthorizationViewState](sfauthorizationview/authorizationstate.md)
  Returns the current state of the authorization view.
- [func isEnabled() -> Bool](sfauthorizationview/isenabled.md)
  Indicates whether the authorization view is enabled ([`true`](https://developer.apple.com/documentation/swift/true)) or disabled ([`false`](https://developer.apple.com/documentation/swift/false)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/authorization())*