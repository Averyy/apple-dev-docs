# getCredentialState(forUserID:completion:)

**Framework**: Authentication Services  
**Kind**: method

Returns the credential state for the given user in a completion handler.

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
func credentialState(forUserID userID: String) async throws -> ASAuthorizationAppleIDProvider.CredentialState
```

## Parameters

- `userID`: An opaque string associated with the Apple ID that your app receives in the credential’s   property after performing a successful authentication request.
- `completion`: A block the method calls to report the state and an optional error condition.

## See Also

- [ASAuthorizationAppleIDProvider.CredentialState](asauthorizationappleidprovider/credentialstate.md)
  Possible values for the credential state of a user.
- [class let credentialRevokedNotification: NSNotification.Name](asauthorizationappleidprovider/credentialrevokednotification.md)
  A notification that indicates the user’s credentials have been revoked and they should be signed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider/getcredentialstate(foruserid:completion:))*