# ASAuthorizationAppleIDProvider.CredentialState.transferred

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

The app has been transferred to a different team, and you need to migrate the user’s identifier.

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
case transferred
```

```c
ASAuthorizationAppleIDProviderCredentialTransferred
```

## See Also

### User Credential States
- [ASAuthorizationAppleIDProvider.CredentialState.authorized](./authorized.md)
  The user is authorized.
- [ASAuthorizationAppleIDProvider.CredentialState.notFound](./notfound.md)
  The user hasn’t established a relationship with Sign in with Apple.
- [ASAuthorizationAppleIDProvider.CredentialState.revoked](./revoked.md)
  The given user’s authorization has been revoked and they should be signed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider/credentialstate/transferred)*