# init(remoteWithProtocolFamily:socketType:protocol:address:)

**Framework**: Foundation  
**Kind**: init

Initializes the receiver as a remote socket with the provided arguments.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init(remoteWithProtocolFamily family: Int32, socketType type: Int32, protocol: Int32, address: Data)
```

#### Discussion

A connection is not opened to the remote address until data is sent.

## Parameters

- `family`: The protocol family for the socket port. Possible values are defined in  , such as  ,  , and  .
- `type`: The type of socket.
- `protocol`: The specific protocol to use from the protocol family.
- `address`: The family-specific socket address for the receiver copied into an   object.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/init(remotewithprotocolfamily:sockettype:protocol:address:))*