# authorizationStateForPlatformCredentials

**Framework**: Authentication Services  
**Kind**: property

Returns a value that indicates whether the browser app has access to a person’s passkeys.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
var authorizationStateForPlatformCredentials: ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState { get }
```

## Mentions

- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)

## See Also

- [func requestAuthorizationForPublicKeyCredentials((ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState) -> Void)](asauthorizationwebbrowserpublickeycredentialmanager/requestauthorizationforpublickeycredentials(_:).md)
  Requests a person’s permission to use their passkeys.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate.md)
  An enumeration of values that indicate whether the browser app has access to a person’s passkeys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager/authorizationstateforplatformcredentials)*