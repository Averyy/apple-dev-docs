# ASAuthorizationResult.customMethod(_:)

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

A chosen custom authorization method.

**Availability**:
- tvOS 16.4+

## Declaration

```swift
case customMethod(ASAuthorizationCustomMethod)
```

## See Also

### Authorization results
- [case appleID(ASAuthorizationAppleIDCredential)](./appleid%28_%29.md)
  A credential from an Apple ID authentication.
- [case passkeyAssertion(ASAuthorizationPlatformPublicKeyCredentialAssertion)](./passkeyassertion%28_%29.md)
  A passkey credential from an assertion request.
- [case passkeyRegistration(ASAuthorizationPlatformPublicKeyCredentialRegistration)](./passkeyregistration%28_%29.md)
  A new passkey credential from a registration request.
- [case password(ASPasswordCredential)](./password%28_%29.md)
  A password credential.
- [case securityKeyAssertion(ASAuthorizationSecurityKeyPublicKeyCredentialAssertion)](./securitykeyassertion%28_%29.md)
  A security key credential from an assertion request.
- [case securityKeyRegistration(ASAuthorizationSecurityKeyPublicKeyCredentialRegistration)](./securitykeyregistration%28_%29.md)
  A new security key credential from a registration request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationresult/custommethod(_:))*