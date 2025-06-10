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

## Relationships

### Inherits From
- [ASAuthorizationRequest](asauthorizationrequest.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md)
- [ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialassertionrequest.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

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