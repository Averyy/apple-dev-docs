# ASAuthorizationAppleIDProvider.CredentialState.notFound

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

The user hasn’t established a relationship with Sign in with Apple.

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
case notFound
```

```c
ASAuthorizationAppleIDProviderCredentialNotFound
```

## See Also

### User Credential States
- [ASAuthorizationAppleIDProvider.CredentialState.authorized](./authorized.md)
  The user is authorized.
- [ASAuthorizationAppleIDProvider.CredentialState.revoked](./revoked.md)
  The given user’s authorization has been revoked and they should be signed out.
- [ASAuthorizationAppleIDProvider.CredentialState.transferred](./transferred.md)
  The app has been transferred to a different team, and you need to migrate the user’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider/credentialstate/notfound)*