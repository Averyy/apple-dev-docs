# ASAuthorizationResult.customMethod(_:)

**Framework**: Authentication Services  
**Kind**: case

A chosen custom authorization method.

**Availability**:
- tvOS 16.4+

## Declaration

```swift
case customMethod(ASAuthorizationCustomMethod)
```

## See Also

- [case appleID(ASAuthorizationAppleIDCredential)](asauthorizationresult/appleid(_:).md)
  A credential from an Apple ID authentication.
- [case passkeyAssertion(ASAuthorizationPlatformPublicKeyCredentialAssertion)](asauthorizationresult/passkeyassertion(_:).md)
  A passkey credential from an assertion request.
- [case passkeyRegistration(ASAuthorizationPlatformPublicKeyCredentialRegistration)](asauthorizationresult/passkeyregistration(_:).md)
  A new passkey credential from a registration request.
- [case password(ASPasswordCredential)](asauthorizationresult/password(_:).md)
  A password credential.
- [case securityKeyAssertion(ASAuthorizationSecurityKeyPublicKeyCredentialAssertion)](asauthorizationresult/securitykeyassertion(_:).md)
  A security key credential from an assertion request.
- [case securityKeyRegistration(ASAuthorizationSecurityKeyPublicKeyCredentialRegistration)](asauthorizationresult/securitykeyregistration(_:).md)
  A new security key credential from a registration request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationresult/custommethod(_:))*