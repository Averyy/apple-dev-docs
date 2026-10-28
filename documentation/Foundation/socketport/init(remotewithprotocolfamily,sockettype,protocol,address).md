# init(remoteWithProtocolFamily:socketType:protocol:address:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver as a remote socket with the provided arguments.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init(remoteWithProtocolFamily family: Int32, socketType type: Int32, protocol: Int32, address: Data)
```

```objc
- (instancetype) initRemoteWithProtocolFamily:(int) family socketType:(int) type protocol:(int) protocol address:(NSData *) address;
```

## Discussion

A connection is not opened to the remote address until data is sent.

## Parameters

- `family`: The protocol family for the socket port. Possible values are defined in `<sys/socket.h>`, such as `AF_LOCAL`, `AF_INET`, and `AF_INET6`.
- `type`: The type of socket.
- `protocol`: The specific protocol to use from the protocol family.
- `address`: The family-specific socket address for the receiver copied into an `NSData` object.

## See Also

### Creating Instances
- [convenience init()](./init%28%29.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [convenience init?(tcpPort: UInt16)](./init%28tcpport%29-6hgbo.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](./init%28protocolfamily,sockettype,protocol,address%29.md)
  Initializes the receiver as a local socket with the provided arguments.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, socket: SocketNativeHandle)](./init%28protocolfamily,sockettype,protocol,socket%29.md)
  Initializes the receiver with a previously created local socket.
- [convenience init?(remoteWithTCPPort: UInt16, host: String?)](./init%28remotewithtcpport,host%29.md)
  Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/init(remotewithprotocolfamily:sockettype:protocol:address:))*