# ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest : ASAuthorizationRequest
```

## Mentions

- [Supporting Security Key Authentication Using Physical Keys](./supporting-security-key-authentication-using-physical-keys.md)

#### Overview

Use this class to sign in with an existing credential on a security key.

## Topics

### Getting the properties
- [var allowedCredentials: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor]](./asauthorizationsecuritykeypublickeycredentialassertionrequest/allowedcredentials.md)
  An array of allowed credentials.
### Instance Properties
- [var appID: String?](./asauthorizationsecuritykeypublickeycredentialassertionrequest/appid.md)
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?](./asauthorizationsecuritykeypublickeycredentialassertionrequest/prf-7pp6b.md)
- [var prf: __ASAuthorizationPublicKeyCredentialPRFAssertionInput?](./asauthorizationsecuritykeypublickeycredentialassertionrequest/prf-99zke.md)

## Relationships

### Inherits From
- [ASAuthorizationRequest](./asauthorizationrequest.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialAssertionRequest](./asauthorizationpublickeycredentialassertionrequest.md)
- [ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest](./asauthorizationwebbrowsersecuritykeypublickeycredentialassertionrequest.md)
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

### Account authentication
- [protocol ASAuthorizationPublicKeyCredentialAssertion](./asauthorizationpublickeycredentialassertion.md)
  An interface for establishing a public key-based assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertion](./asauthorizationplatformpublickeycredentialassertion.md)
  A class that represents the platform credential assertion type.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](./asauthorizationsecuritykeypublickeycredentialassertion.md)
  A class that represents the security key credential assertion type.
- [protocol ASAuthorizationPublicKeyCredentialAssertionRequest](./asauthorizationpublickeycredentialassertionrequest.md)
  An interface for requesting a public key-based credential assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](./asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialassertionrequest)*