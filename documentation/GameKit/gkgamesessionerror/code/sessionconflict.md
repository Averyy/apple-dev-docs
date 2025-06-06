# GKGameSessionError.Code.sessionConflict

**Framework**: GameKit  
**Kind**: case

The requested operation could not be completed because the session has been updated on the server, causing a conflict.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case sessionConflict
```

## See Also

- [GKGameSessionError.Code.unknown](gkgamesessionerror/code/unknown.md)
  The requested operation could not be completed due to an unknown error.
- [GKGameSessionError.Code.notAuthenticated](gkgamesessionerror/code/notauthenticated.md)
  The requested operation could not be completed because you are not signed in to iCloud.
- [GKGameSessionError.Code.sessionNotShared](gkgamesessionerror/code/sessionnotshared.md)
  The requested operation could not be completed because this session has not been shared with other players.
- [GKGameSessionError.Code.connectionCancelledByUser](gkgamesessionerror/code/connectioncancelledbyuser.md)
  The requested operation could not be completed because the connection to the session was cancelled.
- [GKGameSessionError.Code.connectionFailed](gkgamesessionerror/code/connectionfailed.md)
  The requested operation could not be completed because the session could not find other players to connect to.
- [GKGameSessionError.Code.sessionHasMaxConnectedPlayers](gkgamesessionerror/code/sessionhasmaxconnectedplayers.md)
  The requested operation could not be completed because the session has reached the maximum number of connected players.
- [GKGameSessionError.Code.sendDataNotConnected](gkgamesessionerror/code/senddatanotconnected.md)
  The requested operation could not be completed because you are not connected to the session.
- [GKGameSessionError.Code.sendDataNoRecipients](gkgamesessionerror/code/senddatanorecipients.md)
  The requested operation could not be completed because there are no recipients connected to session.
- [GKGameSessionError.Code.sendDataNotReachable](gkgamesessionerror/code/senddatanotreachable.md)
  The requested operation could not be completed because one or more players is not reachable.
- [GKGameSessionError.Code.sendRateLimitReached](gkgamesessionerror/code/sendratelimitreached.md)
  The requested operation could not be completed because you have reached the limits for save data request.
- [GKGameSessionError.Code.badContainer](gkgamesessionerror/code/badcontainer.md)
  The requested operation could not be completed because the iCloud container is invalid.
- [GKGameSessionError.Code.cloudQuotaExceeded](gkgamesessionerror/code/cloudquotaexceeded.md)
  The requested operation could not be completed because the user’s iCloud quota would be exceeded.
- [GKGameSessionError.Code.networkFailure](gkgamesessionerror/code/networkfailure.md)
  The requested operation could not be completed due to an error communicating with the server.
- [GKGameSessionError.Code.cloudDriveDisabled](gkgamesessionerror/code/clouddrivedisabled.md)
  The requested operation could not be completed because iCloud Drive has been disabled for the application.
- [GKGameSessionError.Code.invalidSession](gkgamesessionerror/code/invalidsession.md)
  The requested operation could not be completed because the Game Session does not exist or the player is not part of the game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/sessionconflict)*