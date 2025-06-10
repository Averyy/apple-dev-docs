# GKError

**Framework**: GameKit  
**Kind**: struct

The error structure used by this framework.

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
struct GKError
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

## Topics

### Error Codes
- [GKError.Code](gkerror/code.md)
  Error codes for the GameKit error domain.
- [static var authenticationInProgress: GKError.Code](gkerror/authenticationinprogress.md)
  The system can’t complete the requested operation because the local player is already authenticating.
- [static var cancelled: GKError.Code](gkerror/cancelled.md)
  The system canceled the requested operation or the user disabled it.
- [static var challengeInvalid: GKError.Code](gkerror/challengeinvalid.md)
  The challenge request failed due to invalid challenge data.
- [static var communicationsFailure: GKError.Code](gkerror/communicationsfailure.md)
  The system can’t complete the requested operation due to an error communicating with the server.
- [static var gameSessionRequestInvalid: GKError.Code](gkerror/gamesessionrequestinvalid.md)
  The properties of the game session request are impossible to fulfill.
- [static var gameUnrecognized: GKError.Code](gkerror/gameunrecognized.md)
  The system can’t complete the requested operation because Game Center doesn’t recognize the app.
- [static var invalidCredentials: GKError.Code](gkerror/invalidcredentials.md)
  The system can’t complete the requested operation because the user name or password are incorrect.
- [static var invalidParameter: GKError.Code](gkerror/invalidparameter.md)
  The system can’t complete the requested operation because one or more parameters are invalid.
- [static var invalidPlayer: GKError.Code](gkerror/invalidplayer.md)
  The system can’t complete the requested operation because the player is invalid.
- [static var invitationsDisabled: GKError.Code](gkerror/invitationsdisabled.md)
  The system can’t complete the requested operation because the receiving player has disabled invitations.
- [static var matchNotConnected: GKError.Code](gkerror/matchnotconnected.md)
  The system can’t complete the requested operation because the match isn’t connected to other players.
- [static var matchRequestInvalid: GKError.Code](gkerror/matchrequestinvalid.md)
  The system can’t complete the requested operation because the match request is invalid.
- [static var notAuthenticated: GKError.Code](gkerror/notauthenticated.md)
  The system can’t complete the requested operation because the system hasn’t initialized the local player.
- [static var notSupported: GKError.Code](gkerror/notsupported.md)
  The app doesn’t have Game Center enabled.
- [static var parentalControlsBlocked: GKError.Code](gkerror/parentalcontrolsblocked.md)
  The system can’t complete the requested operation because the user disabled this feature in Restrictions.
- [static var playerPhotoFailure: GKError.Code](gkerror/playerphotofailure.md)
  The system can’t complete the requested operation to retrieve a player’s photo.
- [static var playerStatusExceedsMaximumLength: GKError.Code](gkerror/playerstatusexceedsmaximumlength.md)
  The player’s status exceeds the maximum length.
- [static var playerStatusInvalid: GKError.Code](gkerror/playerstatusinvalid.md)
  The player’s status is invalid.
- [static var scoreNotSet: GKError.Code](gkerror/scorenotset.md)
  The system can’t complete the requested operation because the system hasn’t set the score.
- [static var turnBasedInvalidParticipant: GKError.Code](gkerror/turnbasedinvalidparticipant.md)
  The system can’t complete the requested operation because the specified participant is invalid.
- [static var turnBasedInvalidState: GKError.Code](gkerror/turnbasedinvalidstate.md)
  The system can’t complete the requested operation because the session is in an invalid state.
- [static var turnBasedInvalidTurn: GKError.Code](gkerror/turnbasedinvalidturn.md)
  The system can’t complete the requested operation because the participant doesn’t have the required turn state.
- [static var turnBasedMatchDataTooLarge: GKError.Code](gkerror/turnbasedmatchdatatoolarge.md)
  The system can’t complete the requested operation because the match data is too large.
- [static var turnBasedTooManySessions: GKError.Code](gkerror/turnbasedtoomanysessions.md)
  The system can’t complete the requested operation because it exceeds the maximum number of sessions.
- [static var ubiquityContainerUnavailable: GKError.Code](gkerror/ubiquitycontainerunavailable.md)
  The system can’t complete the requested operation because the user hasn’t signed in to iCloud or hasn’t enabled iCloud Drive.
- [static var underage: GKError.Code](gkerror/underage.md)
  The system can’t complete the requested operation because this feature isn’t available to underage players.
- [static var unexpectedConnection: GKError.Code](gkerror/unexpectedconnection.md)
  An unexpected player has connected to a match.
- [static var unknown: GKError.Code](gkerror/unknown.md)
  The system can’t complete the requested operation due to an unknown error.
- [static var userDenied: GKError.Code](gkerror/userdenied.md)
  The system can’t complete the requested operation because the user denied it.
- [static var restrictedToAutomatch: GKError.Code](gkerror/restrictedtoautomatch.md)
  The system can’t complete the requested operation because the player is using automatch.
- [static var apiNotAvailable: GKError.Code](gkerror/apinotavailable.md)
  The system can’t complete the requested operation because the API isn’t available.
- [static var notAuthorized: GKError.Code](gkerror/notauthorized.md)
  The system can’t complete the requested operation because the system hasn’t authorized the player.
- [static var connectionTimeout: GKError.Code](gkerror/connectiontimeout.md)
  The system can’t complete the requested operation because the connection timed out.
- [static var apiObsolete: GKError.Code](gkerror/apiobsolete.md)
  The system can’t complete the requested operation because Apple deprecated the API.
- [static var iCloudUnavailable: GKError.Code](gkerror/icloudunavailable.md)
  The system can’t complete the requested operation because it can’t access the player’s iCloud account.
- [static var lockdownMode: GKError.Code](gkerror/lockdownmode.md)
  The system can’t complete the requested operation because the player enabled Lockdown Mode on the device.
- [static var appUnlisted: GKError.Code](gkerror/appunlisted.md)
  The system can’t complete the requested operation because the game isn’t available on the App Store.
- [static var friendListDescriptionMissing: GKError.Code](gkerror/friendlistdescriptionmissing.md)
  The system denies access to the local player’s friends list because the game didn’t provide a reason.
- [static var friendListRestricted: GKError.Code](gkerror/friendlistrestricted.md)
  The system restricts access to the local player’s friends list.
- [static var friendListDenied: GKError.Code](gkerror/friendlistdenied.md)
  The local player denies access to their friends list.
- [static var friendRequestNotAvailable: GKError.Code](gkerror/friendrequestnotavailable.md)
  The player can’t send a friend request at this time from this device.
### Error Domain
- [static var errorDomain: String](gkerror/errordomain.md)
### Type Properties
- [static var debugMode: GKError.Code](gkerror/debugmode.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [GKError.Code](gkerror/code.md)
  Error codes for the GameKit error domain.
- [let GKErrorDomain: String](gkerrordomain.md)
  The error domain for general game errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror)*