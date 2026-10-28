# ASAuthorizationPlatformPublicKeyCredentialRegistration

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASAuthorizationPlatformPublicKeyCredentialRegistration : NSObject
```

## Mentions

- [Supporting passkeys](./supporting-passkeys.md)

## Overview

Use this class to verify a successful platform authorization request in [`authorizationController(controller:didCompleteWithAuthorization:)`](./asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewithauthorization%29.md).

## Topics

### Accessing registration properties
- [var attachment: ASAuthorizationPublicKeyCredentialAttachment](./asauthorizationplatformpublickeycredentialregistration/attachment.md)
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput?](./asauthorizationplatformpublickeycredentialregistration/largeblob-5nvj9.md)
  The request’s binary large object value.
- [largeBlob](./asauthorizationplatformpublickeycredentialregistration/largeblob-jhnw.md)
  The request’s binary large object value.
### Initializers
- [init?(coder: NSCoder)](./asauthorizationplatformpublickeycredentialregistration/init%28coder%29.md)
### Instance Properties
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput?](./asauthorizationplatformpublickeycredentialregistration/prf-3xcqu.md)
- [prf](./asauthorizationplatformpublickeycredentialregistration/prf-49gbm.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](./asauthorizationcredential.md)
- [ASAuthorizationPublicKeyCredentialRegistration](./asauthorizationpublickeycredentialregistration.md)
- [ASPublicKeyCredential](./aspublickeycredential.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Account registration
- [protocol ASAuthorizationPublicKeyCredentialRegistration](./asauthorizationpublickeycredentialregistration.md)
  An interface that credential registration requests adhere to.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](./asauthorizationsecuritykeypublickeycredentialregistration.md)
  A newly created security key credential that results from a credential registration request.
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](./asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./asauthorizationplatformpublickeycredentialregistrationrequest.md)
  The object for registering a new platform public key credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)
  The object for registering a new security key credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialregistration)*