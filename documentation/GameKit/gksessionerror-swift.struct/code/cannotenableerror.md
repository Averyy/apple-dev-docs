# GKSessionError.Code.cannotEnableError

**Framework**: GameKit  
**Kind**: case

Bluetooth is not currently available.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case cannotEnableError
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessionerror-swift.struct/code/cannotenableerror)*