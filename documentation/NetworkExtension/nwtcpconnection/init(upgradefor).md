# init(upgradeFor:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

This convenience initializer can be used to create a new connection that will only be connected if there exists a better path (as determined by the system) to the remote endpoint of the original connection.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_create(_:_:)`](../../Network/nw_connection_create%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
init(upgradeFor connection: NWTCPConnection)
```

```objc
- (instancetype) initWithUpgradeForConnection:(NWTCPConnection *) connection;
```

#### Discussion

An upgraded connection will be initialized using the same remote endpoint and set of parameters from the original connection. If the original connection becomes disconnected or cancelled, the new upgrade connection will automatically be considered better.

The caller should create an [`NWTCPConnection`](../nwtcpconnection.md) and watch for the `hasBetterPath` property. When this property is [`true`](../../Swift/true.md), the caller should attempt to create a new upgrade connection, with the goal to start transferring data on the new connection path as soon as possible to reduce power and avoid expensive networks. When the new connection is successfully connected the caller can start using the new connection and cancel the original one.

## See Also

### Responding to network changes
- [var hasBetterPath: Bool](./hasbetterpath.md)
  If a connection has a better path, new connections would use a different interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/init(upgradefor:))*