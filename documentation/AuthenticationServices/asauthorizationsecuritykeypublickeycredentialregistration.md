# ASAuthorizationSecurityKeyPublicKeyCredentialRegistration

**Framework**: Authentication Services  
**Kind**: class

A newly created security key credential that results from a credential registration request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class ASAuthorizationSecurityKeyPublicKeyCredentialRegistration
```

## Mentions

- [Supporting Security Key Authentication Using Physical Keys](supporting-security-key-authentication-using-physical-keys.md)

#### Overview

Use this class to verify a successful security key authorization request in [`authorizationController(controller:didCompleteWithAuthorization:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:).md).

## Topics

### Instance Properties
- [var transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](asauthorizationsecuritykeypublickeycredentialregistration/transports.md)
  An array of transport types.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [ASAuthorizationPublicKeyCredentialRegistration](asauthorizationpublickeycredentialregistration.md)
- [ASPublicKeyCredential](aspublickeycredential.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol ASAuthorizationPublicKeyCredentialRegistration](asauthorizationpublickeycredentialregistration.md)
  An interface that credential registration requests adhere to.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistration](asauthorizationplatformpublickeycredentialregistration.md)
  A newly created platform credential that results from a credential registration request.
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialregistrationrequest.md)
  The object for registering a new platform public key credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)
  The object for registering a new security key credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialregistration)*