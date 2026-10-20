# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init()
```

```objc
- (instancetype) init;
```

#### Return Value

An initialized local TCP/IP socket port of type `SOCK_STREAM`.

#### Discussion

The port number is selected by the system.

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Creating Instances
- [convenience init?(tcpPort: UInt16)](./init%28tcpport%29-6hgbo.md)
  Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](./init%28protocolfamily,sockettype,protocol,address%29.md)
  Initializes the receiver as a local socket with the provided arguments.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, socket: SocketNativeHandle)](./init%28protocolfamily,sockettype,protocol,socket%29.md)
  Initializes the receiver with a previously created local socket.
- [convenience init?(remoteWithTCPPort: UInt16, host: String?)](./init%28remotewithtcpport,host%29.md)
  Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](./init%28remotewithprotocolfamily,sockettype,protocol,address%29.md)
  Initializes the receiver as a remote socket with the provided arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/init())*