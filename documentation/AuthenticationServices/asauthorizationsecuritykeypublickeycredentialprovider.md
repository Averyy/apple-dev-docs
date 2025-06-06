# ASAuthorizationSecurityKeyPublicKeyCredentialProvider

**Framework**: Authentication Services  
**Kind**: class

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

## Mentions

- [Supporting Security Key Authentication Using Physical Keys](supporting-security-key-authentication-using-physical-keys.md)

#### Overview

The credential provider accesses public-private key pairs stored on a physical security key for registration or authentication with a relying party. Instantiate this object, passing in the relying party identifier for the credentials.

## Topics

### Creating the provider
- [init(relyingPartyIdentifier: String)](asauthorizationsecuritykeypublickeycredentialprovider/init(relyingpartyidentifier:).md)
  Creates the object with a relying party identifier.
### Creating the request
- [var relyingPartyIdentifier: String](asauthorizationsecuritykeypublickeycredentialprovider/relyingpartyidentifier.md)
  The domain name of the service to authorize against.
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialprovider/createcredentialassertionrequest(challenge:).md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationsecuritykeypublickeycredentialprovider/createcredentialregistrationrequest(challenge:displayname:name:userid:).md)
  Creates an assertion request with a challenge, display name, and user ID.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](asauthorizationprovider.md)
- [ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider](asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ASAuthorizationPlatformPublicKeyCredentialProvider](asauthorizationplatformpublickeycredentialprovider.md)
  A mechanism for providing public key credential requests to an app or service with iCloud Keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialprovider)*