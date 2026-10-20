# ASAuthorizationSecurityKeyPublicKeyCredentialRegistration

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASAuthorizationSecurityKeyPublicKeyCredentialRegistration : NSObject
```

## Mentions

- [Supporting Security Key Authentication Using Physical Keys](./supporting-security-key-authentication-using-physical-keys.md)

#### Overview

Use this class to verify a successful security key authorization request in [`authorizationController(controller:didCompleteWithAuthorization:)`](./asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewithauthorization%29.md).

## Topics

### Instance Properties
- [var transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](./asauthorizationsecuritykeypublickeycredentialregistration/transports.md)
  An array of transport types.
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput?](./asauthorizationsecuritykeypublickeycredentialregistration/prf-2p2lg.md)
### Initializers
- [init?(coder: NSCoder)](./asauthorizationsecuritykeypublickeycredentialregistration/init%28coder%29.md)

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
- [class ASAuthorizationPlatformPublicKeyCredentialRegistration](./asauthorizationplatformpublickeycredentialregistration.md)
  A newly created platform credential that results from a credential registration request.
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](./asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./asauthorizationplatformpublickeycredentialregistrationrequest.md)
  The object for registering a new platform public key credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)
  The object for registering a new security key credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialregistration)*