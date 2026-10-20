# NWTCPConnectionState

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

Defined connection states. New types may be defined in the future.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_state_t`](../Network/nw_connection_state_t.md) type from the [Network](../Network/Network.md) framework instead.

## Declaration

```swift
enum NWTCPConnectionState
```

```c
enum NWTCPConnectionState : NSInteger;
```

## Topics

### Connection States
- [NWTCPConnectionState.invalid](./nwtcpconnectionstate/invalid.md)
  The connection is in an invalid or uninitialized state.
- [NWTCPConnectionState.connecting](./nwtcpconnectionstate/connecting.md)
  The connection is attempting to connect. This includes endpoint resolution when applicable.
- [NWTCPConnectionState.waiting](./nwtcpconnectionstate/waiting.md)
  The connection has attempted to connect but failed. It is now waiting for better conditions before trying again.
- [NWTCPConnectionState.connected](./nwtcpconnectionstate/connected.md)
  The connection is established. It is now possible to transfer data. If TLS is in use, the TLS handshake has finished.
- [NWTCPConnectionState.disconnected](./nwtcpconnectionstate/disconnected.md)
  The connection is disconnected. It is no longer possible to transfer data. The application should call `cancel` to clean up resources.
- [NWTCPConnectionState.cancelled](./nwtcpconnectionstate/cancelled.md)
  The connection has been cancelled by the client calling `cancel`.
### Initializers
- [init?(rawValue: Int)](./nwtcpconnectionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Monitoring the connection status
- [var state: NWTCPConnectionState](./nwtcpconnection/state.md)
  The status of the connection.
- [var isViable: Bool](./nwtcpconnection/isviable.md)
  The viability of a TCP connection indicates whether or not data can be transferred.
- [var error: (any Error)?](./nwtcpconnection/error.md)
  The connection-wide error property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate)*