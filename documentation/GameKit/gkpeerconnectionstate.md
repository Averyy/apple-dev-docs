# GKPeerConnectionState

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The state of a peer known to the session.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: No longer supported

## Declaration

```swift
enum GKPeerConnectionState
```

```c
enum GKPeerConnectionState : int;
```

#### Overview

States are not mutually exclusive. For example, a peer can be available for other peers to discover while it is attempting to connect to another peer.

## Topics

### Constants
- [GKPeerConnectionState.stateAvailable](./gkpeerconnectionstate/stateavailable.md)
  A peer not connected to the session, but one that the session can connect to.
- [GKPeerConnectionState.stateUnavailable](./gkpeerconnectionstate/stateunavailable.md)
  A peer that is no longer interested in receiving connections.
- [GKPeerConnectionState.stateConnected](./gkpeerconnectionstate/stateconnected.md)
  A peer connected to the session.
- [GKPeerConnectionState.stateDisconnected](./gkpeerconnectionstate/statedisconnected.md)
  A peer that disconnected from the session.
- [GKPeerConnectionState.stateConnecting](./gkpeerconnectionstate/stateconnecting.md)
  A peer attempting to connect to the session.
### Enumeration Cases
- [GKPeerConnectionState.stateConnectedRelay](./gkpeerconnectionstate/stateconnectedrelay.md)
### Initializers
- [init?(rawValue: Int32)](./gkpeerconnectionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated enumerations
- [GKGameSessionError.Code](./gkgamesessionerror/code.md)
  Error codes for the game session domain.
- [enum GKPeerPickerConnectionType](./gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [enum GKSendDataMode](./gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [GKSessionError.Code](./gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](./gksessionerror-swift.struct.md)
- [enum GKSessionMode](./gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [GKVoiceChatServiceError.Code](./gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](./gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate)*