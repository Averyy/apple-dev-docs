# isViable

**Framework**: Network Extension  
**Kind**: property

The viability of a TCP connection indicates whether or not data can be transferred.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isViable: Bool { get }
```

#### Discussion

Evaluates to [`true`](https://developer.apple.com/documentation/Swift/true) if the connection can read and write data, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. Use Key-Value Observing to watch this property.

## See Also

- [var state: NWTCPConnectionState](nwtcpconnection/state.md)
  The status of the connection.
- [enum NWTCPConnectionState](nwtcpconnectionstate.md)
  Defined connection states. New types may be defined in the future.
- [var error: (any Error)?](nwtcpconnection/error.md)
  The connection-wide error property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/isviable)*