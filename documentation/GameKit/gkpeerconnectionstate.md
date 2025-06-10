# GKPeerConnectionState

**Framework**: GameKit  
**Kind**: enum

The state of a peer known to the session.

**Availability**:
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKPeerConnectionState
```

#### Overview

States are not mutually exclusive. For example, a peer can be available for other peers to discover while it is attempting to connect to another peer.

## Topics

### Constants
- [GKPeerConnectionState.stateAvailable](gkpeerconnectionstate/stateavailable.md)
  A peer not connected to the session, but one that the session can connect to.
- [GKPeerConnectionState.stateUnavailable](gkpeerconnectionstate/stateunavailable.md)
  A peer that is no longer interested in receiving connections.
- [GKPeerConnectionState.stateConnected](gkpeerconnectionstate/stateconnected.md)
  A peer connected to the session.
- [GKPeerConnectionState.stateDisconnected](gkpeerconnectionstate/statedisconnected.md)
  A peer that disconnected from the session.
- [GKPeerConnectionState.stateConnecting](gkpeerconnectionstate/stateconnecting.md)
  A peer attempting to connect to the session.
### Enumeration Cases
- [GKPeerConnectionState.stateConnectedRelay](gkpeerconnectionstate/stateconnectedrelay.md)
### Initializers
- [init?(rawValue: Int32)](gkpeerconnectionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [GKGameSessionError.Code](gkgamesessionerror/code.md)
  Error codes for the game session domain.
- [enum GKPeerPickerConnectionType](gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [enum GKSendDataMode](gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [GKSessionError.Code](gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](gksessionerror-swift.struct.md)
- [enum GKSessionMode](gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [GKVoiceChatServiceError.Code](gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate)*