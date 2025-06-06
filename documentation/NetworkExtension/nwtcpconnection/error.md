# error

**Framework**: Network Extension  
**Kind**: property

The connection-wide error property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

Indicates any fatal error that occurred while processing the connection or performing data reading or writing. Use Key-Value Observing to watch this property.

## See Also

- [var state: NWTCPConnectionState](nwtcpconnection/state.md)
  The status of the connection.
- [enum NWTCPConnectionState](nwtcpconnectionstate.md)
  Defined connection states. New types may be defined in the future.
- [var isViable: Bool](nwtcpconnection/isviable.md)
  The viability of a TCP connection indicates whether or not data can be transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/error)*