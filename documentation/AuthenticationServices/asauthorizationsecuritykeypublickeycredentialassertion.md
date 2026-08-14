# ASAuthorizationSecurityKeyPublicKeyCredentialAssertion

**Framework**: Authentication Services  
**Kind**: class

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

#### Overview

The security key creates an assertion when signing in with an existing credential. Use this class to verify the security key credential assertion when the authorization controller calls [`authorizationController(controller:didCompleteWithAuthorization:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:).md).

## Topics

### Instance Properties
- [var appID: Bool](asauthorizationsecuritykeypublickeycredentialassertion/appid.md)
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionOutput?](asauthorizationsecuritykeypublickeycredentialassertion/prf-8ylo.md)
### Initializers
- [init?(coder: NSCoder)](asauthorizationsecuritykeypublickeycredentialassertion/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [ASAuthorizationPublicKeyCredentialAssertion](asauthorizationpublickeycredentialassertion.md)
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

- [protocol ASAuthorizationPublicKeyCredentialAssertion](asauthorizationpublickeycredentialassertion.md)
  An interface for establishing a public key-based assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertion](asauthorizationplatformpublickeycredentialassertion.md)
  A class that represents the platform credential assertion type.
- [protocol ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md)
  An interface for requesting a public key-based credential assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
  A class that defines the assertion request type for security key credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialassertion)*