# ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum ASAuthorizationWebBrowserPublicKeyCredentialManagerAuthorizationState : NSInteger;
```

## Topics

### Passkey access states
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.authorized](./authorizationstate/authorized.md)
  Someone allows the browser app to use passkeys stored in the keychain, and managed by third-party credential manager apps.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.denied](./authorizationstate/denied.md)
  Someone forbids the browser app to use passkeys stored in the keychain, and managed by third-party credential manager apps.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.notDetermined](./authorizationstate/notdetermined.md)
  The person has yet to choose whether to allow the browser app to access passkeys stored on the keychain, or managed by third-party credential managers.
### Initializers
- [init?(rawValue: Int)](./authorizationstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting access to passkeys
- [var authorizationStateForPlatformCredentials: ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState](./authorizationstateforplatformcredentials.md)
  Returns a value that indicates whether the browser app has access to a person’s passkeys.
- [func requestAuthorizationForPublicKeyCredentials((ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState) -> Void)](./requestauthorizationforpublickeycredentials%28_%29.md)
  Requests a person’s permission to use their passkeys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate)*