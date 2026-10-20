# init(remoteWithTCPPort:host:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init?(remoteWithTCPPort port: UInt16, host hostName: String?)
```

```objc
- (instancetype) initRemoteWithTCPPort:(unsigned short) port host:(NSString *) hostName;
```

#### Return Value

A TCP/IP socket port of type `SOCK_STREAM` that can connect to the remote host `hostName` on port `port`.

#### Discussion

A connection is not opened to the remote host until data is sent.

## Parameters

- `port`: The port to connect to.
- `hostName`: The host name to connect to. `hostName` may be either a host name or an IPv4-style address.

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
- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](./init%28remotewithprotocolfamily,sockettype,protocol,address%29.md)
  Initializes the receiver as a remote socket with the provided arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/init(remotewithtcpport:host:))*