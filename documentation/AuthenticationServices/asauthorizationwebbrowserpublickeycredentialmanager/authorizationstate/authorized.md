# ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.authorized

**Framework**: Authentication Services  
**Kind**: case

Someone allows the browser app to use passkeys stored in the keychain, and managed by third-party credential manager apps.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
case authorized
```

## Mentions

- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)

#### Discussion

The person can change their decision by navigating to Passkeys Access for Web Browsers, in the Privacy & Security pane in Settings.

## See Also

- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.denied](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/denied.md)
  Someone forbids the browser app to use passkeys stored in the keychain, and managed by third-party credential manager apps.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.notDetermined](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/notdetermined.md)
  The person has yet to choose whether to allow the browser app to access passkeys stored on the keychain, or managed by third-party credential managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/authorized)*