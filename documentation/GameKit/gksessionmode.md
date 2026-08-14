# GKSessionMode

**Framework**: GameKit  
**Kind**: enum

Modes that determine how a session interacts with other peers.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 3.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKSessionMode
```

## Topics

### Constants
- [GKSessionMode.server](gksessionmode/server.md)
  A server advertises itself to local devices using its [`sessionID`](gksession/sessionid.md) property.
- [GKSessionMode.client](gksessionmode/client.md)
  A client searches for servers advertising the same [`sessionID`](gksession/sessionid.md) property.
- [GKSessionMode.peer](gksessionmode/peer.md)
  A peer advertises like a server and searches like a client.
### Initializers
- [init?(rawValue: Int32)](gksessionmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [GKGameSessionError.Code](gkgamesessionerror/code.md)
  Error codes for the game session domain.
- [enum GKPeerConnectionState](gkpeerconnectionstate.md)
  The state of a peer known to the session.
- [enum GKPeerPickerConnectionType](gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [enum GKSendDataMode](gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [GKSessionError.Code](gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](gksessionerror-swift.struct.md)
- [GKVoiceChatServiceError.Code](gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessionmode)*