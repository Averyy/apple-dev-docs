# friendListDescriptionMissing

**Framework**: GameKit  
**Kind**: property  
**Role**: Type Property

The system denies access to the local player’s friends list because the game didn’t provide a reason.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
static var friendListDescriptionMissing: GKError.Code { get }
```

#### Discussion

If your game wants access to the player’s friends, provide a reason by adding the [`NSGKFriendListUsageDescription`](../../BundleResources/information-property-list/nsgkfriendlistusagedescription.md) key to the information property list.

## See Also

### Error Codes
- [GKError.Code](./code.md)
  Error codes for the GameKit error domain.
- [static var authenticationInProgress: GKError.Code](./authenticationinprogress.md)
  The system can’t complete the requested operation because the local player is already authenticating.
- [static var cancelled: GKError.Code](./cancelled.md)
  The system canceled the requested operation or the user disabled it.
- [static var challengeInvalid: GKError.Code](./challengeinvalid.md)
  The challenge request failed due to invalid challenge data.
- [static var communicationsFailure: GKError.Code](./communicationsfailure.md)
  The system can’t complete the requested operation due to an error communicating with the server.
- [static var gameSessionRequestInvalid: GKError.Code](./gamesessionrequestinvalid.md)
  The properties of the game session request are impossible to fulfill.
- [static var gameUnrecognized: GKError.Code](./gameunrecognized.md)
  The system can’t complete the requested operation because Game Center doesn’t recognize the app.
- [static var invalidCredentials: GKError.Code](./invalidcredentials.md)
  The system can’t complete the requested operation because the user name or password are incorrect.
- [static var invalidParameter: GKError.Code](./invalidparameter.md)
  The system can’t complete the requested operation because one or more parameters are invalid.
- [static var invalidPlayer: GKError.Code](./invalidplayer.md)
  The system can’t complete the requested operation because the player is invalid.
- [static var invitationsDisabled: GKError.Code](./invitationsdisabled.md)
  The system can’t complete the requested operation because the receiving player has disabled invitations.
- [static var matchNotConnected: GKError.Code](./matchnotconnected.md)
  The system can’t complete the requested operation because the match isn’t connected to other players.
- [static var matchRequestInvalid: GKError.Code](./matchrequestinvalid.md)
  The system can’t complete the requested operation because the match request is invalid.
- [static var notAuthenticated: GKError.Code](./notauthenticated.md)
  The system can’t complete the requested operation because the system hasn’t initialized the local player.
- [static var notSupported: GKError.Code](./notsupported.md)
  The app doesn’t have Game Center enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/friendlistdescriptionmissing)*