# ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest

**Framework**: Authentication Services  
**Kind**: class

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

#### Overview

Create an instance of this class when registering for a new credential using security key authorization.

## Topics

### Getting the properties
- [var credentialParameters: [ASAuthorizationPublicKeyCredentialParameters]](asauthorizationsecuritykeypublickeycredentialregistrationrequest/credentialparameters.md)
  An array of parameters for the credential.
- [var excludedCredentials: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor]](asauthorizationsecuritykeypublickeycredentialregistrationrequest/excludedcredentials.md)
  An array of excluded parameters for the credential.
- [var residentKeyPreference: ASAuthorizationPublicKeyCredentialResidentKeyPreference](asauthorizationsecuritykeypublickeycredentialregistrationrequest/residentkeypreference.md)
  The preference that indicates where the resident key resides.

## Relationships

### Inherits From
- [ASAuthorizationRequest](asauthorizationrequest.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md)
- [ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialregistrationrequest.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol ASAuthorizationPublicKeyCredentialRegistration](asauthorizationpublickeycredentialregistration.md)
  An interface that credential registration requests adhere to.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistration](asauthorizationplatformpublickeycredentialregistration.md)
  A newly created platform credential that results from a credential registration request.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](asauthorizationsecuritykeypublickeycredentialregistration.md)
  A newly created security key credential that results from a credential registration request.
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialregistrationrequest.md)
  The object for registering a new platform public key credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialregistrationrequest)*