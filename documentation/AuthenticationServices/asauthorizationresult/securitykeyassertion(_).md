# ASAuthorizationResult.securityKeyAssertion(_:)

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

A security key credential from an assertion request.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
case securityKeyAssertion(ASAuthorizationSecurityKeyPublicKeyCredentialAssertion)
```

## See Also

### Authorization results
- [case appleID(ASAuthorizationAppleIDCredential)](./appleid%28_%29.md)
  A credential from an Apple ID authentication.
- [case customMethod(ASAuthorizationCustomMethod)](./custommethod%28_%29.md)
  A chosen custom authorization method.
- [case passkeyAssertion(ASAuthorizationPlatformPublicKeyCredentialAssertion)](./passkeyassertion%28_%29.md)
  A passkey credential from an assertion request.
- [case passkeyRegistration(ASAuthorizationPlatformPublicKeyCredentialRegistration)](./passkeyregistration%28_%29.md)
  A new passkey credential from a registration request.
- [case password(ASPasswordCredential)](./password%28_%29.md)
  A password credential.
- [case securityKeyRegistration(ASAuthorizationSecurityKeyPublicKeyCredentialRegistration)](./securitykeyregistration%28_%29.md)
  A new security key credential from a registration request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationresult/securitykeyassertion(_:))*