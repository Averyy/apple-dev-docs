# ASAuthorizationAppleIDProvider.CredentialState.authorized

**Framework**: Authentication Services  
**Kind**: case

The user is authorized.

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
case authorized
```

## See Also

- [ASAuthorizationAppleIDProvider.CredentialState.notFound](asauthorizationappleidprovider/credentialstate/notfound.md)
  The user hasn’t established a relationship with Sign in with Apple.
- [ASAuthorizationAppleIDProvider.CredentialState.revoked](asauthorizationappleidprovider/credentialstate/revoked.md)
  The given user’s authorization has been revoked and they should be signed out.
- [ASAuthorizationAppleIDProvider.CredentialState.transferred](asauthorizationappleidprovider/credentialstate/transferred.md)
  The app has been transferred to a different team, and you need to migrate the user’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider/credentialstate/authorized)*