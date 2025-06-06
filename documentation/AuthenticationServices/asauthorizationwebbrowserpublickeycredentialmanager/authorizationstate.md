# ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState

**Framework**: Authentication Services  
**Kind**: enum

An enumeration of values that indicate whether the browser app has access to a person’s passkeys.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
enum AuthorizationState
```

## Topics

### Passkey access states
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.authorized](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/authorized.md)
  Someone allows the browser app to use passkeys stored in the keychain, and managed by third-party credential manager apps.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.denied](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/denied.md)
  Someone forbids the browser app to use passkeys stored in the keychain, and managed by third-party credential manager apps.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.notDetermined](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/notdetermined.md)
  The person has yet to choose whether to allow the browser app to access passkeys stored on the keychain, or managed by third-party credential managers.
### Initializers
- [init?(rawValue: Int)](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var authorizationStateForPlatformCredentials: ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstateforplatformcredentials.md)
  Returns a value that indicates whether the browser app has access to a person’s passkeys.
- [func requestAuthorizationForPublicKeyCredentials((ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState) -> Void)](asauthorizationwebbrowserpublickeycredentialmanager/requestauthorizationforpublickeycredentials(_:).md)
  Requests a person’s permission to use their passkeys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate)*