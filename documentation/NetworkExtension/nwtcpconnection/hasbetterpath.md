# hasBetterPath

**Framework**: Network Extension  
**Kind**: property

If a connection has a better path, new connections would use a different interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var hasBetterPath: Bool { get }
```

#### Discussion

Evaluates to [`true`](https://developer.apple.com/documentation/Swift/true) if a new connection attempt to the remote endpoint would use a different and preferred path. If the current connection is not viable, this can be used as a hint to try again. If the current connection is still viable, this can indicate that the system or user has a preference for the newly available network path. For example, if the connection is established over a cellular data network and Wi-Fi is now available, then the connection has a better path available and this property is set to [`true`](https://developer.apple.com/documentation/Swift/true). Use the `initWithUpgradeForConnection:` initializer to create a new connection with the same parameters as the current connection. Use Key-Value Observing to watch this property.

## See Also

- [var isViable: Bool](nwtcpconnection/isviable.md)
  The viability of a TCP connection indicates whether or not data can be transferred.
- [init(upgradeFor: NWTCPConnection)](nwtcpconnection/init(upgradefor:).md)
  This convenience initializer can be used to create a new connection that will only be connected if there exists a better path (as determined by the system) to the remote endpoint of the original connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/hasbetterpath)*