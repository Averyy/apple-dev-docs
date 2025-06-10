# ASAuthorizationPlatformPublicKeyCredentialProvider

**Framework**: Authentication Services  
**Kind**: class

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

## Mentions

- [Supporting passkeys](supporting-passkeys.md)

#### Overview

The credential provider accesses public-private key pairs stored in iCloud Keychain for registration or authentication with a relying party. Instantiate this object, passing in the relying party identifier for the credentials.

## Topics

### Creating the provider
- [init(relyingPartyIdentifier: String)](asauthorizationplatformpublickeycredentialprovider/init(relyingpartyidentifier:).md)
  Creates the object with a relying party identifier.
### Creating the request
- [var relyingPartyIdentifier: String](asauthorizationplatformpublickeycredentialprovider/relyingpartyidentifier.md)
  The domain name of the service to register or authorize against.
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialprovider/createcredentialassertionrequest(challenge:).md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:).md)
  Creates an assertion request with a challenge, name, and user ID.
### Instance Methods
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:requeststyle:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](asauthorizationprovider.md)
- [ASAuthorizationWebBrowserPlatformPublicKeyCredentialProvider](asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ASAuthorizationSecurityKeyPublicKeyCredentialProvider](asauthorizationsecuritykeypublickeycredentialprovider.md)
  A mechanism for providing public key credential requests to an app or service with a physical security key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialprovider)*