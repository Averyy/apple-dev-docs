# init(remoteWithTCPPort:host:)

**Framework**: Foundation  
**Kind**: init

Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init?(remoteWithTCPPort port: UInt16, host hostName: String?)
```

#### Return Value

A TCP/IP socket port of type `SOCK_STREAM` that can connect to the remote host `hostName` on port `port`.

#### Discussion

A connection is not opened to the remote host until data is sent.

## Parameters

- `port`: The port to connect to.
- `hostName`: The host name to connect to.   may be either a host name or an IPv4-style address.

## See Also

- [convenience init()](socketport/init.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [convenience init?(tcpPort: UInt16)](socketport/init(tcpport:).md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(protocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a local socket with the provided arguments.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, socket: SocketNativeHandle)](socketport/init(protocolfamily:sockettype:protocol:socket:).md)
  Initializes the receiver with a previously created local socket.
- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(remotewithprotocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a remote socket with the provided arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/init(remotewithtcpport:host:))*