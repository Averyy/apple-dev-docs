# ASAuthorizationPlatformPublicKeyCredentialRegistration

**Framework**: Authentication Services  
**Kind**: class

A newly created platform credential that results from a credential registration request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationPlatformPublicKeyCredentialRegistration
```

## Mentions

- [Supporting passkeys](supporting-passkeys.md)

#### Overview

Use this class to verify a successful platform authorization request in [`authorizationController(controller:didCompleteWithAuthorization:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:).md).

## Topics

### Accessing registration properties
- [var attachment: ASAuthorizationPublicKeyCredentialAttachment](asauthorizationplatformpublickeycredentialregistration/attachment.md)
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput?](asauthorizationplatformpublickeycredentialregistration/largeblob-5nvj9.md)
  The request’s binary large object value.
### Initializers
- [init?(coder: NSCoder)](asauthorizationplatformpublickeycredentialregistration/init(coder:).md)
### Instance Properties
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput?](asauthorizationplatformpublickeycredentialregistration/prf-3xcqu.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [ASAuthorizationPublicKeyCredentialRegistration](asauthorizationpublickeycredentialregistration.md)
- [ASPublicKeyCredential](aspublickeycredential.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol ASAuthorizationPublicKeyCredentialRegistration](asauthorizationpublickeycredentialregistration.md)
  An interface that credential registration requests adhere to.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](asauthorizationsecuritykeypublickeycredentialregistration.md)
  A newly created security key credential that results from a credential registration request.
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialregistrationrequest.md)
  The object for registering a new platform public key credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)
  The object for registering a new security key credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialregistration)*