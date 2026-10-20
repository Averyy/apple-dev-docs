# authorizationRights()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the authorization rights for this view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!
```

```objc
- (AuthorizationRights *) authorizationRights;
```

## See Also

### Related Documentation
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](./setauthorizationrights%28_%29.md)
  Sets the authorization rights for this view.
### Getting information about the authorization view
- [func authorization() -> SFAuthorization!](./authorization%28%29.md)
  Returns the authorization object associated with this view.
- [func authorizationState() -> SFAuthorizationViewState](./authorizationstate%28%29.md)
  Returns the current state of the authorization view.
- [func isEnabled() -> Bool](./isenabled%28%29.md)
  Indicates whether the authorization view is enabled ([`true`](../../Swift/true.md)) or disabled ([`false`](../../Swift/false.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/authorizationrights())*