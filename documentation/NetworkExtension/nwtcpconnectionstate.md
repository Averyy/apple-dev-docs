# NWTCPConnectionState

**Framework**: Network Extension  
**Kind**: enum

Defined connection states. New types may be defined in the future.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NWTCPConnectionState
```

## Topics

### Connection States
- [NWTCPConnectionState.invalid](nwtcpconnectionstate/invalid.md)
  The connection is in an invalid or uninitialized state.
- [NWTCPConnectionState.connecting](nwtcpconnectionstate/connecting.md)
  The connection is attempting to connect. This includes endpoint resolution when applicable.
- [NWTCPConnectionState.waiting](nwtcpconnectionstate/waiting.md)
  The connection has attempted to connect but failed. It is now waiting for better conditions before trying again.
- [NWTCPConnectionState.connected](nwtcpconnectionstate/connected.md)
  The connection is established. It is now possible to transfer data. If TLS is in use, the TLS handshake has finished.
- [NWTCPConnectionState.disconnected](nwtcpconnectionstate/disconnected.md)
  The connection is disconnected. It is no longer possible to transfer data. The application should call `cancel` to clean up resources.
- [NWTCPConnectionState.cancelled](nwtcpconnectionstate/cancelled.md)
  The connection has been cancelled by the client calling `cancel`.
### Initializers
- [init?(rawValue: Int)](nwtcpconnectionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: NWTCPConnectionState](nwtcpconnection/state.md)
  The status of the connection.
- [var isViable: Bool](nwtcpconnection/isviable.md)
  The viability of a TCP connection indicates whether or not data can be transferred.
- [var error: (any Error)?](nwtcpconnection/error.md)
  The connection-wide error property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate)*