# authorizationState()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the current state of the authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorizationState() -> SFAuthorizationViewState
```

```objc
- (SFAuthorizationViewState) authorizationState;
```

## See Also

### Related Documentation
- [func deauthorize(Any!) -> Bool](./deauthorize%28_%29.md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.
- [func authorize(Any!) -> Bool](./authorize%28_%29.md)
  Attempts to unlock the lock icon in the view.
### Getting information about the authorization view
- [func authorization() -> SFAuthorization!](./authorization%28%29.md)
  Returns the authorization object associated with this view.
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](./authorizationrights%28%29.md)
  Returns the authorization rights for this view.
- [func isEnabled() -> Bool](./isenabled%28%29.md)
  Indicates whether the authorization view is enabled ([`true`](../../Swift/true.md)) or disabled ([`false`](../../Swift/false.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/authorizationstate())*