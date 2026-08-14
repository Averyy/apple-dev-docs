# init(upgradeFor:)

**Framework**: Network Extension  
**Kind**: init

This convenience initializer can be used to create a new connection that will only be connected if there exists a better path (as determined by the system) to the remote endpoint of the original connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(upgradeFor connection: NWTCPConnection)
```

#### Discussion

An upgraded connection will be initialized using the same remote endpoint and set of parameters from the original connection. If the original connection becomes disconnected or cancelled, the new upgrade connection will automatically be considered better.

The caller should create an [`NWTCPConnection`](nwtcpconnection.md) and watch for the `hasBetterPath` property. When this property is [`true`](https://developer.apple.com/documentation/swift/true), the caller should attempt to create a new upgrade connection, with the goal to start transferring data on the new connection path as soon as possible to reduce power and avoid expensive networks. When the new connection is successfully connected the caller can start using the new connection and cancel the original one.

## See Also

- [var hasBetterPath: Bool](nwtcpconnection/hasbetterpath.md)
  If a connection has a better path, new connections would use a different interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/init(upgradefor:))*