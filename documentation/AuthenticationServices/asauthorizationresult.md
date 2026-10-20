# ASAuthorizationResult

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

Describes the outcome of a successful authorization request.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
enum ASAuthorizationResult
```

## Topics

### Authorization results
- [case appleID(ASAuthorizationAppleIDCredential)](./asauthorizationresult/appleid%28_%29.md)
  A credential from an Apple ID authentication.
- [case customMethod(ASAuthorizationCustomMethod)](./asauthorizationresult/custommethod%28_%29.md)
  A chosen custom authorization method.
- [case passkeyAssertion(ASAuthorizationPlatformPublicKeyCredentialAssertion)](./asauthorizationresult/passkeyassertion%28_%29.md)
  A passkey credential from an assertion request.
- [case passkeyRegistration(ASAuthorizationPlatformPublicKeyCredentialRegistration)](./asauthorizationresult/passkeyregistration%28_%29.md)
  A new passkey credential from a registration request.
- [case password(ASPasswordCredential)](./asauthorizationresult/password%28_%29.md)
  A password credential.
- [case securityKeyAssertion(ASAuthorizationSecurityKeyPublicKeyCredentialAssertion)](./asauthorizationresult/securitykeyassertion%28_%29.md)
  A security key credential from an assertion request.
- [case securityKeyRegistration(ASAuthorizationSecurityKeyPublicKeyCredentialRegistration)](./asauthorizationresult/securitykeyregistration%28_%29.md)
  A new security key credential from a registration request.
### Enumeration Cases
- [case passkeyAccountCreation(ASAuthorizationAccountCreationPlatformPublicKeyCredential)](./asauthorizationresult/passkeyaccountcreation%28_%29.md)
  A newly created passkey credential and associated user information resulting from an account creation request.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Authorization requests
- [class ASAuthorizationController](./asauthorizationcontroller.md)
  A controller that manages authorization requests that a provider creates.
- [struct AuthorizationController](./authorizationcontroller.md)
  A SwiftUI environment value that views use to perform authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationresult)*