# init(to:using:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a new connection to a remote endpoint.

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
init(to: NWEndpoint, using: NWParameters)
```

## See Also

### Creating Connections
- [convenience init(host: NWEndpoint.Host, port: NWEndpoint.Port, using: NWParameters)](./init%28host,port,using%29.md)
  Initializes a new connection to a host and port.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Starts establishing a connection, and sets the queue on which to deliver all connection events.
- [func restart()](./restart%28%29.md)
  Restarts a connection that is in the waiting state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/init(to:using:))*