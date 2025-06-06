# credentialRevokedNotification

**Framework**: Authentication Services  
**Kind**: property

A notification that indicates the user’s credentials have been revoked and they should be signed out.

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
class let credentialRevokedNotification: NSNotification.Name
```

## See Also

- [func getCredentialState(forUserID: String, completion: (ASAuthorizationAppleIDProvider.CredentialState, (any Error)?) -> Void)](asauthorizationappleidprovider/getcredentialstate(foruserid:completion:).md)
  Returns the credential state for the given user in a completion handler.
- [ASAuthorizationAppleIDProvider.CredentialState](asauthorizationappleidprovider/credentialstate.md)
  Possible values for the credential state of a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider/credentialrevokednotification)*