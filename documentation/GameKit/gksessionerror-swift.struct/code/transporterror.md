# GKSessionError.Code.transportError

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

An error occurred in the [`GKSession`](../../gksession.md) object’s transport code.

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
case transportError
```

```c
GKSessionTransportError
```

## See Also

### Constants
- [GKSessionError.Code.invalidParameterError](./invalidparametererror.md)
  A parameter had an unexpected value.
- [GKSessionError.Code.peerNotFoundError](./peernotfounderror.md)
  A peer with the specified `peerID` string could not be found.
- [GKSessionError.Code.declinedError](./declinederror.md)
  The peer your application tried to connect to refused the connection.
- [GKSessionError.Code.timedOutError](./timedouterror.md)
  The operation could not be completed in the specified timeout period.
- [GKSessionError.Code.cancelledError](./cancellederror.md)
  A peer that invited the session to connect to them canceled the connection request.
- [GKSessionError.Code.connectionFailedError](./connectionfailederror.md)
  The attempt to establish a connection with another peer failed.
- [GKSessionError.Code.connectionClosedError](./connectionclosederror.md)
  The connection to another peer closed unexpectedly.
- [GKSessionError.Code.dataTooBigError](./datatoobigerror.md)
  The data your application attempted to send was too large for the session to transmit in a single call.
- [GKSessionError.Code.notConnectedError](./notconnectederror.md)
  Reserved for future use.
- [GKSessionError.Code.cannotEnableError](./cannotenableerror.md)
  Bluetooth is not currently available.
- [GKSessionError.Code.inProgressError](./inprogresserror.md)
  The peer your application attempted to connect to has already requested a connection to your session.
- [GKSessionError.Code.connectivityError](./connectivityerror.md)
  An error occurred in the [`GKSession`](../../gksession.md) object’s connection code.
- [GKSessionError.Code.internalError](./internalerror.md)
  A serious error occurred inside [`GKSession`](../../gksession.md).
- [GKSessionError.Code.unknownError](./unknownerror.md)
  Reserved for when the error does not fit in another category above.
- [GKSessionError.Code.systemError](./systemerror.md)
  An error occurred outside of the [`GKSession`](../../gksession.md) object’s control, such as memory allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessionerror-swift.struct/code/transporterror)*