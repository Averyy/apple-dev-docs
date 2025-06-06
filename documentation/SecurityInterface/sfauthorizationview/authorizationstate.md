# authorizationState()

**Framework**: Security Interface  
**Kind**: method

Returns the current state of the authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func authorizationState() -> SFAuthorizationViewState
```

## Topics

### Related Documentation
- [func deauthorize(Any!) -> Bool](sfauthorizationview/deauthorize(_:).md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.
- [func authorize(Any!) -> Bool](sfauthorizationview/authorize(_:).md)
  Attempts to unlock the lock icon in the view.

## See Also

- [func authorization() -> SFAuthorization!](sfauthorizationview/authorization.md)
  Returns the authorization object associated with this view.
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](sfauthorizationview/authorizationrights.md)
  Returns the authorization rights for this view.
- [func isEnabled() -> Bool](sfauthorizationview/isenabled.md)
  Indicates whether the authorization view is enabled ([`true`](https://developer.apple.com/documentation/swift/true)) or disabled ([`false`](https://developer.apple.com/documentation/swift/false)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/authorizationstate())*