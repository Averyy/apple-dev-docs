# GKSessionError.Code

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

Error codes for the session error domain.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: No longer supported

## Declaration

```swift
enum Code
```

```c
enum GKSessionError : int;
```

## Topics

### Constants
- [GKSessionError.Code.invalidParameterError](./code/invalidparametererror.md)
  A parameter had an unexpected value.
- [GKSessionError.Code.peerNotFoundError](./code/peernotfounderror.md)
  A peer with the specified `peerID` string could not be found.
- [GKSessionError.Code.declinedError](./code/declinederror.md)
  The peer your application tried to connect to refused the connection.
- [GKSessionError.Code.timedOutError](./code/timedouterror.md)
  The operation could not be completed in the specified timeout period.
- [GKSessionError.Code.cancelledError](./code/cancellederror.md)
  A peer that invited the session to connect to them canceled the connection request.
- [GKSessionError.Code.connectionFailedError](./code/connectionfailederror.md)
  The attempt to establish a connection with another peer failed.
- [GKSessionError.Code.connectionClosedError](./code/connectionclosederror.md)
  The connection to another peer closed unexpectedly.
- [GKSessionError.Code.dataTooBigError](./code/datatoobigerror.md)
  The data your application attempted to send was too large for the session to transmit in a single call.
- [GKSessionError.Code.notConnectedError](./code/notconnectederror.md)
  Reserved for future use.
- [GKSessionError.Code.cannotEnableError](./code/cannotenableerror.md)
  Bluetooth is not currently available.
- [GKSessionError.Code.inProgressError](./code/inprogresserror.md)
  The peer your application attempted to connect to has already requested a connection to your session.
- [GKSessionError.Code.connectivityError](./code/connectivityerror.md)
  An error occurred in the [`GKSession`](../gksession.md) object’s connection code.
- [GKSessionError.Code.transportError](./code/transporterror.md)
  An error occurred in the [`GKSession`](../gksession.md) object’s transport code.
- [GKSessionError.Code.internalError](./code/internalerror.md)
  A serious error occurred inside [`GKSession`](../gksession.md).
- [GKSessionError.Code.unknownError](./code/unknownerror.md)
  Reserved for when the error does not fit in another category above.
- [GKSessionError.Code.systemError](./code/systemerror.md)
  An error occurred outside of the [`GKSession`](../gksession.md) object’s control, such as memory allocation.
### Initializers
- [init?(rawValue: Int32)](./code/init%28rawvalue%29.md)

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
- [GKGameSessionError.Code](../gkgamesessionerror/code.md)
  Error codes for the game session domain.
- [enum GKPeerConnectionState](../gkpeerconnectionstate.md)
  The state of a peer known to the session.
- [enum GKPeerPickerConnectionType](../gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [enum GKSendDataMode](../gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [struct GKSessionError](../gksessionerror-swift.struct.md)
- [enum GKSessionMode](../gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [GKVoiceChatServiceError.Code](../gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](../gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessionerror-swift.struct/code)*