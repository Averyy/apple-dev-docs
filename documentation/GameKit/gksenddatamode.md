# GKSendDataMode

**Framework**: GameKit  
**Kind**: enum

The mechanism used to transmit data to other peers.

**Availability**:
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKSendDataMode
```

## Topics

### Constants
- [GKSendDataMode.reliable](gksenddatamode/reliable.md)
  The data is sent continuously until it is successfully received by the intended recipients or the connection times out.
- [GKSendDataMode.unreliable](gksenddatamode/unreliable.md)
  The data is sent once and is not sent again if a transmission error occurred.
### Initializers
- [init?(rawValue: Int32)](gksenddatamode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [GKGameSessionError.Code](gkgamesessionerror/code.md)
  Error codes for the game session domain.
- [enum GKPeerConnectionState](gkpeerconnectionstate.md)
  The state of a peer known to the session.
- [enum GKPeerPickerConnectionType](gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [GKSessionError.Code](gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](gksessionerror-swift.struct.md)
- [enum GKSessionMode](gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [GKVoiceChatServiceError.Code](gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksenddatamode)*