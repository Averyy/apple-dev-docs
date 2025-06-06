# ASAuthorizationCredential

**Framework**: Authentication Services  
**Kind**: protocol

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

## Relationships

### Inherits From
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
### Inherited By
- [ASAuthorizationPublicKeyCredentialAssertion](asauthorizationpublickeycredentialassertion.md)
- [ASAuthorizationPublicKeyCredentialRegistration](asauthorizationpublickeycredentialregistration.md)
- [ASPublicKeyCredential](aspublickeycredential.md)
### Conforming Types
- [ASAuthorizationAppleIDCredential](asauthorizationappleidcredential.md)
- [ASAuthorizationPlatformPublicKeyCredentialAssertion](asauthorizationplatformpublickeycredentialassertion.md)
- [ASAuthorizationPlatformPublicKeyCredentialRegistration](asauthorizationplatformpublickeycredentialregistration.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](asauthorizationsecuritykeypublickeycredentialassertion.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](asauthorizationsecuritykeypublickeycredentialregistration.md)
- [ASAuthorizationSingleSignOnCredential](asauthorizationsinglesignoncredential.md)
- [ASOneTimeCodeCredential](asonetimecodecredential.md)
- [ASPasskeyAssertionCredential](aspasskeyassertioncredential.md)
- [ASPasskeyRegistrationCredential](aspasskeyregistrationcredential.md)
- [ASPasswordCredential](aspasswordcredential.md)

## See Also

- [var credential: any ASAuthorizationCredential](asauthorization/credential.md)
  Information provided about a user after successful authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcredential)*