# NWTCPConnectionState.connected

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

The connection is established. It is now possible to transfer data. If TLS is in use, the TLS handshake has finished.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_state_t`](../../Network/nw_connection_state_t.md) type from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
case connected
```

```c
NWTCPConnectionStateConnected
```

## See Also

### Connection States
- [NWTCPConnectionState.invalid](./invalid.md)
  The connection is in an invalid or uninitialized state.
- [NWTCPConnectionState.connecting](./connecting.md)
  The connection is attempting to connect. This includes endpoint resolution when applicable.
- [NWTCPConnectionState.waiting](./waiting.md)
  The connection has attempted to connect but failed. It is now waiting for better conditions before trying again.
- [NWTCPConnectionState.disconnected](./disconnected.md)
  The connection is disconnected. It is no longer possible to transfer data. The application should call `cancel` to clean up resources.
- [NWTCPConnectionState.cancelled](./cancelled.md)
  The connection has been cancelled by the client calling `cancel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/connected)*