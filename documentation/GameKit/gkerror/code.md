# GKError.Code

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

Error codes for the GameKit error domain.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum Code
```

```c
enum GKErrorCode : NSInteger;
```

## Topics

### Configuration Errors
- [GKError.Code.gameUnrecognized](./code/gameunrecognized.md)
  The system can’t complete the requested operation because Game Center doesn’t recognize the app.
- [GKError.Code.notSupported](./code/notsupported.md)
  The app doesn’t have Game Center enabled.
- [GKError.Code.appUnlisted](./code/appunlisted.md)
  The system can’t complete the requested operation because the game isn’t available on the App Store.
### Communication Errors
- [GKError.Code.unknown](./code/unknown.md)
  The system can’t complete the requested operation due to an unknown error.
- [GKError.Code.cancelled](./code/cancelled.md)
  The system canceled the requested operation or the user disabled it.
- [GKError.Code.communicationsFailure](./code/communicationsfailure.md)
  The system can’t complete the requested operation due to an error communicating with the server.
- [GKError.Code.invalidPlayer](./code/invalidplayer.md)
  The system can’t complete the requested operation because the player is invalid.
- [GKError.Code.invalidParameter](./code/invalidparameter.md)
  The system can’t complete the requested operation because one or more parameters are invalid.
- [GKError.Code.gameSessionRequestInvalid](./code/gamesessionrequestinvalid.md)
  The properties of the game session request are impossible to fulfill.
- [GKError.Code.apiNotAvailable](./code/apinotavailable.md)
  The system can’t complete the requested operation because the API isn’t available.
- [GKError.Code.connectionTimeout](./code/connectiontimeout.md)
  The system can’t complete the requested operation because the connection timed out.
- [GKError.Code.apiObsolete](./code/apiobsolete.md)
  The system can’t complete the requested operation because Apple deprecated the API.
### Player-Related Errors
- [GKError.Code.userDenied](./code/userdenied.md)
  The system can’t complete the requested operation because the user denied it.
- [GKError.Code.invalidCredentials](./code/invalidcredentials.md)
  The system can’t complete the requested operation because the user name or password are incorrect.
- [GKError.Code.notAuthenticated](./code/notauthenticated.md)
  The system can’t complete the requested operation because the system hasn’t authorized the player.
- [GKError.Code.authenticationInProgress](./code/authenticationinprogress.md)
  The system can’t complete the requested operation because the local player is already authenticating.
- [GKError.Code.parentalControlsBlocked](./code/parentalcontrolsblocked.md)
  The system can’t complete the requested operation because the user disabled this feature in Restrictions.
- [GKError.Code.playerStatusExceedsMaximumLength](./code/playerstatusexceedsmaximumlength.md)
  The player’s status exceeds the maximum length.
- [GKError.Code.playerStatusInvalid](./code/playerstatusinvalid.md)
  The player’s status is invalid.
- [GKError.Code.underage](./code/underage.md)
  The system can’t complete the requested operation because this feature isn’t available to underage players.
- [GKError.Code.playerPhotoFailure](./code/playerphotofailure.md)
  The system can’t complete the requested operation to retrieve a player’s photo.
- [GKError.Code.ubiquityContainerUnavailable](./code/ubiquitycontainerunavailable.md)
  The system can’t complete the requested operation because the user hasn’t signed in to iCloud or hasn’t enabled iCloud Drive.
- [GKError.Code.notAuthorized](./code/notauthorized.md)
  The system can’t complete the requested operation because the system hasn’t authorized the player.
- [GKError.Code.iCloudUnavailable](./code/icloudunavailable.md)
  The system can’t complete the requested operation because it can’t access the player’s iCloud account.
- [GKError.Code.lockdownMode](./code/lockdownmode.md)
  The system can’t complete the requested operation because the player enabled Lockdown Mode on the device.
### Friend List Errors
- [GKError.Code.friendListDescriptionMissing](./code/friendlistdescriptionmissing.md)
  Access to the local player’s list of friends denied for lack of a reason.
- [GKError.Code.friendListRestricted](./code/friendlistrestricted.md)
  Access to the local player’s list of friends restricted.
- [GKError.Code.friendListDenied](./code/friendlistdenied.md)
  Access to the local player’s list of friends denied.
- [GKError.Code.friendRequestNotAvailable](./code/friendrequestnotavailable.md)
  The player can’t send a friend request at this time from this device.
### Matchmaking Errors
- [GKError.Code.matchRequestInvalid](./code/matchrequestinvalid.md)
  The system can’t complete the requested operation because the match request is invalid.
- [GKError.Code.unexpectedConnection](./code/unexpectedconnection.md)
  An unexpected player has connected to a match.
- [GKError.Code.invitationsDisabled](./code/invitationsdisabled.md)
  The system can’t complete the requested operation because the receiving player has disabled invitations.
- [GKError.Code.matchNotConnected](./code/matchnotconnected.md)
  The system can’t complete the requested operation because the match isn’t connected to other players.
- [GKError.Code.restrictedToAutomatch](./code/restrictedtoautomatch.md)
  The system can’t complete the requested operation because the player is using automatch.
### Turn-Based Game Errors
- [GKError.Code.turnBasedMatchDataTooLarge](./code/turnbasedmatchdatatoolarge.md)
  The system can’t complete the requested operation because the match data is too large.
- [GKError.Code.turnBasedTooManySessions](./code/turnbasedtoomanysessions.md)
  The system can’t complete the requested operation because it exceeds the maximum number of sessions.
- [GKError.Code.turnBasedInvalidParticipant](./code/turnbasedinvalidparticipant.md)
  The system can’t complete the requested operation because the specified participant is invalid.
- [GKError.Code.turnBasedInvalidTurn](./code/turnbasedinvalidturn.md)
  The system can’t complete the requested operation because the participant doesn’t have the required turn state.
- [GKError.Code.turnBasedInvalidState](./code/turnbasedinvalidstate.md)
  The system can’t complete the requested operation because the session is in an invalid state.
### Leaderboard Errors
- [GKError.Code.scoreNotSet](./code/scorenotset.md)
  The system can’t complete the requested operation because the system hasn’t set the score.
### Challenges Errors
- [GKError.Code.challengeInvalid](./code/challengeinvalid.md)
  The challenge request failed due to invalid challenge data.
### Enumeration Cases
- [GKError.Code.debugMode](./code/debugmode.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct GKError](../gkerror.md)
  The error structure used by this framework.
- [let GKErrorDomain: String](../gkerrordomain.md)
  The error domain for general game errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code)*