# init(tcpPort:)

**Framework**: Foundation  
**Kind**: init

Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init?(tcpPort port: UInt16)
```

#### Return Value

An initialized local TCP/IP socket of type `SOCK_STREAM`, listening on port `port`.

#### Discussion

This method creates an IPv4 port, not an IPv6 port.

## Parameters

- `port`: The port number for the newly created socket port to listen on. If   is 0, the system will assign a port number.

## See Also

- [convenience init()](socketport/init.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(protocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a local socket with the provided arguments.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, socket: SocketNativeHandle)](socketport/init(protocolfamily:sockettype:protocol:socket:).md)
  Initializes the receiver with a previously created local socket.
- [convenience init?(remoteWithTCPPort: UInt16, host: String?)](socketport/init(remotewithtcpport:host:).md)
  Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(remotewithprotocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a remote socket with the provided arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/init(tcpport:))*