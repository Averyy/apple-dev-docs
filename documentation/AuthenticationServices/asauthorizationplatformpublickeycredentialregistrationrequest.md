# ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

The object for registering a new platform public key credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest
```

```objc
@interface ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest : ASAuthorizationRequest
```

## Mentions

- [Supporting passkeys](./supporting-passkeys.md)

#### Overview

Create an instance of this class when registering for a new credential using platform authorization.

## Topics

### Accessing request properties
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput?](./asauthorizationplatformpublickeycredentialregistrationrequest/largeblob-5ismm.md)
  The request’s binary large object value.
### Instance Properties
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationInput?](./asauthorizationplatformpublickeycredentialregistrationrequest/prf-3d9iw.md)
- [var requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle](./asauthorizationplatformpublickeycredentialregistrationrequest/requeststyle-swift.property.md)
### Enumerations
- [ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle](./asauthorizationplatformpublickeycredentialregistrationrequest/requeststyle-swift.enum.md)

## Relationships

### Inherits From
- [ASAuthorizationRequest](./asauthorizationrequest.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialRegistrationRequest](./asauthorizationpublickeycredentialregistrationrequest.md)
- [ASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequest](./asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
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
- [class ASAuthorizationPlatformPublicKeyCredentialRegistration](./asauthorizationplatformpublickeycredentialregistration.md)
  A newly created platform credential that results from a credential registration request.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](./asauthorizationsecuritykeypublickeycredentialregistration.md)
  A newly created security key credential that results from a credential registration request.
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](./asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)
  The object for registering a new security key credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialregistrationrequest)*