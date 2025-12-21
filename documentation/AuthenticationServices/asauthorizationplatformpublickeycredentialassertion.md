# ASAuthorizationPlatformPublicKeyCredentialAssertion

**Framework**: Authentication Services  
**Kind**: class

A class that represents the platform credential assertion type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationPlatformPublicKeyCredentialAssertion
```

#### Overview

The device creates an assertion when signing in with an existing credential. Use this class to verify the platform credential assertion when the authorization controller calls [`authorizationController(controller:didCompleteWithAuthorization:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:).md).

## Topics

### Creating requests
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.
- [class ASAuthorizationPlatformPublicKeyCredentialDescriptor](asauthorizationplatformpublickeycredentialdescriptor.md)
  An object that holds the credential.
### Accessing assertion properties
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput?](asauthorizationplatformpublickeycredentialassertion/largeblob-29ggs.md)
  The request’s binary large object value.
### Instance Properties
- [var attachment: ASAuthorizationPublicKeyCredentialAttachment](asauthorizationplatformpublickeycredentialassertion/attachment.md)
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionOutput?](asauthorizationplatformpublickeycredentialassertion/prf-8o9sr.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [ASAuthorizationPublicKeyCredentialAssertion](asauthorizationpublickeycredentialassertion.md)
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

- [protocol ASAuthorizationPublicKeyCredentialAssertion](asauthorizationpublickeycredentialassertion.md)
  An interface for establishing a public key-based assertion.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](asauthorizationsecuritykeypublickeycredentialassertion.md)
  A class that represents the security key credential assertion type.
- [protocol ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md)
  An interface for requesting a public key-based credential assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
  A class that defines the assertion request type for security key credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialassertion)*