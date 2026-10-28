# authorization()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the authorization object associated with this view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorization() -> SFAuthorization!
```

```objc
- (SFAuthorization *) authorization;
```

## Discussion

The authorization object is defined in [Security Foundation](../../SecurityFoundation/SecurityFoundation.md).

## See Also

### Getting information about the authorization view
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](./authorizationrights%28%29.md)
  Returns the authorization rights for this view.
- [func authorizationState() -> SFAuthorizationViewState](./authorizationstate%28%29.md)
  Returns the current state of the authorization view.
- [func isEnabled() -> Bool](./isenabled%28%29.md)
  Indicates whether the authorization view is enabled ([`true`](../../Swift/true.md)) or disabled ([`false`](../../Swift/false.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/authorization())*