# ASAuthorizationResult.securityKeyRegistration(_:)

**Framework**: Authentication Services  
**Kind**: case

A new security key credential from a registration request.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
case securityKeyRegistration(ASAuthorizationSecurityKeyPublicKeyCredentialRegistration)
```

## See Also

- [case appleID(ASAuthorizationAppleIDCredential)](asauthorizationresult/appleid(_:).md)
  A credential from an Apple ID authentication.
- [case customMethod(ASAuthorizationCustomMethod)](asauthorizationresult/custommethod(_:).md)
  A chosen custom authorization method.
- [case passkeyAssertion(ASAuthorizationPlatformPublicKeyCredentialAssertion)](asauthorizationresult/passkeyassertion(_:).md)
  A passkey credential from an assertion request.
- [case passkeyRegistration(ASAuthorizationPlatformPublicKeyCredentialRegistration)](asauthorizationresult/passkeyregistration(_:).md)
  A new passkey credential from a registration request.
- [case password(ASPasswordCredential)](asauthorizationresult/password(_:).md)
  A password credential.
- [case securityKeyAssertion(ASAuthorizationSecurityKeyPublicKeyCredentialAssertion)](asauthorizationresult/securitykeyassertion(_:).md)
  A security key credential from an assertion request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationresult/securitykeyregistration(_:))*