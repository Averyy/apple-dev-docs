# unknown

**Framework**: GameKit  
**Kind**: property

The requested operation could not be completed due to an unknown error.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var unknown: GKGameSessionError.Code { get }
```

## See Also

- [static var badContainer: GKGameSessionError.Code](gkgamesessionerror/badcontainer.md)
  The requested operation could not be completed because the iCloud container is invalid.
- [static var cloudDriveDisabled: GKGameSessionError.Code](gkgamesessionerror/clouddrivedisabled.md)
  The requested operation could not be completed because iCloud Drive has been disabled for the application.
- [static var cloudQuotaExceeded: GKGameSessionError.Code](gkgamesessionerror/cloudquotaexceeded.md)
  The requested operation could not be completed because the user’s iCloud quota would be exceeded.
- [static var connectionCancelledByUser: GKGameSessionError.Code](gkgamesessionerror/connectioncancelledbyuser.md)
  The requested operation could not be completed because the connection to the session was cancelled.
- [static var connectionFailed: GKGameSessionError.Code](gkgamesessionerror/connectionfailed.md)
  The requested operation could not be completed because the session could not find other players to connect to.
- [static var invalidSession: GKGameSessionError.Code](gkgamesessionerror/invalidsession.md)
  The requested operation could not be completed because the Game Session does not exist or the player is not part of the game session.
- [static var networkFailure: GKGameSessionError.Code](gkgamesessionerror/networkfailure.md)
  The requested operation could not be completed due to an error communicating with the server.
- [static var notAuthenticated: GKGameSessionError.Code](gkgamesessionerror/notauthenticated.md)
  The requested operation could not be completed because you are not signed in to iCloud.
- [static var sendDataNoRecipients: GKGameSessionError.Code](gkgamesessionerror/senddatanorecipients.md)
  The requested operation could not be completed because there are no recipients connected to session.
- [static var sendDataNotConnected: GKGameSessionError.Code](gkgamesessionerror/senddatanotconnected.md)
  The requested operation could not be completed because you are not connected to the session.
- [static var sendDataNotReachable: GKGameSessionError.Code](gkgamesessionerror/senddatanotreachable.md)
  The requested operation could not be completed because one or more players is not reachable.
- [static var sendRateLimitReached: GKGameSessionError.Code](gkgamesessionerror/sendratelimitreached.md)
  The requested operation could not be completed because you have reached the limits for save data request.
- [static var sessionConflict: GKGameSessionError.Code](gkgamesessionerror/sessionconflict.md)
  The requested operation could not be completed because the session has been updated on the server, causing a conflict.
- [static var sessionHasMaxConnectedPlayers: GKGameSessionError.Code](gkgamesessionerror/sessionhasmaxconnectedplayers.md)
  The requested operation could not be completed because the session has reached the maximum number of connected players.
- [static var sessionNotShared: GKGameSessionError.Code](gkgamesessionerror/sessionnotshared.md)
  The requested operation could not be completed because this session has not been shared with other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/unknown)*