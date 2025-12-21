# ASAuthorizationWebBrowserPublicKeyCredentialManager

**Framework**: Authentication Services  
**Kind**: class

A class that you use to request access to a person’s passkeys in a web browser, and that reports on the access status.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
class ASAuthorizationWebBrowserPublicKeyCredentialManager
```

## Mentions

- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)

## Topics

### Creating credential managers
- [init()](asauthorizationwebbrowserpublickeycredentialmanager/init.md)
  Initializes a credential manager.
### Requesting access to passkeys
- [var authorizationStateForPlatformCredentials: ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstateforplatformcredentials.md)
  Returns a value that indicates whether the browser app has access to a person’s passkeys.
- [func requestAuthorizationForPublicKeyCredentials((ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState) -> Void)](asauthorizationwebbrowserpublickeycredentialmanager/requestauthorizationforpublickeycredentials(_:).md)
  Requests a person’s permission to use their passkeys.
- [ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate.md)
  An enumeration of values that indicate whether the browser app has access to a person’s passkeys.
### Using passkeys
- [func platformCredentials(forRelyingParty: String) async -> [ASAuthorizationWebBrowserPlatformPublicKeyCredential]](asauthorizationwebbrowserpublickeycredentialmanager/platformcredentials(forrelyingparty:).md)
  Gets a list of passkeys available for authenticating with the given relying party.
- [struct ASAuthorizationWebBrowserPlatformPublicKeyCredential](asauthorizationwebbrowserplatformpublickeycredential-swift.struct.md)
  A structure that describes a passkey stored in the keychain, or managed by a third-party credential manager.
### Type Properties
- [class var isDeviceConfiguredForPasskeys: Bool](asauthorizationwebbrowserpublickeycredentialmanager/isdeviceconfiguredforpasskeys.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)
  Provide a secure and convenient alternative to passwords.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager)*