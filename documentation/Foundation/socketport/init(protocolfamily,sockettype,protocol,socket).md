# init(protocolFamily:socketType:protocol:socket:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver with a previously created local socket.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(protocolFamily family: Int32, socketType type: Int32, protocol: Int32, socket sock: SocketNativeHandle)
```

```objc
- (instancetype) initWithProtocolFamily:(int) family socketType:(int) type protocol:(int) protocol socket:(NSSocketNativeHandle) sock;
```

## Return Value

A local socket port initialized with the provided socket.

## Parameters

- `family`: The protocol family for the provided socket. Possible values are defined in `<sys/socket.h>`, such as `AF_LOCAL`, `AF_INET`, and `AF_INET6`.
- `type`: The type of the provided socket.
- `protocol`: The specific protocol the provided socket uses.
- `sock`: The previously created socket.

## See Also

### Creating Instances
- [convenience init()](./init%28%29.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [convenience init?(tcpPort: UInt16)](./init%28tcpport%29-6hgbo.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](./init%28protocolfamily,sockettype,protocol,address%29.md)
  Initializes the receiver as a local socket with the provided arguments.
- [convenience init?(remoteWithTCPPort: UInt16, host: String?)](./init%28remotewithtcpport,host%29.md)
  Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](./init%28remotewithprotocolfamily,sockettype,protocol,address%29.md)
  Initializes the receiver as a remote socket with the provided arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/init(protocolfamily:sockettype:protocol:socket:))*