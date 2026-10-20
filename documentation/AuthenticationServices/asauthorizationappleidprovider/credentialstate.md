# ASAuthorizationAppleIDProvider.CredentialState

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum ASAuthorizationAppleIDProviderCredentialState : NSInteger;
```

## Topics

### User Credential States
- [ASAuthorizationAppleIDProvider.CredentialState.authorized](./credentialstate/authorized.md)
  The user is authorized.
- [ASAuthorizationAppleIDProvider.CredentialState.notFound](./credentialstate/notfound.md)
  The user hasn’t established a relationship with Sign in with Apple.
- [ASAuthorizationAppleIDProvider.CredentialState.revoked](./credentialstate/revoked.md)
  The given user’s authorization has been revoked and they should be signed out.
- [ASAuthorizationAppleIDProvider.CredentialState.transferred](./credentialstate/transferred.md)
  The app has been transferred to a different team, and you need to migrate the user’s identifier.
### Initializers
- [init?(rawValue: Int)](./credentialstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting State
- [func getCredentialState(forUserID: String, completion: (ASAuthorizationAppleIDProvider.CredentialState, (any Error)?) -> Void)](./getcredentialstate%28foruserid,completion%29.md)
  Returns the credential state for the given user in a completion handler.
- [class let credentialRevokedNotification: NSNotification.Name](./credentialrevokednotification.md)
  A notification that indicates the user’s credentials have been revoked and they should be signed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider/credentialstate)*