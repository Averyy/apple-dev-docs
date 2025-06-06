# init(protocolFamily:socketType:protocol:socket:)

**Framework**: Foundation  
**Kind**: init

Initializes the receiver with a previously created local socket.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(protocolFamily family: Int32, socketType type: Int32, protocol: Int32, socket sock: SocketNativeHandle)
```

#### Return Value

A local socket port initialized with the provided socket.

## Parameters

- `family`: The protocol family for the provided socket. Possible values are defined in  , such as  ,  , and  .
- `type`: The type of the provided socket.
- `protocol`: The specific protocol the provided socket uses.
- `sock`: The previously created socket.

## See Also

- [convenience init()](socketport/init.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [convenience init?(tcpPort: UInt16)](socketport/init(tcpport:).md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(protocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a local socket with the provided arguments.
- [convenience init?(remoteWithTCPPort: UInt16, host: String?)](socketport/init(remotewithtcpport:host:).md)
  Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(remotewithprotocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a remote socket with the provided arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/init(protocolfamily:sockettype:protocol:socket:))*