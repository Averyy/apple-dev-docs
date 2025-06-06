# newConnectionHandler

**Framework**: Network  
**Kind**: property

A handler that receives inbound connections.

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
@preconcurrency
final var newConnectionHandler: ((NWConnection) -> Void)? { get set }
```

#### Discussion

Upon receiving a new connection, you should set update handlers on the connection and start it in order to accept it. If you want to reject the connection, cancel the connection.

## See Also

- [var newConnectionLimit: Int](nwlistener/newconnectionlimit.md)
  The remaining number of inbound connections to deliver before rejecting connections.
- [static let InfiniteConnectionLimit: Int](nwlistener/infiniteconnectionlimit.md)
  A static value to indicate that inbound connections should not be limited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/newconnectionhandler)*