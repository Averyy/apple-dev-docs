# turnBasedTooManySessions

**Framework**: GameKit  
**Kind**: property

The system can’t complete the requested operation because it exceeds the maximum number of sessions.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var turnBasedTooManySessions: GKError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/turnbasedtoomanysessions)*