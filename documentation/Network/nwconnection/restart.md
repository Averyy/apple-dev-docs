# restart()

**Framework**: Network  
**Kind**: method

Restarts a connection that is in the waiting state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
final func restart()
```

#### Discussion

Restart a connection when it is in the waiting state and you have reason to believe the connection may succeed if it tries again. Connections that are waiting will automatically restart on network path changes.

## See Also

- [convenience init(host: NWEndpoint.Host, port: NWEndpoint.Port, using: NWParameters)](nwconnection/init(host:port:using:).md)
  Initializes a new connection to a host and port.
- [init(to: NWEndpoint, using: NWParameters)](nwconnection/init(to:using:).md)
  Initializes a new connection to a remote endpoint.
- [func start(queue: DispatchQueue)](nwconnection/start(queue:).md)
  Starts establishing a connection, and sets the queue on which to deliver all connection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/restart())*