# ASAuthorizationPublicKeyCredentialAssertion

**Framework**: Authentication Services  
**Kind**: protocol

An interface for establishing a public key-based assertion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol ASAuthorizationPublicKeyCredentialAssertion : ASPublicKeyCredential
```

#### Overview

Both [`ASAuthorizationSecurityKeyPublicKeyCredentialAssertion`](asauthorizationsecuritykeypublickeycredentialassertion.md) and [`ASAuthorizationPlatformPublicKeyCredentialAssertion`](asauthorizationplatformpublickeycredentialassertion.md) adhere to this interface.

## Topics

### Getting the properties
- [var signature: Data!](asauthorizationpublickeycredentialassertion/signature.md)
  The signature for the assertion.
- [var userID: Data!](asauthorizationpublickeycredentialassertion/userid.md)
  A user identifier for the assertion.
- [var rawAuthenticatorData: Data!](asauthorizationpublickeycredentialassertion/rawauthenticatordata.md)
  A byte sequence that contains additional information about the credential.

## Relationships

### Inherits From
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [ASPublicKeyCredential](aspublickeycredential.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialAssertion](asauthorizationplatformpublickeycredentialassertion.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](asauthorizationsecuritykeypublickeycredentialassertion.md)

## See Also

- [class ASAuthorizationPlatformPublicKeyCredentialAssertion](asauthorizationplatformpublickeycredentialassertion.md)
  A class that represents the platform credential assertion type.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](asauthorizationsecuritykeypublickeycredentialassertion.md)
  A class that represents the security key credential assertion type.
- [protocol ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md)
  An interface for requesting a public key-based credential assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
  A class that defines the assertion request type for security key credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertion)*