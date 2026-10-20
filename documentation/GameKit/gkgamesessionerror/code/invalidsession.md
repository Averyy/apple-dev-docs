# GKGameSessionError.Code.invalidSession

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

The requested operation could not be completed because the Game Session does not exist or the player is not part of the game session.

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
case invalidSession
```

```c
GKGameSessionErrorInvalidSession
```

## See Also

### Enumeration Cases
- [GKGameSessionError.Code.unknown](./unknown.md)
  The requested operation could not be completed due to an unknown error.
- [GKGameSessionError.Code.notAuthenticated](./notauthenticated.md)
  The requested operation could not be completed because you are not signed in to iCloud.
- [GKGameSessionError.Code.sessionConflict](./sessionconflict.md)
  The requested operation could not be completed because the session has been updated on the server, causing a conflict.
- [GKGameSessionError.Code.sessionNotShared](./sessionnotshared.md)
  The requested operation could not be completed because this session has not been shared with other players.
- [GKGameSessionError.Code.connectionCancelledByUser](./connectioncancelledbyuser.md)
  The requested operation could not be completed because the connection to the session was cancelled.
- [GKGameSessionError.Code.connectionFailed](./connectionfailed.md)
  The requested operation could not be completed because the session could not find other players to connect to.
- [GKGameSessionError.Code.sessionHasMaxConnectedPlayers](./sessionhasmaxconnectedplayers.md)
  The requested operation could not be completed because the session has reached the maximum number of connected players.
- [GKGameSessionError.Code.sendDataNotConnected](./senddatanotconnected.md)
  The requested operation could not be completed because you are not connected to the session.
- [GKGameSessionError.Code.sendDataNoRecipients](./senddatanorecipients.md)
  The requested operation could not be completed because there are no recipients connected to session.
- [GKGameSessionError.Code.sendDataNotReachable](./senddatanotreachable.md)
  The requested operation could not be completed because one or more players is not reachable.
- [GKGameSessionError.Code.sendRateLimitReached](./sendratelimitreached.md)
  The requested operation could not be completed because you have reached the limits for save data request.
- [GKGameSessionError.Code.badContainer](./badcontainer.md)
  The requested operation could not be completed because the iCloud container is invalid.
- [GKGameSessionError.Code.cloudQuotaExceeded](./cloudquotaexceeded.md)
  The requested operation could not be completed because the user’s iCloud quota would be exceeded.
- [GKGameSessionError.Code.networkFailure](./networkfailure.md)
  The requested operation could not be completed due to an error communicating with the server.
- [GKGameSessionError.Code.cloudDriveDisabled](./clouddrivedisabled.md)
  The requested operation could not be completed because iCloud Drive has been disabled for the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/invalidsession)*