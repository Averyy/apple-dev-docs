# ASAuthorizationPlatformPublicKeyCredentialAssertionRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASAuthorizationPlatformPublicKeyCredentialAssertionRequest : ASAuthorizationRequest
```

## Mentions

- [Supporting passkeys](./supporting-passkeys.md)

#### Overview

Use this class to sign in with an existing credential that the system stores in iCloud Keychain.

## Topics

### Accessing request properties
- [var allowedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]](./asauthorizationplatformpublickeycredentialassertionrequest/allowedcredentials.md)
  The array of allowed credentials.
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput?](./asauthorizationplatformpublickeycredentialassertionrequest/largeblob-9kvvl.md)
  The request’s binary large object value.
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?](./asauthorizationplatformpublickeycredentialassertionrequest/prf-47uoa.md)
- [largeBlob](./asauthorizationplatformpublickeycredentialassertionrequest/largeblob-5mg1q.md)
  The request’s binary large object value.
- [ASAuthorizationPublicKeyCredentialPRFAssertionInput](./asauthorizationpublickeycredentialprfassertioninput-c.class.md)
  A type that represents input for the web authentication PRF extension in passkey assertion requests.
### Instance Properties
- [prf](./asauthorizationplatformpublickeycredentialassertionrequest/prf-60tle.md)

## Relationships

### Inherits From
- [ASAuthorizationRequest](./asauthorizationrequest.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialAssertionRequest](./asauthorizationpublickeycredentialassertionrequest.md)
- [ASAuthorizationWebBrowserExternallyAuthenticatableRequest](./asauthorizationwebbrowserexternallyauthenticatablerequest.md)
- [ASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest](./asauthorizationwebbrowserplatformpublickeycredentialassertionrequest.md)
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
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](./asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
  A class that defines the assertion request type for security key credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialassertionrequest)*