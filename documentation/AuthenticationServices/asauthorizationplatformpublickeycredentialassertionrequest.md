# ASAuthorizationPlatformPublicKeyCredentialAssertionRequest

**Framework**: Authentication Services  
**Kind**: class

The concrete assertion request type for platform credentials.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest
```

## Mentions

- [Supporting passkeys](supporting-passkeys.md)

#### Overview

Use this class to sign in with an existing credential that the system stores in iCloud Keychain.

## Topics

### Getting the properties
- [var allowedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]](asauthorizationplatformpublickeycredentialassertionrequest/allowedcredentials.md)
  The array of allowed credentials.
### Instance Properties
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput?](asauthorizationplatformpublickeycredentialassertionrequest/largeblob-9kvvl.md)
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?](asauthorizationplatformpublickeycredentialassertionrequest/prf-47uoa.md)
- [var prf: __ASAuthorizationPublicKeyCredentialPRFAssertionInput?](asauthorizationplatformpublickeycredentialassertionrequest/prf-60tle.md)

## Relationships

### Inherits From
- [ASAuthorizationRequest](asauthorizationrequest.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md)
- [ASAuthorizationWebBrowserExternallyAuthenticatableRequest](asauthorizationwebbrowserexternallyauthenticatablerequest.md)
- [ASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest](asauthorizationwebbrowserplatformpublickeycredentialassertionrequest.md)
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
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
  A class that defines the assertion request type for security key credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialassertionrequest)*