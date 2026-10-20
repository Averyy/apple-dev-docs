# isEnabled()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Indicates whether the authorization view is enabled ([`true`](../../Swift/true.md)) or disabled ([`false`](../../Swift/false.md)).

**Availability**:
- macOS 10.3+

## Declaration

```swift
func isEnabled() -> Bool
```

```objc
- (BOOL) isEnabled;
```

## See Also

### Related Documentation
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Sets the current state of the authorization view.
### Getting information about the authorization view
- [func authorization() -> SFAuthorization!](./authorization%28%29.md)
  Returns the authorization object associated with this view.
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](./authorizationrights%28%29.md)
  Returns the authorization rights for this view.
- [func authorizationState() -> SFAuthorizationViewState](./authorizationstate%28%29.md)
  Returns the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/isenabled())*