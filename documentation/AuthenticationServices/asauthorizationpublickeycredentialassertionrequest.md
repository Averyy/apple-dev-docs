# ASAuthorizationPublicKeyCredentialAssertionRequest

**Framework**: Authentication Services  
**Kind**: protocol

An interface for requesting a public key-based credential assertion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol ASAuthorizationPublicKeyCredentialAssertionRequest : NSCopying, NSSecureCoding, NSObjectProtocol
```

## Topics

### Getting the properties
- [var challenge: Data](asauthorizationpublickeycredentialassertionrequest/challenge.md)
  The challenge to sign.
- [var relyingPartyIdentifier: String](asauthorizationpublickeycredentialassertionrequest/relyingpartyidentifier.md)
  The domain name of the website for the credential.
- [var allowedCredentials: [any ASAuthorizationPublicKeyCredentialDescriptor]](asauthorizationpublickeycredentialassertionrequest/allowedcredentials.md)
  A list of allowed credential descriptors the user attempts to sign in with.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialassertionrequest/userverificationpreference.md)
  A preference that indicates whether the authenticator attempts to verify the user at the time of sign-in.

## Relationships

### Inherits From
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialassertionrequest.md)

## See Also

- [protocol ASAuthorizationPublicKeyCredentialAssertion](asauthorizationpublickeycredentialassertion.md)
  An interface for establishing a public key-based assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertion](asauthorizationplatformpublickeycredentialassertion.md)
  A class that represents the platform credential assertion type.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](asauthorizationsecuritykeypublickeycredentialassertion.md)
  A class that represents the security key credential assertion type.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
  A class that defines the assertion request type for security key credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertionrequest)*