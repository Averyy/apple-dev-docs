# GKSessionError.Code

**Framework**: GameKit  
**Kind**: enum

Error codes for the session error domain.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum Code
```

## Topics

### Constants
- [GKSessionError.Code.invalidParameterError](gksessionerror-swift.struct/code/invalidparametererror.md)
  A parameter had an unexpected value.
- [GKSessionError.Code.peerNotFoundError](gksessionerror-swift.struct/code/peernotfounderror.md)
  A peer with the specified `peerID` string could not be found.
- [GKSessionError.Code.declinedError](gksessionerror-swift.struct/code/declinederror.md)
  The peer your application tried to connect to refused the connection.
- [GKSessionError.Code.timedOutError](gksessionerror-swift.struct/code/timedouterror.md)
  The operation could not be completed in the specified timeout period.
- [GKSessionError.Code.cancelledError](gksessionerror-swift.struct/code/cancellederror.md)
  A peer that invited the session to connect to them canceled the connection request.
- [GKSessionError.Code.connectionFailedError](gksessionerror-swift.struct/code/connectionfailederror.md)
  The attempt to establish a connection with another peer failed.
- [GKSessionError.Code.connectionClosedError](gksessionerror-swift.struct/code/connectionclosederror.md)
  The connection to another peer closed unexpectedly.
- [GKSessionError.Code.dataTooBigError](gksessionerror-swift.struct/code/datatoobigerror.md)
  The data your application attempted to send was too large for the session to transmit in a single call.
- [GKSessionError.Code.notConnectedError](gksessionerror-swift.struct/code/notconnectederror.md)
  Reserved for future use.
- [GKSessionError.Code.cannotEnableError](gksessionerror-swift.struct/code/cannotenableerror.md)
  Bluetooth is not currently available.
- [GKSessionError.Code.inProgressError](gksessionerror-swift.struct/code/inprogresserror.md)
  The peer your application attempted to connect to has already requested a connection to your session.
- [GKSessionError.Code.connectivityError](gksessionerror-swift.struct/code/connectivityerror.md)
  An error occurred in the [`GKSession`](gksession.md) object’s connection code.
- [GKSessionError.Code.transportError](gksessionerror-swift.struct/code/transporterror.md)
  An error occurred in the [`GKSession`](gksession.md) object’s transport code.
- [GKSessionError.Code.internalError](gksessionerror-swift.struct/code/internalerror.md)
  A serious error occurred inside [`GKSession`](gksession.md).
- [GKSessionError.Code.unknownError](gksessionerror-swift.struct/code/unknownerror.md)
  Reserved for when the error does not fit in another category above.
- [GKSessionError.Code.systemError](gksessionerror-swift.struct/code/systemerror.md)
  An error occurred outside of the [`GKSession`](gksession.md) object’s control, such as memory allocation.
### Initializers
- [init?(rawValue: Int32)](gksessionerror-swift.struct/code/init(rawvalue:).md)

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
- [enum GKSendDataMode](gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [struct GKSessionError](gksessionerror-swift.struct.md)
- [enum GKSessionMode](gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [GKVoiceChatServiceError.Code](gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessionerror-swift.struct/code)*