# ASAuthorizationCredential

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface that all credentials share.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol ASAuthorizationCredential : NSCopying, NSSecureCoding, NSObjectProtocol
```

```objc
@protocol ASAuthorizationCredential <NSObject, NSCopying, NSSecureCoding>
```

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
### Inherited By
- [ASAuthorizationPublicKeyCredentialAssertion](./asauthorizationpublickeycredentialassertion.md)
- [ASAuthorizationPublicKeyCredentialRegistration](./asauthorizationpublickeycredentialregistration.md)
- [ASPublicKeyCredential](./aspublickeycredential.md)
### Conforming Types
- [ASAuthorizationAccountCreationPlatformPublicKeyCredential](./asauthorizationaccountcreationplatformpublickeycredential.md)
- [ASAuthorizationAppleIDCredential](./asauthorizationappleidcredential.md)
- [ASAuthorizationPlatformPublicKeyCredentialAssertion](./asauthorizationplatformpublickeycredentialassertion.md)
- [ASAuthorizationPlatformPublicKeyCredentialRegistration](./asauthorizationplatformpublickeycredentialregistration.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](./asauthorizationsecuritykeypublickeycredentialassertion.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](./asauthorizationsecuritykeypublickeycredentialregistration.md)
- [ASAuthorizationSingleSignOnCredential](./asauthorizationsinglesignoncredential.md)
- [ASOneTimeCodeCredential](./asonetimecodecredential.md)
- [ASPasskeyAssertionCredential](./aspasskeyassertioncredential.md)
- [ASPasskeyRegistrationCredential](./aspasskeyregistrationcredential.md)
- [ASPasswordCredential](./aspasswordcredential.md)

## See Also

### Getting the Credential
- [var credential: any ASAuthorizationCredential](./asauthorization/credential.md)
  Information provided about a user after successful authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcredential)*