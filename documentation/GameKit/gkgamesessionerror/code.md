# GKGameSessionError.Code

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

Error codes for the game session domain.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the real-time and turn-based matchmaking APIs instead.

## Declaration

```swift
enum Code
```

```c
enum GKGameSessionErrorCode : NSInteger;
```

## Topics

### Enumeration Cases
- [GKGameSessionError.Code.unknown](./code/unknown.md)
  The requested operation could not be completed due to an unknown error.
- [GKGameSessionError.Code.notAuthenticated](./code/notauthenticated.md)
  The requested operation could not be completed because you are not signed in to iCloud.
- [GKGameSessionError.Code.sessionConflict](./code/sessionconflict.md)
  The requested operation could not be completed because the session has been updated on the server, causing a conflict.
- [GKGameSessionError.Code.sessionNotShared](./code/sessionnotshared.md)
  The requested operation could not be completed because this session has not been shared with other players.
- [GKGameSessionError.Code.connectionCancelledByUser](./code/connectioncancelledbyuser.md)
  The requested operation could not be completed because the connection to the session was cancelled.
- [GKGameSessionError.Code.connectionFailed](./code/connectionfailed.md)
  The requested operation could not be completed because the session could not find other players to connect to.
- [GKGameSessionError.Code.sessionHasMaxConnectedPlayers](./code/sessionhasmaxconnectedplayers.md)
  The requested operation could not be completed because the session has reached the maximum number of connected players.
- [GKGameSessionError.Code.sendDataNotConnected](./code/senddatanotconnected.md)
  The requested operation could not be completed because you are not connected to the session.
- [GKGameSessionError.Code.sendDataNoRecipients](./code/senddatanorecipients.md)
  The requested operation could not be completed because there are no recipients connected to session.
- [GKGameSessionError.Code.sendDataNotReachable](./code/senddatanotreachable.md)
  The requested operation could not be completed because one or more players is not reachable.
- [GKGameSessionError.Code.sendRateLimitReached](./code/sendratelimitreached.md)
  The requested operation could not be completed because you have reached the limits for save data request.
- [GKGameSessionError.Code.badContainer](./code/badcontainer.md)
  The requested operation could not be completed because the iCloud container is invalid.
- [GKGameSessionError.Code.cloudQuotaExceeded](./code/cloudquotaexceeded.md)
  The requested operation could not be completed because the user’s iCloud quota would be exceeded.
- [GKGameSessionError.Code.networkFailure](./code/networkfailure.md)
  The requested operation could not be completed due to an error communicating with the server.
- [GKGameSessionError.Code.cloudDriveDisabled](./code/clouddrivedisabled.md)
  The requested operation could not be completed because iCloud Drive has been disabled for the application.
- [GKGameSessionError.Code.invalidSession](./code/invalidsession.md)
  The requested operation could not be completed because the Game Session does not exist or the player is not part of the game session.
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

### Deprecated enumerations
- [enum GKPeerConnectionState](../gkpeerconnectionstate.md)
  The state of a peer known to the session.
- [enum GKPeerPickerConnectionType](../gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [enum GKSendDataMode](../gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [GKSessionError.Code](../gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](../gksessionerror-swift.struct.md)
- [enum GKSessionMode](../gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [GKVoiceChatServiceError.Code](../gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](../gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code)*