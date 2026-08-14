# ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest

**Framework**: Authentication Services  
**Kind**: class

A class that defines the assertion request type for security key credentials.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest
```

## Mentions

- [Supporting Security Key Authentication Using Physical Keys](supporting-security-key-authentication-using-physical-keys.md)

#### Overview

Use this class to sign in with an existing credential on a security key.

## Topics

### Getting the properties
- [var allowedCredentials: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor]](asauthorizationsecuritykeypublickeycredentialassertionrequest/allowedcredentials.md)
  An array of allowed credentials.
### Instance Properties
- [var appID: String?](asauthorizationsecuritykeypublickeycredentialassertionrequest/appid.md)
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?](asauthorizationsecuritykeypublickeycredentialassertionrequest/prf-7pp6b.md)
- [var prf: __ASAuthorizationPublicKeyCredentialPRFAssertionInput?](asauthorizationsecuritykeypublickeycredentialassertionrequest/prf-99zke.md)

## Relationships

### Inherits From
- [ASAuthorizationRequest](asauthorizationrequest.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md)
- [ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialassertionrequest.md)
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
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
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](asauthorizationsecuritykeypublickeycredentialassertion.md)
  A class that represents the security key credential assertion type.
- [protocol ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md)
  An interface for requesting a public key-based credential assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialassertionrequest)*