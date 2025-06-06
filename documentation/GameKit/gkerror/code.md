# GKError.Code

**Framework**: GameKit  
**Kind**: enum

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

## Topics

### Configuration Errors
- [GKError.Code.gameUnrecognized](gkerror/code/gameunrecognized.md)
  The system can’t complete the requested operation because Game Center doesn’t recognize the app.
- [GKError.Code.notSupported](gkerror/code/notsupported.md)
  The app doesn’t have Game Center enabled.
- [GKError.Code.appUnlisted](gkerror/code/appunlisted.md)
  The system can’t complete the requested operation because the game isn’t available on the App Store.
### Communication Errors
- [GKError.Code.unknown](gkerror/code/unknown.md)
  The system can’t complete the requested operation due to an unknown error.
- [GKError.Code.cancelled](gkerror/code/cancelled.md)
  The system canceled the requested operation or the user disabled it.
- [GKError.Code.communicationsFailure](gkerror/code/communicationsfailure.md)
  The system can’t complete the requested operation due to an error communicating with the server.
- [GKError.Code.invalidPlayer](gkerror/code/invalidplayer.md)
  The system can’t complete the requested operation because the player is invalid.
- [GKError.Code.invalidParameter](gkerror/code/invalidparameter.md)
  The system can’t complete the requested operation because one or more parameters are invalid.
- [GKError.Code.gameSessionRequestInvalid](gkerror/code/gamesessionrequestinvalid.md)
  The properties of the game session request are impossible to fulfill.
- [GKError.Code.apiNotAvailable](gkerror/code/apinotavailable.md)
  The system can’t complete the requested operation because the API isn’t available.
- [GKError.Code.connectionTimeout](gkerror/code/connectiontimeout.md)
  The system can’t complete the requested operation because the connection timed out.
- [GKError.Code.apiObsolete](gkerror/code/apiobsolete.md)
  The system can’t complete the requested operation because Apple deprecated the API.
### Player-Related Errors
- [GKError.Code.userDenied](gkerror/code/userdenied.md)
  The system can’t complete the requested operation because the user denied it.
- [GKError.Code.invalidCredentials](gkerror/code/invalidcredentials.md)
  The system can’t complete the requested operation because the user name or password are incorrect.
- [GKError.Code.notAuthenticated](gkerror/code/notauthenticated.md)
  The system can’t complete the requested operation because the system hasn’t authorized the player.
- [GKError.Code.authenticationInProgress](gkerror/code/authenticationinprogress.md)
  The system can’t complete the requested operation because the local player is already authenticating.
- [GKError.Code.parentalControlsBlocked](gkerror/code/parentalcontrolsblocked.md)
  The system can’t complete the requested operation because the user disabled this feature in Restrictions.
- [GKError.Code.playerStatusExceedsMaximumLength](gkerror/code/playerstatusexceedsmaximumlength.md)
  The player’s status exceeds the maximum length.
- [GKError.Code.playerStatusInvalid](gkerror/code/playerstatusinvalid.md)
  The player’s status is invalid.
- [GKError.Code.underage](gkerror/code/underage.md)
  The system can’t complete the requested operation because this feature isn’t available to underage players.
- [GKError.Code.playerPhotoFailure](gkerror/code/playerphotofailure.md)
  The system can’t complete the requested operation to retrieve a player’s photo.
- [GKError.Code.ubiquityContainerUnavailable](gkerror/code/ubiquitycontainerunavailable.md)
  The system can’t complete the requested operation because the user hasn’t signed in to iCloud or hasn’t enabled iCloud Drive.
- [GKError.Code.notAuthorized](gkerror/code/notauthorized.md)
  The system can’t complete the requested operation because the system hasn’t authorized the player.
- [GKError.Code.iCloudUnavailable](gkerror/code/icloudunavailable.md)
  The system can’t complete the requested operation because it can’t access the player’s iCloud account.
- [GKError.Code.lockdownMode](gkerror/code/lockdownmode.md)
  The system can’t complete the requested operation because the player enabled Lockdown Mode on the device.
### Friend List Errors
- [GKError.Code.friendListDescriptionMissing](gkerror/code/friendlistdescriptionmissing.md)
  Access to the local player’s list of friends denied for lack of a reason.
- [GKError.Code.friendListRestricted](gkerror/code/friendlistrestricted.md)
  Access to the local player’s list of friends restricted.
- [GKError.Code.friendListDenied](gkerror/code/friendlistdenied.md)
  Access to the local player’s list of friends denied.
- [GKError.Code.friendRequestNotAvailable](gkerror/code/friendrequestnotavailable.md)
  The player can’t send a friend request at this time from this device.
### Matchmaking Errors
- [GKError.Code.matchRequestInvalid](gkerror/code/matchrequestinvalid.md)
  The system can’t complete the requested operation because the match request is invalid.
- [GKError.Code.unexpectedConnection](gkerror/code/unexpectedconnection.md)
  An unexpected player has connected to a match.
- [GKError.Code.invitationsDisabled](gkerror/code/invitationsdisabled.md)
  The system can’t complete the requested operation because the receiving player has disabled invitations.
- [GKError.Code.matchNotConnected](gkerror/code/matchnotconnected.md)
  The system can’t complete the requested operation because the match isn’t connected to other players.
- [GKError.Code.restrictedToAutomatch](gkerror/code/restrictedtoautomatch.md)
  The system can’t complete the requested operation because the player is using automatch.
### Turn-Based Game Errors
- [GKError.Code.turnBasedMatchDataTooLarge](gkerror/code/turnbasedmatchdatatoolarge.md)
  The system can’t complete the requested operation because the match data is too large.
- [GKError.Code.turnBasedTooManySessions](gkerror/code/turnbasedtoomanysessions.md)
  The system can’t complete the requested operation because it exceeds the maximum number of sessions.
- [GKError.Code.turnBasedInvalidParticipant](gkerror/code/turnbasedinvalidparticipant.md)
  The system can’t complete the requested operation because the specified participant is invalid.
- [GKError.Code.turnBasedInvalidTurn](gkerror/code/turnbasedinvalidturn.md)
  The system can’t complete the requested operation because the participant doesn’t have the required turn state.
- [GKError.Code.turnBasedInvalidState](gkerror/code/turnbasedinvalidstate.md)
  The system can’t complete the requested operation because the session is in an invalid state.
### Leaderboard Errors
- [GKError.Code.scoreNotSet](gkerror/code/scorenotset.md)
  The system can’t complete the requested operation because the system hasn’t set the score.
### Challenges Errors
- [GKError.Code.challengeInvalid](gkerror/code/challengeinvalid.md)
  The challenge request failed due to invalid challenge data.
### Enumeration Cases
- [GKError.Code.debugMode](gkerror/code/debugmode.md)
### Initializers
- [init?(rawValue: Int)](gkerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct GKError](gkerror.md)
  The error structure used by this framework.
- [let GKErrorDomain: String](gkerrordomain.md)
  The error domain for general game errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code)*