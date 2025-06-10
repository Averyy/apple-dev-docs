# SocketPort

**Framework**: Foundation  
**Kind**: class

A port that represents a BSD socket.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class SocketPort
```

#### Overview

A [`SocketPort`](socketport.md) object can be used as an endpoint for distributed object connections. Companion classes, [`NSMachPort`](nsmachport.md) and [`MessagePort`](messageport.md), allow for local (on the same machine) communication only. The [`SocketPort`](socketport.md) class allows for both local and remote communication, but may be more expensive than the others for the local case.

> **Note**:  The [`SocketPort`](socketport.md) class conforms to the [`NSCoding`](nscoding.md) protocol, but only supports coding by an [`NSPortCoder`](nsportcoder.md). [`Port`](port.md) and its other subclasses do not support archiving.

## Topics

### Creating Instances
- [convenience init()](socketport/init.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [convenience init?(tcpPort: UInt16)](socketport/init(tcpport:).md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(protocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a local socket with the provided arguments.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, socket: SocketNativeHandle)](socketport/init(protocolfamily:sockettype:protocol:socket:).md)
  Initializes the receiver with a previously created local socket.
- [convenience init?(remoteWithTCPPort: UInt16, host: String?)](socketport/init(remotewithtcpport:host:).md)
  Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(remotewithprotocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a remote socket with the provided arguments.
### Getting Information
- [var address: Data](socketport/address.md)
  The receiver’s socket address structure stored inside an [`NSData`](nsdata.md) object.
- [var `protocol`: Int32](socketport/protocol.md)
  The protocol that the receiver uses for communication.
- [var protocolFamily: Int32](socketport/protocolfamily.md)
  The protocol family that the receiver uses for communication.
- [var socket: SocketNativeHandle](socketport/socket.md)
  The receiver’s native socket identifier on the platform.
- [var socketType: Int32](socketport/sockettype.md)
  The receiver’s socket type.

## Relationships

### Inherits From
- [Port](port.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class Host](host.md)
  A representation of an individual host on the network.
- [class Port](port.md)
  An abstract class that represents a communication channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport)*