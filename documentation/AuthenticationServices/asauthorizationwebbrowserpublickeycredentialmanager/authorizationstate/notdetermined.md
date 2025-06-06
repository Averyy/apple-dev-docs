# ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.notDetermined

**Framework**: Authentication Services  
**Kind**: case

The person has yet to choose whether to allow the browser app to access passkeys stored on the keychain, or managed by third-party credential managers.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
case notDetermined
```

## Mentions

- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)

## See Also

- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.authorized](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/authorized.md)
  Someone allows the browser app to use passkeys stored in the keychain, and managed by third-party credential manager apps.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.denied](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/denied.md)
  Someone forbids the browser app to use passkeys stored in the keychain, and managed by third-party credential manager apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/notdetermined)*