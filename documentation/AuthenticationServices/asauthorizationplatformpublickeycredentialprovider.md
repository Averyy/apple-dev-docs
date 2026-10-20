# ASAuthorizationPlatformPublicKeyCredentialProvider

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A mechanism for providing public key credential requests to an app or service with iCloud Keychain.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationPlatformPublicKeyCredentialProvider
```

```objc
@interface ASAuthorizationPlatformPublicKeyCredentialProvider : NSObject
```

## Mentions

- [Supporting passkeys](./supporting-passkeys.md)

#### Overview

The credential provider accesses public-private key pairs stored in iCloud Keychain for registration or authentication with a relying party. Instantiate this object, passing in the relying party identifier for the credentials.

## Topics

### Creating the provider
- [init(relyingPartyIdentifier: String)](./asauthorizationplatformpublickeycredentialprovider/init%28relyingpartyidentifier%29.md)
  Creates the object with a relying party identifier.
### Creating the request
- [var relyingPartyIdentifier: String](./asauthorizationplatformpublickeycredentialprovider/relyingpartyidentifier.md)
  The domain name of the service to register or authorize against.
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](./asauthorizationplatformpublickeycredentialprovider/createcredentialassertionrequest%28challenge%29.md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest%28challenge,name,userid%29.md)
  Creates a registration request with a challenge, name, and user ID.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest%28challenge,name,userid,requeststyle%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](./asauthorizationprovider.md)
- [ASAuthorizationWebBrowserPlatformPublicKeyCredentialProvider](./asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq.md)
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
- [class ASAuthorizationSecurityKeyPublicKeyCredentialProvider](./asauthorizationsecuritykeypublickeycredentialprovider.md)
  A mechanism for providing public key credential requests to an app or service with a physical security key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialprovider)*