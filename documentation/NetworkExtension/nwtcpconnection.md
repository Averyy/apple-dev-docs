# NWTCPConnection

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An object to manage a TCP connection, with or without TLS.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_t`](../Network/nw_connection_t.md) type from the [Network](../Network/Network.md) framework instead.

## Declaration

```swift
class NWTCPConnection
```

```objc
@interface NWTCPConnection : NSObject
```

## Topics

### Monitoring the connection status
- [var state: NWTCPConnectionState](./nwtcpconnection/state.md)
  The status of the connection.
- [enum NWTCPConnectionState](./nwtcpconnectionstate.md)
  Defined connection states. New types may be defined in the future.
- [var isViable: Bool](./nwtcpconnection/isviable.md)
  The viability of a TCP connection indicates whether or not data can be transferred.
- [var error: (any Error)?](./nwtcpconnection/error.md)
  The connection-wide error property.
### Transferring data
- [func readMinimumLength(Int, maximumLength: Int, completionHandler: (Data?, (any Error)?) -> Void)](./nwtcpconnection/readminimumlength%28_,maximumlength,completionhandler%29.md)
  Read the requested range of bytes.
- [func readLength(Int, completionHandler: (Data?, (any Error)?) -> Void)](./nwtcpconnection/readlength%28_,completionhandler%29.md)
  Read a certain number of bytes on a connection.
- [func write(Data, completionHandler: ((any Error)?) -> Void)](./nwtcpconnection/write%28_,completionhandler%29.md)
  Write the data to the connection.
- [func writeClose()](./nwtcpconnection/writeclose%28%29.md)
  Close the connection for writing.
### Canceling the connection
- [func cancel()](./nwtcpconnection/cancel%28%29.md)
  Cancel the connection.
### Responding to network changes
- [var hasBetterPath: Bool](./nwtcpconnection/hasbetterpath.md)
  If a connection has a better path, new connections would use a different interface.
- [init(upgradeFor: NWTCPConnection)](./nwtcpconnection/init%28upgradefor%29.md)
  This convenience initializer can be used to create a new connection that will only be connected if there exists a better path (as determined by the system) to the remote endpoint of the original connection.
### Getting connection properties
- [var endpoint: NWEndpoint](./nwtcpconnection/endpoint.md)
  The destination endpoint with which this connection was created.
- [var localAddress: NWEndpoint?](./nwtcpconnection/localaddress.md)
  The IP address endpoint from which the connection was established.
- [var remoteAddress: NWEndpoint?](./nwtcpconnection/remoteaddress.md)
  The IP address endpoint to which the connection was established.
- [var connectedPath: NWPath?](./nwtcpconnection/connectedpath.md)
  The network path over which the connection was established.
- [var txtRecord: Data?](./nwtcpconnection/txtrecord.md)
  The TXT record associated with a connected Bonjour service endpoint.
### Initializers
- [init(upgradeForConnection: NWTCPConnection)](./nwtcpconnection/init%28upgradeforconnection%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### TCP connections
- [class NWTLSParameters](./nwtlsparameters.md)
  TLS properties for creating a connection.
- [protocol NWTCPConnectionAuthenticationDelegate](./nwtcpconnectionauthenticationdelegate.md)
  A delegate protocol to customize the TLS authentication done by a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection)*