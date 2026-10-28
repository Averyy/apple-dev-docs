# ASAuthorizationSecurityKeyPublicKeyCredentialAssertion

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A class that represents the security key credential assertion type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class ASAuthorizationSecurityKeyPublicKeyCredentialAssertion
```

```objc
@interface ASAuthorizationSecurityKeyPublicKeyCredentialAssertion : NSObject
```

## Overview

The security key creates an assertion when signing in with an existing credential. Use this class to verify the security key credential assertion when the authorization controller calls [`authorizationController(controller:didCompleteWithAuthorization:)`](./asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewithauthorization%29.md).

## Topics

### Instance Properties
- [var appID: Bool](./asauthorizationsecuritykeypublickeycredentialassertion/appid.md)
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionOutput?](./asauthorizationsecuritykeypublickeycredentialassertion/prf-8ylo.md)
- [prf](./asauthorizationsecuritykeypublickeycredentialassertion/prf-57nvr.md)
### Initializers
- [init?(coder: NSCoder)](./asauthorizationsecuritykeypublickeycredentialassertion/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](./asauthorizationcredential.md)
- [ASAuthorizationPublicKeyCredentialAssertion](./asauthorizationpublickeycredentialassertion.md)
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

### Account authentication
- [protocol ASAuthorizationPublicKeyCredentialAssertion](./asauthorizationpublickeycredentialassertion.md)
  An interface for establishing a public key-based assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertion](./asauthorizationplatformpublickeycredentialassertion.md)
  A class that represents the platform credential assertion type.
- [protocol ASAuthorizationPublicKeyCredentialAssertionRequest](./asauthorizationpublickeycredentialassertionrequest.md)
  An interface for requesting a public key-based credential assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](./asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](./asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
  A class that defines the assertion request type for security key credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialassertion)*