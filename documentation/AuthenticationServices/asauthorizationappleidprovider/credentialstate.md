# ASAuthorizationAppleIDProvider.CredentialState

**Framework**: Authentication Services  
**Kind**: enum

Possible values for the credential state of a user.

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
enum CredentialState
```

## Topics

### User Credential States
- [ASAuthorizationAppleIDProvider.CredentialState.authorized](asauthorizationappleidprovider/credentialstate/authorized.md)
  The user is authorized.
- [ASAuthorizationAppleIDProvider.CredentialState.notFound](asauthorizationappleidprovider/credentialstate/notfound.md)
  The user hasn’t established a relationship with Sign in with Apple.
- [ASAuthorizationAppleIDProvider.CredentialState.revoked](asauthorizationappleidprovider/credentialstate/revoked.md)
  The given user’s authorization has been revoked and they should be signed out.
- [ASAuthorizationAppleIDProvider.CredentialState.transferred](asauthorizationappleidprovider/credentialstate/transferred.md)
  The app has been transferred to a different team, and you need to migrate the user’s identifier.
### Initializers
- [init?(rawValue: Int)](asauthorizationappleidprovider/credentialstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func getCredentialState(forUserID: String, completion: (ASAuthorizationAppleIDProvider.CredentialState, (any Error)?) -> Void)](asauthorizationappleidprovider/getcredentialstate(foruserid:completion:).md)
  Returns the credential state for the given user in a completion handler.
- [class let credentialRevokedNotification: NSNotification.Name](asauthorizationappleidprovider/credentialrevokednotification.md)
  A notification that indicates the user’s credentials have been revoked and they should be signed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider/credentialstate)*