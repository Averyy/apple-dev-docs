# badContainer

**Framework**: GameKit  
**Kind**: property  
**Role**: Type Property

The requested operation could not be completed because the iCloud container is invalid.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: GKGameSession is deprecated, use real-time and turn-based matchmaking APIs instead.

## Declaration

```swift
static var badContainer: GKGameSessionError.Code { get }
```

## See Also

### Error Codes
- [static var cloudDriveDisabled: GKGameSessionError.Code](./clouddrivedisabled.md)
  The requested operation could not be completed because iCloud Drive has been disabled for the application.
- [static var cloudQuotaExceeded: GKGameSessionError.Code](./cloudquotaexceeded.md)
  The requested operation could not be completed because the user’s iCloud quota would be exceeded.
- [static var connectionCancelledByUser: GKGameSessionError.Code](./connectioncancelledbyuser.md)
  The requested operation could not be completed because the connection to the session was cancelled.
- [static var connectionFailed: GKGameSessionError.Code](./connectionfailed.md)
  The requested operation could not be completed because the session could not find other players to connect to.
- [static var invalidSession: GKGameSessionError.Code](./invalidsession.md)
  The requested operation could not be completed because the Game Session does not exist or the player is not part of the game session.
- [static var networkFailure: GKGameSessionError.Code](./networkfailure.md)
  The requested operation could not be completed due to an error communicating with the server.
- [static var notAuthenticated: GKGameSessionError.Code](./notauthenticated.md)
  The requested operation could not be completed because you are not signed in to iCloud.
- [static var sendDataNoRecipients: GKGameSessionError.Code](./senddatanorecipients.md)
  The requested operation could not be completed because there are no recipients connected to session.
- [static var sendDataNotConnected: GKGameSessionError.Code](./senddatanotconnected.md)
  The requested operation could not be completed because you are not connected to the session.
- [static var sendDataNotReachable: GKGameSessionError.Code](./senddatanotreachable.md)
  The requested operation could not be completed because one or more players is not reachable.
- [static var sendRateLimitReached: GKGameSessionError.Code](./sendratelimitreached.md)
  The requested operation could not be completed because you have reached the limits for save data request.
- [static var sessionConflict: GKGameSessionError.Code](./sessionconflict.md)
  The requested operation could not be completed because the session has been updated on the server, causing a conflict.
- [static var sessionHasMaxConnectedPlayers: GKGameSessionError.Code](./sessionhasmaxconnectedplayers.md)
  The requested operation could not be completed because the session has reached the maximum number of connected players.
- [static var sessionNotShared: GKGameSessionError.Code](./sessionnotshared.md)
  The requested operation could not be completed because this session has not been shared with other players.
- [static var unknown: GKGameSessionError.Code](./unknown.md)
  The requested operation could not be completed due to an unknown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/badcontainer)*