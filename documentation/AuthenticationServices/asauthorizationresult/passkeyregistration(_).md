# ASAuthorizationResult.passkeyRegistration(_:)

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

A new passkey credential from a registration request.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
case passkeyRegistration(ASAuthorizationPlatformPublicKeyCredentialRegistration)
```

## See Also

### Authorization results
- [case appleID(ASAuthorizationAppleIDCredential)](./appleid%28_%29.md)
  A credential from an Apple ID authentication.
- [case customMethod(ASAuthorizationCustomMethod)](./custommethod%28_%29.md)
  A chosen custom authorization method.
- [case passkeyAssertion(ASAuthorizationPlatformPublicKeyCredentialAssertion)](./passkeyassertion%28_%29.md)
  A passkey credential from an assertion request.
- [case password(ASPasswordCredential)](./password%28_%29.md)
  A password credential.
- [case securityKeyAssertion(ASAuthorizationSecurityKeyPublicKeyCredentialAssertion)](./securitykeyassertion%28_%29.md)
  A security key credential from an assertion request.
- [case securityKeyRegistration(ASAuthorizationSecurityKeyPublicKeyCredentialRegistration)](./securitykeyregistration%28_%29.md)
  A new security key credential from a registration request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationresult/passkeyregistration(_:))*