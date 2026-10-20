# ASAuthorizationSecurityKeyPublicKeyCredentialProvider

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A mechanism for providing public key credential requests to an app or service with a physical security key.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class ASAuthorizationSecurityKeyPublicKeyCredentialProvider
```

```objc
@interface ASAuthorizationSecurityKeyPublicKeyCredentialProvider : NSObject
```

## Mentions

- [Supporting Security Key Authentication Using Physical Keys](./supporting-security-key-authentication-using-physical-keys.md)

#### Overview

The credential provider accesses public-private key pairs stored on a physical security key for registration or authentication with a relying party. Instantiate this object, passing in the relying party identifier for the credentials.

## Topics

### Creating the provider
- [init(relyingPartyIdentifier: String)](./asauthorizationsecuritykeypublickeycredentialprovider/init%28relyingpartyidentifier%29.md)
  Creates the object with a relying party identifier.
### Creating the request
- [var relyingPartyIdentifier: String](./asauthorizationsecuritykeypublickeycredentialprovider/relyingpartyidentifier.md)
  The domain name of the service to authorize against.
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](./asauthorizationsecuritykeypublickeycredentialprovider/createcredentialassertionrequest%28challenge%29.md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./asauthorizationsecuritykeypublickeycredentialprovider/createcredentialregistrationrequest%28challenge,displayname,name,userid%29.md)
  Creates a registration request with a challenge, display name, and user ID.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](./asauthorizationprovider.md)
- [ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider](./asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Credential providers
- [class ASAuthorizationPlatformPublicKeyCredentialProvider](./asauthorizationplatformpublickeycredentialprovider.md)
  A mechanism for providing public key credential requests to an app or service with iCloud Keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialprovider)*