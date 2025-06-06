# ASAuthorizationPublicKeyCredentialRegistration

**Framework**: Authentication Services  
**Kind**: protocol

An interface that credential registration requests adhere to.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol ASAuthorizationPublicKeyCredentialRegistration : ASPublicKeyCredential
```

## Topics

### Getting attestation information
- [var rawAttestationObject: Data?](asauthorizationpublickeycredentialregistration/rawattestationobject.md)
  A data object that contains the returned attestation.

## Relationships

### Inherits From
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [ASPublicKeyCredential](aspublickeycredential.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialRegistration](asauthorizationplatformpublickeycredentialregistration.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](asauthorizationsecuritykeypublickeycredentialregistration.md)

## See Also

- [class ASAuthorizationPlatformPublicKeyCredentialRegistration](asauthorizationplatformpublickeycredentialregistration.md)
  A newly created platform credential that results from a credential registration request.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](asauthorizationsecuritykeypublickeycredentialregistration.md)
  A newly created security key credential that results from a credential registration request.
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialregistrationrequest.md)
  The object for registering a new platform public key credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)
  The object for registering a new security key credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialregistration)*