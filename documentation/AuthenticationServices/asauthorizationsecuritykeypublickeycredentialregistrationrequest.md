# ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

The object for registering a new security key credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest
```

```objc
@interface ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest : ASAuthorizationRequest
```

## Overview

Create an instance of this class when registering for a new credential using security key authorization.

## Topics

### Getting the properties
- [var credentialParameters: [ASAuthorizationPublicKeyCredentialParameters]](./asauthorizationsecuritykeypublickeycredentialregistrationrequest/credentialparameters.md)
  An array of parameters for the credential.
- [var excludedCredentials: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor]](./asauthorizationsecuritykeypublickeycredentialregistrationrequest/excludedcredentials.md)
  An array of excluded parameters for the credential.
- [var residentKeyPreference: ASAuthorizationPublicKeyCredentialResidentKeyPreference](./asauthorizationsecuritykeypublickeycredentialregistrationrequest/residentkeypreference.md)
  The preference that indicates where the resident key resides.
### Instance Properties
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationInput?](./asauthorizationsecuritykeypublickeycredentialregistrationrequest/prf-964zl.md)
- [prf](./asauthorizationsecuritykeypublickeycredentialregistrationrequest/prf-2ys9l.md)

## Relationships

### Inherits From
- [ASAuthorizationRequest](./asauthorizationrequest.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialRegistrationRequest](./asauthorizationpublickeycredentialregistrationrequest.md)
- [ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest](./asauthorizationwebbrowsersecuritykeypublickeycredentialregistrationrequest.md)
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
- [class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./asauthorizationplatformpublickeycredentialregistrationrequest.md)
  The object for registering a new platform public key credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialregistrationrequest)*